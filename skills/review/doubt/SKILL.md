---
name: doubt
description: Materialize a fresh-context adversarial reviewer for a decision that has not landed yet — biased to disprove, and deliberately not told what you concluded. Use when correctness beats speed, in unfamiliar code, before an irreversible action (deploy, migration, public API change), or on "am I sure about this", "poke holes in this", "doubt this". Do not use on a finished artifact — that is a review skill — or on mechanical edits where the correctness is obvious.
argument-hint: "[the decision or artifact to doubt]"
---

# Doubt — Adversarial Review While It Is Still Cheap

A confident answer is not a correct one. A long session accumulates context that
quietly promotes assumptions into facts, and the agent that formed the
assumption is the worst possible auditor of it. By the time the artifact is
finished, the cost of being wrong has already been paid.

Every other judge in this repo runs afterward. This one runs mid-flight, while
course-correcting is still free.

## Use this vs. its neighbors

- A finished diff, and you want findings → `code-review`, or the language
  `*-review` for one debt class.
- Whether the change is safe outside the diff → `blast-radius`.
- Whether the whole thing holds together → `vibe-check`.
- A decision that has not landed, where being wrong is expensive → here.

## What counts as non-trivial

Doubt every keystroke and you ship nothing. Apply this only when at least one is
true:

- It introduces or changes branching logic.
- It crosses a module or service boundary.
- It asserts something the compiler cannot check: thread safety, idempotence,
  ordering, an invariant.
- Its correctness depends on context the next reader cannot see.
- Its blast radius is irreversible.

Skip it for renames, formatting, file moves, one-line changes with obvious
correctness, and any time the user has asked for speed over verification.

## The cycle

### 1. Claim

Name the decision in two or three lines, plus why being wrong would hurt.

```
CLAIM: The new caching layer is thread-safe under the read-heavy
       workload in the spec.
COSTS: A race here corrupts user data and survives QA.
```

If the claim will not compress to that, you have a vibe rather than a decision.
Surface it before scrutinizing it.

### 2. Extract

A fresh reviewer needs the **artifact** and the **contract**, never the journey.

- Code: the diff or the function, not the file.
- Decision: the proposal in three to five sentences plus the constraints it must
  satisfy.
- Assertion: the claim plus whatever evidence supposedly supports it.

Strip your reasoning out. Hand over conclusions and you get back validation of
your conclusions. If the unit is too large to hold in one read, decompose before
continuing.

### 3. Doubt

**Pass the artifact and the contract. Never pass the claim.** This is the whole
mechanism. A reviewer told what you concluded will grade your conclusion; a
reviewer told only what the thing must do will test whether it does.

Framing decides the answer, so the prompt is adversarial:

```
Adversarial review. Find what is wrong with this artifact. Assume the
author is overconfident. Look for unstated assumptions, unhandled edge
cases, hidden coupling or shared state, ways the contract could be
violated, conventions this breaks, and failure modes under unexpected
input.

Do NOT validate. Do NOT summarize. Report issues, or state plainly that
you found none after thorough examination.

ARTIFACT: <paste>
CONTRACT: <paste>
```

A reviewer on the same model shares blind spots with the author. Offer a
second opinion from a different model when the stakes justify it, and let the
user decide rather than deciding for them.

### 4. Reconcile

The reviewer's output is data, not a verdict. Re-read the artifact against each
finding — rubber-stamping the reviewer fails the same way ignoring it does.
Classify each finding, first match winning:

| Class                | Means                                                | Do                                              |
| -------------------- | ---------------------------------------------------- | ----------------------------------------------- |
| **Contract misread** | Flagged because your contract was unclear or partial | Fix the contract, re-classify next cycle        |
| **Valid**            | Real issue needing a change                          | Change it, loop                                 |
| **Trade-off**        | Real, but fixing costs more than accepting           | Document it where the user will see it          |
| **Noise**            | Correct under context the reviewer lacked            | Ask whether the contract should have carried it |

A fresh reviewer is often wrong precisely because it is fresh. Freshness earns
it a hearing, not deference.

### 5. Stop

Stop when the next cycle returns only trivial or already-considered findings,
after three cycles, or when the user says ship it.

Three cycles still surfacing substantive issues is information about the
artifact, not a reason to grind a fourth. Surface it. If three feels obviously
insufficient because the artifact is large, the artifact is too large — return
to step 2 and decompose. Do not lift the bound.

---

Adapted from `doubt-driven-development` in
[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) (MIT).
Compressed to the cycle and the withheld-claim rule; the persona and
orchestration plumbing is upstream-specific and dropped.
