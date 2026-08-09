---
name: refactor
description: Execute a named restructure with observable behavior held constant, applying Fowler's Refactoring. Use when you name a target ("extract this", "consolidate these three", "split this phase"), when `maintainability` hands off a cure, or when a change needs preparatory restructuring before the feature lands. Works in small verified steps against a green test suite and commits each step. Do NOT use to find problems (that is `maintainability` or `code-review`), to judge a design (that is `ousterhout-software-design`), or to change what the code does.
---

# Refactor

Change the structure, never the behavior. Fowler's discipline: a series of small transformations, each one verified, each one revertible, none of them altering what a caller observes.

## Use this vs. its neighbors

- Find what is wrong and rank it -> `maintainability`.
- Hunt correctness bugs in a diff -> `code-review`.
- Judge module boundaries and interface depth -> `ousterhout-software-design`.
- Judge whether the domain owns its own invariants -> `domain-model`.
- Quick reuse/simplification pass on a just-written diff -> `simplify`.
- Execute a named restructure with behavior held constant -> here.

## The contract

Kent Beck's two hats: **adding function** and **refactoring** are separate hats. Wear one at a time and know which one is on. Adding function never changes existing structure; refactoring never changes behavior. A step that does both is neither, and it is unreviewable.

The test of a refactoring is not the diff size. It is whether any caller can tell. If a public contract, a stored format, an emitted event, or an error type changed, the hat came off.

## Preconditions

Refuse to start without all three. Say which one is missing and stop.

1. **A green, self-checking test suite covering the target.** Run it first and see it pass; a suite you did not watch pass is not a baseline. No coverage means the first job is characterization tests — write them, get them green, then refactor. Never restructure code whose behavior nothing pins down.
2. **A clean working tree**, or unrelated changes committed first. A refactor tangled with a feature cannot be reviewed and cannot be reverted.
3. **A named target.** "Clean this up" is not a target. Either the caller names the move, or `maintainability` hands one over, or you name it explicitly and confirm before touching code.

## Workflow

1. **Establish green.** Run the suite. Record the pass count. That number is the invariant for the rest of the session.
2. **Name the move.** One refactoring from the catalog, with its site. State it before editing: "Extract Function on the tenant-scoping block in `billing.py:140-172`."
3. **Follow the mechanics.** Each refactoring has an ordered procedure — see `references/catalog.md`. The mechanics exist so that every intermediate state compiles and passes. Do not improvise a shortcut through the middle.
4. **Test after every step**, not at the end. The step is the unit of verification.
5. **Commit each green step.** Small commits are what make a bad refactor cheap to undo.
6. **Revert, do not debug.** A refactoring that goes red mid-flight is reverted to the last green commit and retried in smaller steps. Debugging a half-applied restructure costs more than redoing it. Fowler's rule: if it hurts, the steps are too big.
7. **Verify behavior held.** Same pass count, and no assertion edited. Then report: the move, the sites, the commits.

## Choosing the move

| Smell                             | Move                                                                 |
| --------------------------------- | -------------------------------------------------------------------- |
| Duplicated logic (three or more)  | Extract Function, then Pull Up / Move Function to a shared owner     |
| Long parameter list               | Introduce Parameter Object, Preserve Whole Object                    |
| Primitive obsession               | Replace Primitive with Object, Replace Type Code with Subclasses     |
| Shotgun surgery                   | Move Function / Move Field until the change has one home             |
| Divergent change                  | Split Phase, or extract the axis that varies independently           |
| Nested conditionals               | Replace Nested Conditional with Guard Clauses, Decompose Conditional |
| Type-switch repeated across sites | Replace Conditional with Polymorphism                                |
| Flag argument                     | Remove Flag Argument (split into two intention-revealing functions)  |
| Pass-through / delegation layer   | Inline Function, Remove Middle Man                                   |
| Data clump                        | Extract Class, Introduce Parameter Object                            |
| Mixed computation and I/O         | Split Phase, Separate Query from Modifier                            |
| Speculative generality            | Inline Function, Collapse Hierarchy, Remove Dead Code                |

Full mechanics: `references/catalog.md`. Detection is `maintainability`'s job, not this skill's — arrive here with the smell already named.

## Tiebreaks

Where Fowler and Ousterhout disagree, **Ousterhout wins** — same tiebreak as `maintainability`.

- **Never extract to shrink a function.** Line count is not a smell. Extract only when it separates concerns a reader currently has to interleave. A long, deep function beats five shallow ones, and Extract Function is the move most often applied for the wrong reason.
- **An extraction that yields a pass-through is a net loss.** If the new function only forwards, or the new class only delegates, inline it back. Test: does the layer change the abstraction?
- **Rule of Three.** First occurrence, write it. Second, wince and duplicate. Third, consolidate. Consolidating at two guesses the axis of variation and usually guesses wrong.
- **Preparatory refactoring** — "make the change easy, then make the easy change" — is the highest-value use of this skill, but the two land as **separate commits**. The preparatory one must stand alone and pass on its own.
- **Comments**: the `code-comments` rule overrides Fowler. Never add a comment as part of a refactor — not to explain the new shape, not to justify the move. Refactoring deletes comments more often than it touches them: a comment explaining an unclear fragment is a signal to extract and name it, and the name retires the comment. If an extracted name needs a comment to be understood, the name is wrong. Comments already in the code travel with the lines they explain; never strand one by moving its subject out from under it.
- **Guards**: the `no-dead-defensiveness` rule holds. Do not add null checks, `try/except`, or fallback defaults while restructuring; let exceptions raise to a caller that can handle them. A guard is a behavior change wearing a structural disguise, and a swallowed exception makes the refactor unverifiable — the suite goes green on a silent default instead of the real path.

## When not to refactor

- **Code you do not need to modify and do not need to understand.** Ugly and stable is not a defect. Refactoring earns its cost only against a change you are actually about to make.
- **When a rewrite is cheaper.** If the module cannot be brought green in small steps, it is a rewrite behind a preserved interface, not a refactoring. Name it as such.
- **Mid-feature.** Finish the feature, commit, then re-hat.
- **Without the budget for tests.** Refactoring untested code is editing code and hoping. Either write the characterization tests or leave it.

## Gotchas

- **Rewriting instead of refactoring** is the dominant agent failure. The pull is to regenerate the file in the shape you would have written. If the diff is larger than the named move requires, behavior has moved with it. Constrain each edit to the mechanics.
- **Edited assertions are the tell.** If a test had to change to stay green, the refactoring changed behavior. The only legitimate test edits are renames that follow a renamed symbol.
- **Batching.** One refactoring per commit. Three moves in one commit cannot be bisected, reviewed, or partially reverted.
- **Renames go through tooling** (LSP rename, IDE refactor), never `sed`. Text substitution catches strings, comments, and unrelated identifiers.
- **Dynamic call sites survive static search.** Reflection, string-keyed dispatch, serialized class names, and templates will not appear in a rename's results. Grep the bare string before declaring a move complete.
- **Behavior includes performance at the boundaries.** Extracting inside a hot loop, or replacing a lazy path with an eager one, is observable. Check before assuming structure-only.
