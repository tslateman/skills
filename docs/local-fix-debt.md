# Local-Fix Debt

The thesis behind every skill in this repo.

## The mechanism

An agent given a failing signal — a compiler error, a lint warning, a red test —
searches for the smallest edit that clears it. This is not a defect in the
agent. It is what "fix the error" means when the error is the only feedback
available, and a human under the same pressure reaches for the same edits.

The problem is that clearing a signal and fixing a cause are different
operations that look identical from outside. Both end with a green build.

```text
signal ──▶ [ fix the cause ]     ──▶ green   the failure cannot recur
       └─▶ [ silence the signal ] ──▶ green   the failure recurs, undetected
```

**Local-fix debt** is the accumulated second path. Three properties make it
worse than ordinary technical debt:

1. **It is invisible to the tool it silenced.** A `# type: ignore` is not
   findable by the type checker. That is the entire purpose of the annotation.
   Running the linter harder will never surface it.
2. **It relocates the failure.** The error does not stop happening; it stops
   being reported at the place it happened. It resurfaces downstream, without
   the stack that would explain it.
3. **It is invisible in review.** Each edit is one token, one line, defensible in
   isolation. The debt is in the aggregate, and only a reader asking _why is this
   here_ can see it.

## Why every language has one

A silencer is the escape hatch a language provides for the constraint it
enforces. Strong constraints produce sharp escape hatches, which is why the
strictest languages have the most characteristic failure mode.

| Language       | Enforces                     | Escape hatch                  | What it costs                          |
| -------------- | ---------------------------- | ----------------------------- | -------------------------------------- |
| **Go**         | Errors are values you handle | `_ = err`, bare `return err`  | The cause chain                        |
| **Rust**       | Ownership and lifetimes      | `.clone()`, `.unwrap()`       | The ownership design, then the process |
| **TypeScript** | Static types, opt-out        | `as any`, `!`, `@ts-ignore`   | The guarantee the type was making      |
| **Python**     | Nothing, at runtime          | `except: pass`, `.get(k, "")` | The traceback                          |
| **Shell**      | Nothing, by default          | `2>/dev/null`, `\|\| true`    | Any evidence that it failed            |
| **Tests**      | Only what you assert         | Assert what the code just did | The detection power the suite claims   |

Python and shell invert the pattern: they enforce so little that the silencer
is not an escape hatch but the _default behavior_. There, the review looks for
what was never added — a narrowed exception, `set -euo pipefail` — rather than
what was inserted.

## Why a linter cannot find it

Linters answer "does this code match a known-bad pattern." Local-fix debt asks a
different question: **which specific failure was this suppression meant to
catch?**

That question has three possible answers, and only one is fine:

- A named, expected error — the suppression is correct and should say so
- An unnamed error the author never diagnosed — a finding
- The author does not know — the strongest finding of the three

No static tool can distinguish these, because the distinction lives in intent.
Which is why every skill here runs the linter first and then does its actual
work: judging each hit.

## The three buckets

Every trigger sorts into one of three, and the sorting is the review.

### 1. Fine

Idiomatic, or the pragmatic choice is documented. `Arc::clone` for a thread
handoff. `_ = f.Close()` on a read-only file with a comment.
`command -v foo >/dev/null 2>&1` as a presence check. `dict.get` where absence
is a valid state.

The test is whether the specific failure being suppressed can be named. If it
can, the code is fine and the comment should record it.

### 2. Mechanical fix

The intent is right, the execution leaks. A safe, local, verifiable rewrite:
narrow the except, wrap with `%w`, replace the cast with a type guard, quote
the expansion, swap the sleep for a wait-for-condition.

These are applied directly, then verified by re-running the linter and the
tests.

### 3. Restructure

The silencer exists because the design fights the data flow. This is the bucket
the review exists to surface:

- Five string matches on error text → the package never defined an error contract
- Five `as any` on one API response → an unvalidated boundary
- Twelve tests mocking one collaborator → a seam that resists testing
- Six `2>/dev/null || true` in one hook → no error strategy at all

Restructures are named with their blast radius and never applied without asking.
The repetition is the signal: **a repeated trigger is one finding, not many.**

## The standing rule

> Green is the floor, not the verdict.

A silenced error and a handled error look identical from outside. A test that
cannot fail and a test that passes look identical from outside. A quiet script
and a working script look identical from outside.

Every skill in this repo exists to tell those pairs apart, and none of them
accepts a passing build as evidence.
