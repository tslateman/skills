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

| Smell                  | Symptom                                   | Fix                                    |
| ---------------------- | ----------------------------------------- | -------------------------------------- |
| Testing implementation | Breaks on refactor, behavior unchanged    | Test outputs, not internals            |
| Tautological test      | Repeats production logic in assertions    | Test observable behavior               |
| Happy path only        | No error/boundary cases                   | Add boundary analysis                  |
| Flaky                  | Passes sometimes, fails sometimes         | Fix nondeterminism or mark explicitly  |
| Giant arrange          | 30 lines of setup for 1 assertion         | Simplify the interface or use builders |
| Invisible assertion    | `expect(result).toBeTruthy()`             | Assert specific values                 |
| Test per method        | One test per function, misses integration | Test use cases, not methods            |

## Red-Green Discipline

Two failure modes when building test-first. Adapted from mattpocock/skills `tdd` (MIT).

**Horizontal slicing.** Writing all the tests, then all the implementation, treats RED as "write every test" and GREEN as "write every impl". It produces crap tests: authored in bulk against _imagined_ behavior, they assert the shape of things (signatures, data structures) rather than user-facing behavior, and they go insensitive to real change. Slice vertically instead, one tracer bullet at a time: one test, then the minimal code to pass it, then the next test informed by what that one taught you. Because you just wrote the code, you know exactly what behavior matters and how to verify it.

**Tautological tests.** A test whose expected value is computed the way the code computes it can never disagree with the code: break the code wrong and the assertion breaks wrong with it. `expect(add(a, b)).toBe(a + b)`, a figure hand-snapshotted the code's own way, a constant asserted against itself, all pass by construction and give zero confidence. The expected value must come from an _independent source of truth_: a known-good literal, a worked example, the spec.

## Strategy Templates

### For a pure function:

```markdown
## Contract

[function name]: [input types] → [output type]

- Promises: [what it guarantees]
- Requires: [what inputs must satisfy]

## Test Cases

- [ ] Empty/zero input
- [ ] Single valid input
- [ ] Multiple valid inputs
- [ ] Boundary values
- [ ] Invalid inputs (error cases)
- [ ] Properties that hold for all inputs
```

### For an API endpoint:

```markdown
## Contract

[METHOD /path]: [request] → [response]

- Auth: [required/optional/none]
- Idempotent: [yes/no]

## Test Cases

- [ ] Happy path (valid request → expected response)
- [ ] Validation failures (400)
- [ ] Auth failures (401/403)
- [ ] Not found (404)
- [ ] Concurrent requests
- [ ] Rate limiting
```

### For a UI component:

```markdown
## Contract

[Component]: [props] → [rendered output + interactions]

## Test Cases

- [ ] Renders with required props
- [ ] Renders with all optional props
- [ ] User interactions trigger callbacks
- [ ] Loading/error/empty states
- [ ] Accessibility (keyboard nav, screen reader)
```

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

- `/review-decisions`: Reviews assess test coverage alongside code quality
- `skills/FRAMEWORKS.md`: Full framework index
- `RECIPE.md`: Agent recipe for parallel decomposition (2 workers)
