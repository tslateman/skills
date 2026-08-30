---
name: testing
description: Design test strategy using Beck's Test Desiderata — which properties matter, which tradeoffs to make. Use when the user asks "how should I test this", "what tests do I need", "review my test strategy", "is this well-tested", or when planning tests for a new feature or refactor.
---

# Test Design as Thinking

## Overview

Test _strategy_, not test generation. Treat test design as an act of specification, articulate the contract, find the boundaries, surface hidden assumptions. Use Beck's Test Desiderata to make testing tradeoffs deliberate instead of accidental.

## Beck's 12 Test Desiderata

Every test balances these properties. No test maximizes all twelve. The skill is knowing which to prioritize.

| Property              | Definition                                | Tension                          |
| --------------------- | ----------------------------------------- | -------------------------------- |
| Isolated              | Same results regardless of run order      | vs. speed (shared setup)         |
| Composable            | Test dimensions of variability separately | vs. writability (more tests)     |
| Deterministic         | Same results if nothing changes           | vs. realism (real services)      |
| Fast                  | Run quickly                               | vs. predictiveness (integration) |
| Writable              | Cheap to write relative to code cost      | vs. thoroughness                 |
| Readable              | Comprehensible, invokes motivation        | vs. conciseness                  |
| Behavioral            | Sensitive to behavior changes             | vs. structure-insensitivity      |
| Structure-insensitive | Unaffected by refactoring                 | vs. behavioral sensitivity       |
| Automated             | No human intervention needed              | vs. exploratory testing          |
| Specific              | Failure cause is obvious                  | vs. breadth of coverage          |
| Predictive            | Passing means production-ready            | vs. speed and isolation          |
| Inspiring             | Passing builds confidence to deploy       | vs. all other properties         |

See `references/desiderata.md` for application guidance.

## Test Design Workflow

### 1. Articulate the Contract

Before writing any test, answer:

- What does this code promise to callers?
- What does it require from its inputs?
- What side effects does it produce?
- What invariants must always hold?

If you can't answer these, the code's contract is unclear. Fix that first.

### 2. Identify Boundaries

Every contract has edges. Test them:

- **Empty/zero/null**, the degenerate case
- **One**, the simplest non-empty case
- **Many**, the normal case
- **Boundary**, max values, off-by-one, type limits
- **Error**, invalid input, unavailable dependencies
- **Concurrent**, multiple callers, race conditions

### 3. Choose the Testing Approach

Match the approach to what you're testing:

**Example-based tests**, specific inputs and expected outputs. Best for known contracts with clear boundaries.

**Property-based tests**, invariants that hold for all inputs. Best for algorithms, parsers, serialization (encode/decode roundtrip), and sorting.

**Integration tests**, multiple components together. Best for verifying wiring, data flow, and contracts between modules.

**Snapshot tests**, output matches recorded baseline. Best for rendering, serialization, and configuration.

### 4. Apply the Testing Trophy

Kent C. Dodds' priority order:

```
         ┌──────┐
         │  E2E │  Few, slow, high confidence
        ┌┴──────┴┐
        │Integra-│  Most tests here
        │  tion  │
       ┌┴────────┴┐
       │   Unit   │  Many, fast, specific
      ┌┴──────────┴┐
      │   Static   │  Types, linters, formatters
      └────────────┘
```

**"The more your tests resemble the way your software is used, the more confidence they can give you."**

### 5. Evaluate Existing Tests

Ask of each test:

- Which Desiderata properties does it maximize?
- Which did it sacrifice? Was that deliberate?
- Does it test behavior or implementation detail?
- If this test fails, will the message tell you why?
- If the implementation changes but behavior doesn't, does this test break? (It shouldn't)

## Test Smells

Three that a different strategy fixes. The rest are somebody else's job.

| Smell           | Symptom                                   | Fix                                    |
| --------------- | ----------------------------------------- | -------------------------------------- |
| Happy path only | No error/boundary cases                   | Add boundary analysis                  |
| Giant arrange   | 30 lines of setup for 1 assertion         | Simplify the interface or use builders |
| Test per method | One test per function, misses integration | Test use cases, not methods            |

An expected value must come from _outside_ the code under test: a known-good
literal, a worked example, the spec. A value computed the way the code computes
it can never disagree with the code — break the code wrong and the assertion
breaks wrong with it. `expect(add(a, b)).toBe(a + b)`, a figure snapshotted the
code's own way, a constant asserted against itself: each passes by construction
and gives zero confidence.

The smells that decide whether a test can fail at all — tautologies, invisible
assertions, implementation coupling, flakes, mock saturation — belong to
`/test-review`. The order tests get written in belongs to `/test-first`. Do not
restate either here.

## Strategy Templates

Three fill-in shapes — pure function, API endpoint, UI component — in
`references/strategy-templates.md`. Any one run needs one of them, so they load
on demand rather than sitting in every invocation.

## Output Format

When designing test strategy:

```markdown
## Test Strategy for [feature/module]

### Contract

[What this code promises and requires]

### Priority Properties

[Which Desiderata properties matter most and why]

### Test Plan

1. [Test case] — [what it verifies] — [approach]
2. [Test case] — [what it verifies] — [approach]

### Tradeoffs Accepted

- [Property sacrificed] because [reason]

### Not Testing

- [What's deliberately excluded and why]
```

## The Confidence Question

After designing the test suite, ask: "If all these tests pass, would you deploy with confidence?" If no, identify what's missing. If yes, stop, more tests beyond confidence are waste.

## See Also

- `/test-first`: This skill chooses which properties matter; test-first fixes the order they get written in
- `/test-review`: Audits whether an existing suite can actually fail
- `/legacy`: When the code has no tests at all, start with characterization
- `/review-decisions`: Reviews assess test coverage alongside code quality
- `references/desiderata.md`: The twelve properties in full
- `references/strategy-templates.md`: Fill-in shapes per test subject
- `skills/FRAMEWORKS.md`: Full framework index
- `RECIPE.md`: Agent recipe for parallel decomposition (2 workers)
