---
name: legacy
description: Get code with no tests under a harness so it can be changed safely, applying Feathers' Working Effectively with Legacy Code. Use when a change is needed in untested code, when refactor refuses for want of a green baseline, when a class cannot be instantiated in a test, or when adding behavior to code you dare not touch. Covers characterization tests, seams, dependency-breaking, and sprout/wrap. Do NOT use when a green suite already covers the target (that is refactor or tidy) or to drive new behavior from a failing test (that is test-first).
---

# Legacy

Answers one question: how do I get this under test without changing it first? Feathers' definition is operational and has nothing to do with age — **legacy code is code without tests.** Code without tests cannot be changed safely, and code that cannot be changed safely is where every risky change ends up.

This skill produces a green baseline over behavior that nothing currently pins down. It never improves that behavior; the improvement comes after, through `refactor` or `tidy`.

## Use this vs. its neighbors

- A green suite already covers the target -> `refactor`, or `tidy` for smaller moves.
- Drive new behavior from a failing test -> `test-first`.
- Decide which test properties the eventual suite needs -> `testing`.
- Judge how the code will age once it is safe to touch -> `maintainability`.
- Get untested code under a harness so any of the above becomes possible -> here.

## The dilemma

To change code safely you need tests. To put tests around it you usually have to change it. That circle is the whole problem, and the way out is to make the smallest, most conservative change that creates a place to test from — accepting a worse design temporarily to get the safety that lets you fix the design properly.

The order is fixed: **cover, then change.** Never improve on the way in.

## Characterization tests

A characterization test records what the code **does**, not what it should do. It is a description, not a specification, and it preserves bugs deliberately — the bug may be load-bearing, and you are not fixing it yet.

The mechanical procedure, which requires no understanding of the code:

1. Write a test that calls the code with a concrete input and asserts something you know is wrong — an obviously bogus expected value.
2. Run it. The failure message reports the actual value.
3. Change the expectation to the actual value. The test now passes.
4. Repeat for the inputs that matter: each branch, each boundary, each error path.

You now have a green suite over the current behavior without having read the implementation closely. Where the recorded behavior is obviously wrong, note it as a finding and leave it green. Fixing it is a separate, later, deliberate change with its own test.

Name these tests for what they pin, not for correctness: `records_zero_balance_returns_none`, never `test_handles_zero_balance_correctly`.

## Seams

A **seam** is a place where behavior can be altered without editing in that place. Every seam has an **enabling point** — where the choice of behavior is made. No seam, no test harness.

| Seam type         | Alter behavior at                                               | Enabling point                        |
| ----------------- | --------------------------------------------------------------- | ------------------------------------- |
| **Object**        | Override a method in a subclass or substitute an implementation | Where the instance is chosen          |
| **Link**          | Swap what the build or runtime resolves the name to             | Build config, path, module resolution |
| **Preprocessing** | Replace text before compilation                                 | Macro or include configuration        |

Object seams are the ones to reach for. Link and preprocessing seams work when you truly cannot alter the source, and they are harder to see from the code, which makes them harder for the next reader.

## Adding behavior without touching the mass

When the surrounding code cannot be brought under test cheaply, do not change it. Add beside it.

- **Sprout method** — write the new behavior as a new, fully tested method. Call it from one line inside the untested code.
- **Sprout class** — same, when the new behavior needs its own state, or when the host class cannot be instantiated in a test at all.
- **Wrap method** — rename the original, then write a new method with the original name that calls both the renamed original and your new behavior. Callers are untouched.
- **Wrap class** — a new class with the same interface, delegating to the original and adding behavior around it.

The cost is honest and worth naming: sprouting leaves the untested mass untested and adds a seam that looks arbitrary until someone reads why. Take it when covering the host is genuinely out of budget, and say so.

## When the class will not go in a harness

Four common blockers and the standard moves:

- **Cannot construct the object.** Parameterize Constructor, Extract Interface on the hard collaborator, Introduce Instance Delegator.
- **Constructor does real work** (opens sockets, reads config, hits a database). Extract and Override Factory Method, or Extract and Override Call.
- **Hidden dependency reached for inside a method** (global, singleton, static). Parameterize Method, Expose Static Method, or Introduce Instance Delegator.
- **A method is too tangled to call in isolation.** Break Out Method Object: move the method to a new class with its locals as fields, then test that class.

Subclass and Override Method is the blunt instrument that works when nothing else does — subclass the target in the test and stub the one method blocking you. It is ugly, it is temporary, and it beats not testing.

## Understanding it first

When the code is opaque, two cheap tools before any edit:

- **Scratch refactoring**: restructure freely to understand it, learn the shape, then **throw it away uncommitted**. The value is the reading, not the diff.
- **Effect sketching**: from the line you intend to change, trace outward to everything that could observe the change — return values, fields, globals, I/O. Where many effects funnel through few places, those pinch points are where the characterization tests go.

## Workflow

1. **Name the change** you actually need to make. Coverage is not the goal; a safe change is.
2. **Sketch the effects** of that change and find the pinch point.
3. **Break the minimum dependencies** to reach a harness. Conservative moves only, applied by hand or by tooling, never by regeneration.
4. **Characterize** the current behavior at the pinch point until green.
5. **Commit the tests alone.** They describe today's behavior and are valuable independent of the change.
6. **Now make the change** — hand off to `test-first` for new behavior, `refactor` or `tidy` for structure.

## Gotchas

- **Fixing the bug while characterizing** is the dominant agent failure. The test run reports `-0.5` where the docstring promises `0`, and the instinct is to write `assert result == 0` and repair the code. That is a silent behavior change under cover of adding tests. Record `-0.5`, note the discrepancy, move on.
- **Testing the docstring instead of the code.** The name, the comment, and the ticket all describe intent. Characterization records behavior. Where they disagree, the behavior is what shipped and what callers depend on.
- **Mocking everything to force a harness.** A test where every collaborator is a mock verifies the mocks and pins nothing. Prefer a real object; if that is impossible, the seam is in the wrong place.
- **Rewriting instead of sprouting.** Regenerating the file in a better shape discards the behavior you cannot see. There is no baseline to catch what it lost.
- **Deleting "dead" code without evidence.** Reflection, string dispatch, serialized names, and templates all survive static search. Grep the bare string before concluding nothing calls it.
- **Coverage as the goal.** Characterizing an entire legacy system before changing anything spends the budget and delivers nothing. Cover the pinch point for the change at hand.
