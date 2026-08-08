---
name: go-review
description: >
  Review Go code for agent-typical anti-patterns: discarded or unwrapped
  errors, string-matched error handling instead of errors.Is/As, panic as
  control flow, any plus type switches to bypass the type system, nolint
  suppression, leaked goroutines. Runs go vet and golangci-lint with a
  targeted linter set, then judges each trigger with an error-contract
  lens. Use when: reviewing agent-written Go, before committing Go
  changes, or on "go review", "review this go", "lint pass", "check
  error handling". For generic bug hunts use /code-review; for generic
  judgment use /vibe-check.
argument-hint: "[path or package to review, defaults to working-tree changes]"
---

# Go Review — Local-Fix Debt Audit

Go makes errors values, so the agent-typical minimal edit is to make
the value go away: `_ = err`, a bare `return err` that strips context,
`strings.Contains(err.Error(), ...)` when the typed error was too much
work. Each edit compiles and often passes tests; the debt surfaces as
undebuggable failures with no cause chain. This review hunts that debt
class specifically.

## Context

Changed files:
!`git diff --name-only HEAD 2>/dev/null | grep '\.go$' || echo "(not a git repo or no changed .go files — review the given path instead)"`

## Process

### Step 1: Scope

Review `$ARGUMENTS` if given; otherwise the changed `.go` files above;
otherwise ask which package. Read the scoped files fully before judging —
every finding needs the surrounding error contract, not just the line.

### Step 2: Mechanical Pass

```bash
go vet ./...
golangci-lint run --enable errcheck,errorlint,staticcheck,ineffassign,unparam,bodyclose,noctx,contextcheck
```

- `errcheck` — discarded error returns
- `errorlint` — `==` comparisons and type asserts on wrapped errors
- `bodyclose`/`noctx`/`contextcheck` — leaked responses, missing context

If the project has `.golangci.yml`, run its pinned set instead and say
so (an unpinned linter set drifts — flag its absence as an observation,
not a finding).

Then grep the scoped files for triggers the linters can't judge:

| Trigger                                           | Suspicion                                                                                 |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `_ =` on an error return                          | Deliberate discard, or a silencer? Deliberate wants a comment                             |
| `err.Error() ==` / `strings.Contains(err.Error()` | Error control flow by string match — wants `errors.Is`/`As` with sentinel or typed errors |
| bare `return err` up a long chain                 | Context stripped — wants `fmt.Errorf("doing X: %w", err)`                                 |
| `panic(` outside main/init                        | Error return path abandoned                                                               |
| `interface{}` / `any` + type switch               | Type system bypassed — what did the signature give up?                                    |
| `//nolint`                                        | Who silenced the linter, and is the reason written down?                                  |
| `go func(` without WaitGroup/errgroup/context     | Goroutine with no lifecycle — leak or lost error                                          |
| `time.Sleep` in tests or sync code                | Timing guess standing in for synchronization                                              |

### Step 3: Judgment Pass

For each trigger hit, decide which of three buckets it belongs in —
this is the review's actual work:

1. **Fine** — idiomatic, or the pragmatic choice is documented.
   `_ = f.Close()` on a read-only file with a comment is not a finding;
   `panic` in an init-time invariant is defensible.
2. **Mechanical fix** — safe local rewrite: wrap with `%w` and a verb
   phrase, replace string match with `errors.Is` against an existing
   sentinel, hand the goroutine an errgroup.
3. **Error-contract restructure** — the string match or discard exists
   because the package never defined its error contract: no sentinel
   errors, no typed errors, meaning lives only in message text. Name
   the restructure (exported sentinels, a typed error with fields,
   context threading through the call chain) and its blast radius.
   Do not apply it without asking — this bucket is why the review
   exists.

A repeated trigger is one finding, not many: five string matches on the
same error text point at one package's missing error contract.

### Step 4: Report

Findings ordered by severity, each with `file:line`, the bucket, why it
matters in one sentence, and the suggested fix. Then a one-paragraph
verdict: when this code fails, does the error arrive with a cause chain
or as an orphaned string? End with the counts: N fine / N mechanical /
N restructure.

If the user asks you to apply fixes, apply bucket 2 directly and run
the linters plus `go test -race ./...` after; bucket 3 gets a plan
first.

## Rules

- Never suggest `_ =`, `//nolint`, or string matching as a fix.
- Compiling and green tests are the floor, not the verdict — Go's
  compiler does not check error handling quality.
- Judge `any` by what the signature gave up, not by whether a type
  switch recovers it downstream.
