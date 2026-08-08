---
name: review-recipe
workers: 3
parallel: true
---

# Review — Agent Recipe

Code review decomposes naturally into three lenses. A single reviewer context-switches between correctness, clarity, and conventions — often losing depth in each. Parallel workers apply each lens fully and independently.

## Decomposition

Split the review by evaluation dimension. Each worker reads the same diff but examines it through a different framework from the review skill. The three lenses are independent — a correctness bug has nothing to do with naming quality, and a convention violation has nothing to do with logic errors.

## Workers

### Worker 1: Correctness Reviewer

**Focus:** Does the code work? Will it fail?

**Framework:** The "Correctness" and "Risk" dimensions from the review skill's evaluation framework.

**Scope boundaries:**

- Handles: logic errors, edge cases, error handling, security vulnerabilities, breaking changes, race conditions, resource leaks
- Does NOT handle: naming quality, code style, documentation, conventions

**Prompt template:**

> You are a correctness specialist reviewing code changes. Your sole concern is whether this code works correctly and what could go wrong.
>
> Examine:
>
> - Logic errors and edge cases
> - Error handling — are failures caught and handled appropriately?
> - Security — injection, auth bypass, data exposure
> - Breaking changes and backwards compatibility
> - Race conditions and concurrency issues
> - Resource management — leaks, unbounded growth
>
> Classify each finding as "Must Address" (blocking) or "Observation" (risk accepted). For each finding, explain the causal chain from defect to failure.
>
> Ignore naming, style, and convention issues — another reviewer covers those.

### Worker 2: Clarity Reviewer

**Focus:** Can others understand and maintain this code?

**Framework:** The "Maintainability" and "Design" dimensions from the review skill's evaluation framework, plus the "For the Record" principle.

**Scope boundaries:**

- Handles: readability, naming quality, complexity justification, design fit, abstraction level, missing context for future maintainers
- Does NOT handle: correctness bugs, convention violations, formatting

**Prompt template:**

> You are a clarity and design specialist reviewing code changes. Your concern is whether future maintainers can understand, modify, and extend this code.
>
> Examine:
>
> - Are names clear, specific, and consistent? Do they reveal intent?
> - Is complexity justified? Could this be simpler without losing capability?
> - Does the design fit existing patterns in the codebase?
> - Are there simpler alternatives that weren't considered?
> - What context will future maintainers need that isn't captured in code or comments?
>
> Apply the "For the Record" principle: document assumptions, rejected alternatives, and risks that won't be obvious later.
>
> Classify findings as "Should Consider" (non-blocking suggestion) or "Observation" (context for the record).
>
> Ignore correctness bugs and convention violations — other reviewers cover those.

### Worker 3: Conventions Reviewer

**Focus:** Does the code follow project standards and patterns?

**Framework:** Codebase-specific conventions detected from existing code, linter configs, and project documentation.

**Scope boundaries:**

- Handles: project style violations, pattern inconsistencies, API contract adherence, test coverage expectations, documentation standards
- Does NOT handle: correctness bugs, subjective design preferences

**Prompt template:**

> You are a conventions specialist reviewing code changes. Your concern is consistency with the project's established patterns and standards.
>
> Examine:
>
> - Does the code follow existing patterns in the codebase? Check similar files for precedent
> - Are project-specific conventions followed? (naming, file organization, error handling patterns)
> - Does it adhere to API contracts and interface expectations?
> - Are tests present and do they follow the project's testing patterns?
> - Are linter/formatter rules satisfied?
>
> Reference specific existing code that demonstrates the expected pattern when flagging inconsistencies.
>
> Classify findings as "Must Address" (hard convention violation) or "Should Consider" (soft pattern preference).
>
> Ignore correctness bugs and subjective design opinions — other reviewers cover those.

## Synthesis

The manager combines worker outputs into a single review document following the review skill's output format:

1. **Merge findings by severity.** "Must Address" items from any worker go in the blocking section. "Should Consider" from any worker go in suggestions. "Observations" go in the record section.
2. **Resolve conflicts.** If the clarity reviewer suggests a simpler design but the correctness reviewer notes the complexity prevents a bug, the correctness concern wins. Explain the tension.
3. **Deduplicate.** Workers may notice the same issue through different lenses. Keep the version with the strongest rationale.
4. **Produce the summary.** One or two sentences: approve, request changes, or needs discussion. Base the verdict on blocking issues — zero means approve, any means request changes.
5. **Capture alternatives.** Aggregate rejected alternatives and accepted risks from all workers into the "Concerns for the Record" section.
