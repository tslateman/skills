---
name: slice
description: Turn a spec, plan, or conversation into a graph of tracer-bullet tasks, each declaring what blocks it and how you will know it is done. Covers vertical slicing, sizing tests, verification commands, checkpoints, and the expand-migrate-contract sequence for wide refactors no single slice can land green. Use after a spec exists and before implementation starts, or on "break this down", "what are the tasks", "turn this into tickets". Do not use to decide what to build — that is spec-out — or to execute a named restructure, which is refactor.
argument-hint: "[spec path, issue reference, or nothing to use the conversation]"
---

# Slice — From Spec to Units That Finish

A spec says what to build. It does not say what to build first, or what done
means for any one piece of it. Hand an agent a spec and it builds until it runs
out of context, leaving a half-finished layer nobody can verify. Hand it a slice
and it finishes.

Two properties make a slice finishable: it cuts through every layer so the
result is demonstrable on its own, and it names the evidence that will prove it.
Everything below serves those two.

## Use this vs. its neighbors

- Deciding what to build at all → `spec-out`.
- Exploring options before committing → `brainstorm`.
- Executing one named restructure → `refactor`.
- Retiring code rather than adding it → `deprecate`.
- Turning a finished spec into work that can be picked up → here.

## 1. Slice vertically

Each task cuts a narrow but complete path through every layer — schema, service,
interface, tests — so finishing it produces something demonstrable.

```text
HORIZONTAL (wrong)              VERTICAL (right)
1. All the schema               1. User can create an account
2. All the endpoints            2. User can log in
3. All the UI                   3. User can create a task
4. Wire it together             4. User can see their tasks
```

Horizontal slices finish in the wrong order: nothing is demonstrable until the
last one lands, so every estimate is a guess until the end.

Do any prefactoring first, as its own task. Make the change easy, then make the
easy change.

## 2. Build a graph, not a list

Give every task its **blocking edges**: the tasks that must complete before it
can start. A task with no blockers can start now.

This makes the **frontier** visible — every task whose blockers are done — which
is what lets work be picked up in parallel, or picked up at all after a break.
A flat ordered list hides that; it says what came next for the author, not what
is available to the next person.

On a real tracker use its native blocking links. In local files, name the
blockers in the task itself.

## 3. Size it so it fits

| Size   | Files | Scope                         |
| ------ | ----- | ----------------------------- |
| **XS** | 1     | One function or config change |
| **S**  | 1-2   | One component or endpoint     |
| **M**  | 3-5   | One feature slice             |
| **L**  | 5-8   | Multi-component feature       |
| **XL** | 8+    | Too large — break it down     |

Agents finish S and M reliably. L is a warning; XL is not a size, it is a
decomposition you have not done yet.

Break a task down further when any of these is true:

- It would take more than one focused session.
- Its acceptance criteria will not fit in three bullets.
- It touches two independent subsystems.
- You wrote "and" in the title.

## 4. Say how it will be proven

Acceptance criteria state the behavior. **Verification names the commands**, so
whoever picks the task up does not have to reconstruct how this repo proves
anything:

```markdown
## Task 3: User can create a task

**Delivers:** the end-to-end behavior, from the user's side, not a layer list.

**Blocked by:** Task 1 (schema), Task 2 (auth)

**Acceptance:**

- [ ] Specific, testable condition
- [ ] Specific, testable condition

**Verification:**

- [ ] Tests: <the repo's focused-test command>
- [ ] Build: <the repo's build command>
- [ ] Manual: <what to look at, and what right looks like>

**Size:** M
```

**Leave file paths out of anything that outlives the week.** Paths go stale
faster than the work does, and a wrong path is worse than none. A same-session
checklist can name them; a tracker item should not.

Add a checkpoint every two or three tasks — full suite green, the core flow
working end to end, and a human look before continuing.

## 5. The wide-refactor exception

A **wide refactor** is one mechanical change whose blast radius fans across the
codebase: retype a shared symbol, rename a column. A single edit breaks
thousands of call sites at once, so no vertical slice can land green and the
rule above stops applying.

Sequence it as expand, migrate, contract instead:

```text
EXPAND ─────────────→ MIGRATE ─────────────→ CONTRACT
add the new form      move call sites in     drop the old form once
beside the old        batches sized by       nothing references it
                      blast radius
```

Each migrate batch is its own task blocked by the expand, and CI stays green
between them because the old form still exists. Contract is blocked by every
batch. Where batches genuinely cannot stay green alone, let them share an
integration branch that blocks one final verify task, and promise green only
there. `deprecate` runs the same sequence for removal.

## 6. Check the breakdown before publishing

Show the numbered list — title, blocked by, what it delivers — and ask three
questions: is the granularity right, does each task depend only on what
genuinely gates it, and should anything be merged or split. Iterate until the
answer is yes, then publish in dependency order so blockers exist before the
tasks that reference them.

## Rules

1. **A task nobody can demo is not a slice.** If finishing it changes nothing
   observable, it is a layer, and it belongs inside a slice rather than beside
   one.
2. **Every task declares its blockers, even when the answer is none.** The empty
   declaration is what marks it available.
3. **Acceptance without verification is a wish.** Name the command.

---

Merged from `to-tickets` in
[mattpocock/skills](https://github.com/mattpocock/skills) (blocking edges, the
frontier, expand-migrate-contract) and `planning-and-task-breakdown` in
[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) (sizing
tests, verification commands, checkpoints). Both MIT. They disagree on file
paths; the rule above resolves it by lifespan.
