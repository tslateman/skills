---
name: testing-recipe
workers: 2
parallel: true
---

# Testing — Agent Recipe

Test work splits between strategy and implementation. Strategy decides what to test and why — articulating contracts, choosing desiderata tradeoffs, identifying boundaries. Implementation writes the actual tests. Separating these prevents the common failure of jumping straight to code and missing coverage gaps, or over-designing a strategy that never gets implemented.

## Decomposition

Split testing by phase. Worker 1 designs the test strategy: what to test, which desiderata to prioritize, what boundaries matter. Worker 2 implements the tests following that strategy. Strategy informs implementation, so Worker 1 runs first — but the manager can run them in parallel when Worker 2 has enough context to start on obvious test cases while Worker 1 finalizes the strategy.

## Workers

### Worker 1: Test Strategist

**Focus:** What should we test? Which properties matter? What tradeoffs are we making?

**Framework:** Beck's 12 Test Desiderata, the "Test Design Workflow" (Articulate the Contract, Identify Boundaries, Choose the Testing Approach), and the Testing Trophy.

**Scope boundaries:**

- Handles: contract articulation, boundary identification, desiderata prioritization, testing approach selection (example-based, property-based, integration, snapshot), test smell detection in existing tests, coverage gap analysis
- Does NOT handle: writing test code, running tests, fixing test failures

**Prompt template:**

> You are a test strategy specialist. Design the testing approach for the given code using Beck's Test Desiderata as your framework.
>
> Follow this workflow:
>
> 1. **Articulate the contract** — What does this code promise to callers? What does it require? What side effects does it produce? What invariants must hold?
> 2. **Identify boundaries** — Empty/zero/null, one, many, boundary values, error cases, concurrency
> 3. **Choose desiderata priorities** — Which of the 12 properties matter most for this code? Which are we deliberately sacrificing? Make the tradeoff explicit
> 4. **Select testing approach** — Example-based, property-based, integration, or snapshot? Match approach to what we're testing
> 5. **Apply the Testing Trophy** — Where on the trophy (static, unit, integration, E2E) should most tests live?
>
> If existing tests are present, evaluate them: which desiderata do they maximize? Which do they sacrifice? Are there test smells?
>
> Deliver: contract definition, test plan with specific cases, desiderata tradeoffs accepted, and what we're deliberately not testing.

### Worker 2: Test Implementer

**Focus:** Write the tests. Make them pass. Ensure they follow the strategy.

**Framework:** The "Strategy Templates" from the testing skill (pure function, API endpoint, UI component) and test quality standards.

**Scope boundaries:**

- Handles: writing test code, choosing test framework patterns, creating fixtures and helpers, running tests, fixing test failures, ensuring tests are isolated and deterministic
- Does NOT handle: deciding what to test (follows Worker 1's strategy), choosing desiderata tradeoffs

**Prompt template:**

> You are a test implementation specialist. Write tests following the provided test strategy.
>
> For each test case in the strategy:
>
> 1. **Write the test** using the project's existing test framework and patterns
> 2. **Follow the strategy's desiderata priorities** — if the strategy says "prioritize isolation over speed," use mocks; if "prioritize predictiveness over isolation," use real dependencies
> 3. **Apply the appropriate template** — pure function, API endpoint, or UI component
> 4. **Run the tests** and verify they pass
> 5. **Check test quality** — Does each test fail for the right reason? Is the failure message specific? Would a refactor break tests that shouldn't break?
>
> Match existing test conventions in the codebase: file naming, directory structure, assertion library, setup/teardown patterns.
>
> Flag any strategy gaps discovered during implementation — cases the strategy missed that became obvious while writing code.

## Synthesis

The manager coordinates strategy and implementation:

1. **Strategy first.** Worker 1 delivers the test strategy. The manager reviews it for completeness before passing to Worker 2.
2. **Implementation follows strategy.** Worker 2 implements tests according to Worker 1's plan. Deviations are flagged, not silently made.
3. **Feedback loop.** If Worker 2 discovers gaps (boundary cases the strategy missed, untestable contracts), the manager routes these back to Worker 1 for strategy revision.
4. **Final check.** Ask the confidence question: "If all these tests pass, would you deploy with confidence?" If no, identify what's missing. If yes, stop.
5. **Produce the output.** Combined test strategy document (from Worker 1) and implemented tests (from Worker 2) with any tradeoffs accepted noted.
