---
name: typescript-review
description: >
  Review TypeScript code for agent-typical anti-patterns: as-any and
  double casts to silence tsc, ts-ignore without reason, non-null
  assertions, empty catch blocks, floating promises, untyped JSON at
  boundaries, eslint-disable suppression. Runs tsc and typescript-eslint
  with a targeted rule set, then judges each trigger with a type-design
  lens. Use when: reviewing agent-written TypeScript, before committing
  TS changes, or on "typescript review", "ts review", "review this
  typescript", "check for any abuse". For generic bug hunts use
  /code-review; for generic judgment use /vibe-check.
argument-hint: "[path or package to review, defaults to working-tree changes]"
---

# TypeScript Review — Local-Fix Debt Audit

TypeScript's type system is opt-out, so the agent-typical minimal edit
is an escape hatch: `as any` where the types disagree, `!` where null
might flow, `@ts-ignore` where neither works. Each edit satisfies tsc
by telling it to stop looking; the runtime error the type was guarding
against still ships. This review hunts that debt class specifically.

## Context

Changed files:
!`git diff --name-only HEAD 2>/dev/null | grep -E '\.(ts|tsx)$' || echo "(not a git repo or no changed .ts/.tsx files — review the given path instead)"`

## Process

### Step 1: Scope

Review `$ARGUMENTS` if given; otherwise the changed `.ts`/`.tsx` files
above; otherwise ask which package. Read the scoped files fully before
judging — every finding needs the surrounding type flow, not just the
line.

### Step 2: Mechanical Pass

```bash
npx tsc --noEmit
npx eslint . --rule '{"@typescript-eslint/no-explicit-any": "warn",
  "@typescript-eslint/no-non-null-assertion": "warn",
  "@typescript-eslint/no-floating-promises": "warn",
  "@typescript-eslint/no-misused-promises": "warn",
  "@typescript-eslint/ban-ts-comment": "warn"}'
```

If the project has its own eslint config with typescript-eslint, run
that instead and say so. Check `tsconfig.json` first: if `strict` is
off (or `strictNullChecks`/`noImplicitAny` disabled), report that
before anything else — every finding below is masked by it.

Then grep the scoped files for triggers the tooling can't judge:

| Trigger                                           | Suspicion                                                                           |
| ------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `as any` / `as unknown as`                        | Type disagreement silenced — what does the real type say?                           |
| `@ts-ignore` / `@ts-expect-error` without comment | Who silenced tsc, and is the reason written down?                                   |
| `!` non-null assertion                            | Proven non-null, or a strictNullChecks silencer?                                    |
| `catch {}` / `catch (e) {}` empty or log-only     | Error swallowing — can the caller tell this failed?                                 |
| `?.` chains ending in `?? default`                | Legitimate optional, or undefined smeared past its origin?                          |
| `JSON.parse(` / `await res.json()` unvalidated    | Untyped data entering as a trusted type — wants a schema (zod) or type guard        |
| `e.message.includes(`                             | Error control flow by string match — wants error subclasses or discriminated unions |
| `eslint-disable`                                  | Same question as ts-ignore                                                          |
| `Promise` without `await`/`void`/`.catch`         | Floating promise — rejection disappears                                             |

### Step 3: Judgment Pass

For each trigger hit, decide which of three buckets it belongs in —
this is the review's actual work:

1. **Fine** — idiomatic, or the pragmatic choice is documented.
   `@ts-expect-error` with a reason on a known library gap is not a
   finding; `!` right after an explicit check the narrower missed is
   defensible.
2. **Mechanical fix** — safe local rewrite: replace the cast with the
   actual type or a type guard, `!` with a narrowing check, add the
   missing `await`, rethrow or surface the caught error.
3. **Type restructure** — the escape hatch exists because the types
   fight the data flow: stringly-typed unions (wants discriminated
   unions), unvalidated boundaries (wants zod or guards at the edge,
   trusted types inside), optionality flowing through every layer
   (wants narrowing at the source). Name the restructure and its blast
   radius. Do not apply it without asking — this bucket is why the
   review exists.

A repeated trigger is one finding, not many: five `as any` on the same
API response point at one unvalidated boundary.

### Step 4: Report

Findings ordered by severity, each with `file:line`, the bucket, why it
matters in one sentence, and the suggested fix. Then a one-paragraph
verdict: do the types describe the data, or describe what tsc was told
to accept? End with the counts: N fine / N mechanical / N restructure.

If the user asks you to apply fixes, apply bucket 2 directly and run
tsc, eslint, and the test suite after; bucket 3 gets a plan first.

## Rules

- Never suggest `as any`, `!`, `@ts-ignore`, or `eslint-disable` as a
  fix.
- tsc passing is the floor, not the verdict — a cast makes tsc pass by
  making it blind.
- Judge casts by what the value actually is at runtime, not by what
  makes the assignment typecheck.
