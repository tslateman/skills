---
name: python-review
description: >
  Review Python code for agent-typical anti-patterns: blind except and
  try/except/pass error swallowing, type-ignore and Any sprinkled to
  silence the checker, string-matched exception handling, .get() defaults
  hiding missing keys, noqa suppression. Runs Ruff with a targeted rule
  set, then judges each trigger with a design lens. Use when: reviewing
  agent-written Python, before committing Python changes, or on "python
  review", "review this python", "ruff pass", "check for except abuse".
  For generic bug hunts use /code-review; for generic judgment use
  /duet:vibe-check.
argument-hint: "[path or package to review, defaults to working-tree changes]"
---

# Python Review — Local-Fix Debt Audit

Python's dynamism means the interpreter rarely pushes back, so the
agent-typical minimal edit is a _silencer_: wrap the failing call in
`try/except: pass`, add `# type: ignore`, default the missing key with
`.get(k, "")`. Each edit makes the traceback vanish; the bug moves
downstream and loses its stack trace on the way. This review hunts that
debt class specifically.

## Context

Changed files:
!`git diff --name-only HEAD 2>/dev/null | grep '\.py$' || echo "(not a git repo or no changed .py files — review the given path instead)"`

## Process

### Step 1: Scope

Review `$ARGUMENTS` if given; otherwise the changed `.py` files above;
otherwise ask which package. Read the scoped files fully before judging —
every finding needs the surrounding control flow, not just the line.

### Step 2: Mechanical Pass

Run Ruff with the targeted rule set (project rules plus the ones that
catch this debt class):

```bash
uvx ruff check --select E722,BLE,TRY,B,SIM,ARG,RET,RUF --output-format concise .
```

- `E722`/`BLE` — bare and blind excepts
- `TRY` — exception handling design (tryceratops)
- `B` — bugbear: mutable defaults, no-op assertions
- `SIM`/`RET` — collapsible conditionals, dead branches

If the project pins its own Ruff config (`pyproject.toml`, `ruff.toml`),
respect it and say so. If a type checker is configured (mypy, pyright,
ty), run it too — type errors that were silenced rather than fixed are
the core of this review.

Then grep the scoped files for triggers Ruff can't judge:

| Trigger                               | Suspicion                                                      |
| ------------------------------------- | -------------------------------------------------------------- |
| `except Exception:` / `except: pass`  | Error swallowing — which specific exception was expected?      |
| `# type: ignore` / `# noqa` / `cast(` | Who silenced the checker, and is the reason written down?      |
| `Any` in signatures                   | Typing given up at the boundary — callers inherit the fog      |
| `.get(key, default)`                  | Legitimate optional, or a KeyError hidden behind a default?    |
| `str(e)` comparison / `in str(e)`     | Exception control flow by string match — wants exception types |
| `hasattr`/`getattr` with defaults     | Duck-typing check, or an AttributeError silencer?              |
| `isinstance` chains                   | Usually polymorphism or `match` in disguise                    |
| Mutable default args                  | Classic footgun (bugbear catches most)                         |

### Step 3: Judgment Pass

For each trigger hit, decide which of three buckets it belongs in —
this is the review's actual work:

1. **Fine** — idiomatic, or the pragmatic choice is documented.
   `except KeyError` around one dict access with a comment is not a
   finding; `dict.get` for a genuinely optional field is not a finding.
2. **Mechanical fix** — safe local rewrite: narrow the except to the
   expected exception, replace `type: ignore` with the actual type,
   convert isinstance chain to `match`, raise instead of default.
3. **Design restructure** — the silencer exists because the design
   fights the data flow: exceptions carrying meaning in their message
   strings (wants an exception hierarchy), `Any` at a module boundary
   (wants a Protocol or TypedDict), optionality smeared through every
   caller (wants validation at the edge, e.g. pydantic). Name the
   restructure and its blast radius. Do not apply it without asking —
   this bucket is why the review exists.

A repeated trigger is one finding, not many: five `.get(k, "")` on the
same payload point at one unvalidated boundary.

### Step 4: Report

Findings ordered by severity, each with `file:line`, the bucket, why it
matters in one sentence, and the suggested fix. Then a one-paragraph
verdict: does this code fail loudly at the boundary, or quietly
downstream? End with the counts: N fine / N mechanical / N restructure.

If the user asks you to apply fixes, apply bucket 2 directly and
run Ruff plus the test suite after; bucket 3 gets a plan first.

## Rules

- Never suggest `except Exception`, `# type: ignore`, or a default
  value as a fix.
- "No traceback" is the floor, not the verdict — a swallowed error is
  worse than a raised one.
- Judge `.get()` and `getattr` by whether absence is a valid state,
  not by whether the code runs.
