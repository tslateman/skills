---
name: vibe-check
description: Judgment linter for vibe-coded output: reads the energy of the code, not just correctness. Use when the user says "vibe check", "does this hold up", "sanity check this AI code", or after a fast generation session before committing.
---

# Vibe Check

## Overview

"Vibe check?", a way of asking _what's the energy like right now?_

Static linters catch syntax. Code review catches everything but takes time. Vibe-check sits between: a quick judgment pass that asks whether AI-generated code feels like it was written with thought or just generated on autopilot.

Single-agent, one pass. Runs on the diff by default. Surfaces higher-order problems that require reasoning, the things a thoughtful reviewer notices in the first 30 seconds that no regex can detect.

## Input

**Default:** Git diff (staged if present, unstaged otherwise).

```bash
# Check current changes
/vibe-check

# Check specific files or directories
/vibe-check src/auth/
```

**Override:** Named files or directories passed as arguments.

## Assertion Categories

Each category reads a specific vibe. Findings require AI judgment, if a static linter could catch it, it doesn't belong here.

| Category                  | The vibe                                             | What it catches                                                                                                                    |
| ------------------------- | ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Earned complexity**     | "This feels over-engineered"                         | Abstractions that don't justify themselves, premature generalization, indirection without payoff                                   |
| **Prompt-shaped code**    | "This feels shaped by the prompt, not the problem"   | Odd boundaries, misnamed concepts, structure that mirrors how the request was worded rather than the domain                        |
| **Missing skepticism**    | "This feels like nothing can go wrong"               | Happy-path-only logic, unchallenged assumptions, no failure modes considered, silent swallowing of errors                          |
| **Cargo-culted patterns** | "This feels ceremonial"                              | Design patterns applied without justification, boilerplate that adds ceremony without value, framework idioms used out of context  |
| **Integration blindness** | "This feels written in a vacuum"                     | Duplicates existing utilities, contradicts established codebase patterns, ignores conventions visible in surrounding code          |
| **Shallow naming**        | "This feels like nobody thought about what it means" | Names describe implementation (`handleData`, `processItems`) instead of intent, a signal the author didn't reason about the domain |
| **Security surface**      | "This feels like it trusts too much"                 | Auth gaps, unsanitized boundaries, trust assumptions, only the ones requiring judgment, not what semgrep catches                   |

## Severity

Each category defaults to a severity level. Users can override per-category.

| Level     | Meaning                         |
| --------- | ------------------------------- |
| **error** | Must address before committing  |
| **warn**  | Worth considering, not blocking |
| **off**   | Skip this category              |

**Defaults:**

- **error:** missing-skepticism, security-surface
- **warn:** earned-complexity, prompt-shaped-code, cargo-culted-patterns, integration-blindness, shallow-naming

## Workflow

### 1. Gather the Code

Read the git diff or specified files. Identify the languages and frameworks involved.

### 2. Read the Room

For each assertion category (unless severity is `off`), scan the code and ask the category's question. Apply language-aware judgment:

- **Python:** mutable default args, bare `except`, implicit `None` returns
- **JavaScript/TypeScript:** `==` vs `===`, unhandled promise rejections, prototype pollution
- **Go:** unchecked errors, goroutine leaks
- **Rust:** unnecessary `unwrap()`, `clone()` to satisfy the borrow checker
- **General:** any language-specific footgun that a vibe coder would hit

### 3. Report Findings

Group findings by category. Each finding includes:

```
## Prompt-Shaped Code (warn)

- `src/auth/handler.ts:42` — Function boundary splits "validate" and "authorize" because the prompt asked for them separately, but they share all context and should be one operation
- `src/auth/types.ts:8` — `RequestData` is a generic wrapper that mirrors the prompt's language ("request data") rather than the domain concept (`AuthAttempt`)
```

### 4. Summarize

End with a summary line:

```
vibe-check: 2 errors, 4 warnings across 3 files
```

### 5. Escalate (if needed)

When findings are dense (8+ findings or 4+ categories with hits), suggest escalation:

```
Dense findings across multiple categories — consider running /code-review for a deeper pass.
```

## Guidelines

- **One pass, no back-and-forth.** Read the code, report findings, done.
- **Be assertive, not exhaustive.** Flag what stands out. A vibe check is quick, 30 seconds of focused attention, not a thorough audit.
- **Require judgment.** Every finding should need reasoning to identify. If `ruff` or `eslint` could catch it, skip it.
- **Include file:line references.** Every finding points to a specific location.
- **Explain the why.** Don't just name the smell, say what's wrong with the energy. "This wrapper adds a layer of indirection but every caller passes through unchanged" beats "unnecessary abstraction."
- **Respect language idioms.** A Go error check isn't cargo cult. A React `useEffect` cleanup isn't ceremony. Know the difference.
- **No rewrites.** Flag the problem, don't fix it. The developer decides what to do.

## See Also

- `/code-review`: Full structured review when vibe-check suggests escalation
- `/naming`: Deep dive when shallow-naming findings accumulate
- `/testing`: When missing-skepticism reveals untested assumptions
- `/sweep`: Post-op damage check; vibe-check is pre-commit, sweep is post-merge
- `skills/FRAMEWORKS.md`: Full framework index
