# Test Desiderata

From Kent Beck's _Test Desiderata_ (2019). Twelve properties
of good tests, treated as sliders — not checkboxes.

## The Core Insight

No test maximizes all twelve properties simultaneously.
Every test is a design decision about which properties to
prioritize for this specific code. Make the tradeoff
deliberate.

## Property 1: Isolated

Tests produce the same results regardless of run order.

**Maximizing:** Each test creates its own state, tears it
down after. No shared mutable state between tests.

**Sacrificing:** Shared database, shared server, test
ordering dependencies. Faster suite but fragile.

**Prioritize when:** Tests run in parallel, CI randomizes
order, failures must be independently reproducible.

## Property 2: Composable

Test dimensions of variability separately, compose for
coverage.

**Maximizing:** Test each axis independently.
3 inputs x 4 outputs = 12 tests that cover everything,
not 12 specific scenarios that leave gaps.

**Sacrificing:** Testing specific end-to-end scenarios only.
Easier to write but combinatorial gaps emerge.

**Prioritize when:** Multiple independent variables interact.

## Property 3: Deterministic

Same results if nothing meaningful changes.

**Maximizing:** No real clocks, no real network, no random
values. Everything controlled.

**Sacrificing:** Real external services for realism.
More predictive but introduces flakiness.

**Prioritize when:** CI must be reliable. Flaky tests erode
team trust in the entire suite.

## Property 4: Fast

Run quickly enough to use during development.

**Maximizing:** Unit tests, in-memory everything, no I/O.
Milliseconds per test.

**Sacrificing:** Real databases, browser rendering, network
calls. Slower but more predictive.

**Prioritize when:** Developer feedback loop. Tests that
take 30 seconds don't get run during development.

## Property 5: Writable

Cheap to write relative to the cost of the code being
tested.

**Maximizing:** Simple assertions, minimal setup, test
utilities and builders.

**Sacrificing:** Thorough property-based testing, complex
integration scenarios. More coverage but higher cost.

**Prioritize when:** Codebase moves fast, tests must keep
up. Low-risk code doesn't need elaborate tests.

## Property 6: Readable

Comprehensible to someone seeing the test for the first
time. Invokes motivation — the reader understands _why_
this test exists.

**Maximizing:** Clear test names, visible arrange/act/assert,
minimal abstraction in tests.

**Sacrificing:** DRY test code (shared helpers that hide
setup). Less duplication but harder to follow.

**Prioritize when:** Team has mixed experience levels.
Tests serve as documentation.

## Property 7: Behavioral

Sensitive to changes in the system's behavior.

**Maximizing:** Test what the code does (outputs, side
effects), not how it does it (internal calls, structure).

**Sacrificing:** Testing internal implementation details
gives faster feedback but breaks on refactoring.

**Prioritize when:** Code will be refactored. Behavioral
tests survive redesigns.

## Property 8: Structure-insensitive

Unaffected by refactoring that preserves behavior.

**Maximizing:** Test through public interfaces only.
No mocking internal collaborators.

**Sacrificing:** Mocking internals gives isolation but
couples tests to implementation.

**Prioritize when:** Investing in long-lived code that
will evolve. Tests should not fight refactoring.

**Note:** Behavioral and structure-insensitive are natural
allies. Both push toward testing observable behavior
through public interfaces.

## Property 9: Automated

No human intervention to run or evaluate.

**Maximizing:** Everything in CI. Clear pass/fail.
No "look at this screenshot and decide."

**Sacrificing:** Exploratory testing, visual review.
Humans catch things automation misses.

**Prioritize when:** Always. The baseline. Manual testing
doesn't scale and isn't repeatable.

## Property 10: Specific

When a test fails, the cause is obvious from the failure
message alone.

**Maximizing:** One assertion per behavior. Descriptive
test names. Error messages that include actual vs expected.

**Sacrificing:** Broad integration tests that say "something
broke" without pointing to what.

**Prioritize when:** CI failures must be diagnosable without
running the test locally.

## Property 11: Predictive

Passing means the system works in production.

**Maximizing:** Test in production-like environments. Real
databases, real services, real browsers.

**Sacrificing:** Fast, isolated unit tests that pass even
when production would fail.

**Prioritize when:** Deployment confidence matters more than
speed. Payment processing, data integrity, security.

## Property 12: Inspiring

Passing the test suite builds confidence to deploy.

**Maximizing:** The suite covers what you worry about. When
it's green, you feel safe.

**Sacrificing:** A green suite that doesn't reduce anxiety
is failing this property regardless of coverage numbers.

**Prioritize when:** Always. This is the purpose of testing.
If green doesn't mean "ship it", the suite needs work.

## Common Tradeoff Profiles

**Unit tests:**
Maximize: fast, isolated, specific, writable
Sacrifice: predictive, inspiring (alone)

**Integration tests:**
Maximize: predictive, behavioral, inspiring
Sacrifice: fast, specific, isolated

**E2E tests:**
Maximize: predictive, inspiring
Sacrifice: fast, specific, deterministic, writable

**Property-based tests:**
Maximize: composable, behavioral, structure-insensitive
Sacrifice: readable, specific (on failure)

## The Decision

For each piece of code, ask:

1. Which properties matter most for _this_ code?
2. Which testing approach maximizes those properties?
3. What am I deliberately sacrificing, and why?

Document the tradeoff. A test suite with deliberate
tradeoffs beats one with accidental gaps.
