---
name: rust-review
description: >
  Review Rust code for agent-typical anti-patterns: clone-to-satisfy-the-
  borrow-checker, silent error swallowing, string-matched error control
  flow, bare unwrap, lint suppression. Runs Clippy with a strict targeted
  lint set, then judges each trigger with an ownership and architecture
  lens. Use when: reviewing agent-written Rust, before committing Rust
  changes, or on "rust review", "review this rust", "clippy pass",
  "check for clone abuse". For generic bug hunts use /code-review; for
  generic judgment use /duet:vibe-check.
argument-hint: "[path or crate to review, defaults to working-tree changes]"
---

# Rust Review — Local-Fix Debt Audit

Agent-written Rust has a signature failure mode: the minimal local edit
that makes the compiler error vanish. `.clone()` silences the borrow
checker, `unwrap_or_default()` silences a Result, `#[allow]` silences a
lint. Each edit compiles; the debt is architectural and invisible to
`cargo check`. This review hunts that debt class specifically.

Reference: Rust Design Patterns book, anti-patterns section
(rust-unofficial.github.io/patterns/anti_patterns/), especially
"Clone to satisfy the borrow checker".

## Context

Changed files:
!`git diff --name-only HEAD 2>/dev/null | grep '\.rs$' || echo "(not a git repo or no changed .rs files — review the given path instead)"`

## Process

### Step 1: Scope

Review `$ARGUMENTS` if given; otherwise the changed `.rs` files above;
otherwise ask which crate. Read the scoped files fully before judging —
every finding needs the surrounding ownership context, not just the line.

### Step 2: Mechanical Pass

Run Clippy with the targeted lint set (default lints plus the ones that
catch this debt class):

```bash
cargo clippy --all-targets -- \
  -W clippy::unwrap_used \
  -W clippy::redundant_clone \
  -W clippy::clone_on_ref_ptr \
  -W clippy::needless_pass_by_value \
  -W clippy::or_fun_call \
  -W clippy::comparison_chain \
  -W clippy::large_types_passed_by_value
```

Note: `redundant_clone` is a nursery lint — treat its hits as leads to
verify, not verdicts. If the workspace has its own lint config
(`[lints]` in Cargo.toml, clippy.toml), respect it and say so.

Then grep the scoped files for triggers Clippy can't judge:

| Trigger                                         | Suspicion                                                                             |
| ----------------------------------------------- | ------------------------------------------------------------------------------------- |
| `.clone()`                                      | Borrow-checker silencer? Or legitimate ownership transfer / `Rc`/`Arc` refcount bump? |
| `.unwrap()`                                     | Should be `expect("why this holds")` or `?` propagation                               |
| `unwrap_or_default()` / `.ok()` discarding      | Silent error swallowing — is the error genuinely ignorable?                           |
| `.contains(` / `.starts_with(` on error strings | Error control flow by string match — wants enum variants (`thiserror`)                |
| `else if let` chains                            | Usually a `match` in disguise                                                         |
| `#[allow(`                                      | Who silenced the lint, and is the reason written down?                                |
| `unsafe`, `as` casts                            | Standard scrutiny: invariant documented?                                              |

### Step 3: Judgment Pass

For each trigger hit, decide which of three buckets it belongs in —
this is the review's actual work:

1. **Fine** — idiomatic, or the pragmatic choice is documented.
   `Arc::clone` for a thread handoff is not a finding.
2. **Mechanical fix** — safe local rewrite: `unwrap` → `expect`/`?`,
   `else if let` chain → `match`, drop a provably redundant clone.
3. **Ownership restructure** — the clone/swallow exists because the
   ownership design fights the code's actual data flow. Name the
   restructure (borrow instead of own, `Cow`, lifetimes on the struct,
   error enum with variants) and its blast radius. Do not apply it
   without asking — this bucket is why the review exists.

A repeated trigger is one finding, not many: five clones of the same
`String` field point at one struct's ownership design.

### Step 4: Report

Findings ordered by severity, each with `file:line`, the bucket, why it
matters in one sentence, and the suggested fix. Then a one-paragraph
verdict: is this code compile-shaped or design-shaped? End with the
counts: N fine / N mechanical / N restructure.

If the user asks you to apply fixes, apply bucket 2 directly and
`cargo clippy && cargo test` after; bucket 3 gets a plan first.

## Rules

- Never suggest `.clone()` or `#[allow]` as a fix.
- `cargo check` passing is the floor, not the verdict.
- Judge clones by what the data flow wants, not by count — one clone in
  a hot loop outranks ten in startup config parsing.
