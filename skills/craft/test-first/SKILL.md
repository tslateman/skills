---
name: test-first
description: "Drive code from a failing test, applying Beck's Test-Driven Development by Example. Use when starting new behavior (\"TDD this\", \"write it test-first\", \"red green refactor\"), when fixing a bug (reproduce before repair), or to audit whether existing tests were ever red. Answers one question, forward or backward: did the test fail first, and for the right reason? Do NOT use to choose which properties a suite needs (that is testing), to audit a whole suite for tests that cannot fail (that is test-review), or to get untested legacy code under test (that is legacy)."
---

# Test First

Answers one question: did the test fail first, and for the right reason? A test written after the code it checks is shaped by that code — it encodes the implementation's behavior, bugs included, as the specification. Only a test that has been observed to fail has demonstrated it can fail.

Two modes. **Drive**: write the failing test, then the code. **Audit**: take a diff whose tests and implementation arrived together and ask whether any of those tests could ever have been red.

## Use this vs. its neighbors

- Choose which test properties matter and what they cost -> `testing`.
- Audit a whole suite for tests that cannot fail -> `test-review`.
- Get code with no tests at all under a harness -> `legacy`.
- Restructure with the suite already green -> `refactor`, or `tidy` for smaller moves.
- Drive new behavior from a failing test, or check that one did fail -> here.

## The loop

**Red.** Write one test for behavior that does not exist. Run it. Watch it fail.

**Green.** Write the least code that passes. Not the right code — the passing code. Beck's three routes, in order of increasing cost:

1. **Fake it.** Return the constant the test expects. Legitimate, and the fastest way to prove the test is wired up.
2. **Obvious implementation.** When the real code is a few lines and you are sure, type it.
3. **Triangulation.** When you cannot see the general shape, add a second test with different data. Two examples force the generalization the first one let you fake.

**Refactor.** Now make it right. This is the step that gets dropped, and dropping it is what turns TDD into a pile of green tests over bad structure. Hand off: `tidy` for a small cleanup, `refactor` for a named move.

Then the next test. One at a time.

## Red means red

A test that fails is not automatically red. Read the failure and confirm it is the failure you predicted:

- **Right reason**: the assertion fired, and the message names the gap you intended.
- **Wrong reason**: import error, syntax error, typo in a fixture, connection refused, wrong test collected. Fix the harness and get to a real red before writing any implementation.

State the expected failure before running. If the observed failure differs from the predicted one, something other than the missing behavior is broken.

## Step size

Small steps when the ground is unfamiliar; larger steps when you are confident. Beck's rule is that step size is a dial, not a virtue — and the direction to turn it is set by feedback: after a surprise, make the steps smaller until the surprises stop.

Keep a **test list**. Before starting, write the cases you know you will need. Add to it whenever a new one occurs to you mid-loop, and never chase it immediately. Finish the current cycle, then pick the next item. The list is what keeps one-test-at-a-time from losing the thread.

## Bugs

A bug means a test was missing. The sequence does not change:

1. Write the test that reproduces it. It goes red for the right reason — the reported symptom, not a proxy for it.
2. Fix it. The test goes green.
3. Keep the test. It is now a regression test, and it is the only proof the fix works.

Never repair first and add the test afterward. A test written against a fixed implementation has never seen the bug.

## Audit mode

Given a diff where tests and implementation landed together, the question is retroactive: could this test ever have been red? Check each test by construction, not by reading it:

- **Revert the implementation** (or mutate one branch, one operator, one constant) and run the test. If it still passes, it never tested that code.
- **Assertion strength**: does it assert the value, or that the call returned without raising? `assert result` passes on any truthy value.
- **Shape match**: does the test mirror the implementation's structure, branch for branch? That is a test written by reading the code, and it will follow the code's bugs.
- **Mock saturation**: if every collaborator is mocked, the test verifies the mocks. See `test-review`.

Report per test: could-fail, cannot-fail, or unproven. A suite where nothing fails under mutation is decoration.

## Tiebreaks

- **Comments**: the `code-comments` rule holds here as everywhere. A test name carries the intent; never add a comment explaining what a test covers. If the name cannot carry it, the test is doing too much.
- **Guards**: the `no-dead-defensiveness` rule holds. Do not write a test for a state the contract rules out, and do not add a guard to make a test pass — redefine the contract so the state cannot occur.
- **Assertions are never edited to reach green.** Changing the expectation to match the output is the inverse of this skill. If the expectation was wrong, say so out loud and rewrite the test deliberately, red first.

## Gotchas

- **Writing the whole test file up front** is not this skill. That is specify-then-implement, and it loses the feedback that makes step size self-correcting. One test, one cycle.
- **Reaching green by weakening the test** — relaxing an assertion, widening a tolerance, catching the exception the test was meant to provoke. The tell is a test edit in the same commit as the fix.
- **Skipping refactor** leaves the fake-it constant in place, or the duplication triangulation created. Green is the midpoint of the cycle, not the end.
- **Retrofitted tests presented as TDD.** An agent asked to "TDD this" will often write the implementation, then the tests, then report red-green-refactor. The artifact looks identical. Only the run order distinguishes them, so run the test before the implementation exists and say what it printed.
- **Untestable design is the message, not the obstacle.** When a test is hard to write because the unit cannot be constructed without a database, the design is telling you where the seam belongs. Take it to `domain-model` rather than mocking around it.
