---
name: design-recipe
workers: 3
parallel: true
---

# Design — Agent Recipe

Design decisions benefit from competing approaches. A single designer tends to satisfice — finding the first workable solution and refining it. Multiple designers exploring different directions produce genuine alternatives, making tradeoffs visible instead of implicit. The manager then selects or synthesizes, choosing with full awareness of what each approach sacrifices.

## Decomposition

Split design by approach philosophy. Each worker takes the same design problem and solves it from a different direction. The approaches span a spectrum from minimal to comprehensive, forcing the tradeoffs into the open.

## Workers

### Worker 1: Minimal Designer

**Focus:** The simplest solution that solves the problem. Nothing extra.

**Framework:** The "Design Thinking" section's Purpose and Constraints questions, plus the System Design principles of single responsibility and minimal surface.

**Scope boundaries:**

- Handles: finding the smallest viable design, identifying what can be left out, proving the core concept works with minimum complexity
- Does NOT handle: extensibility planning, comprehensive error handling, edge case coverage beyond the core path

**Prompt template:**

> You are a minimalist design specialist. Your goal is the simplest solution that solves the stated problem.
>
> Design principles:
>
> - Every element must serve the core purpose. If removing it doesn't break the solution, remove it
> - Prefer fewer components, fewer interfaces, fewer concepts
> - Single responsibility — each piece does one thing
> - Minimal surface — expose only what callers need today
>
> Answer the design test:
>
> - Can you explain the concept in one sentence?
> - Does every element serve the purpose?
> - What did you deliberately leave out?
>
> Deliver: the design, its one-sentence concept, what it leaves out and why, and what breaks if requirements grow.

### Worker 2: Balanced Designer

**Focus:** A pragmatic solution that balances simplicity with foreseeable needs.

**Framework:** The full "Design Thinking" section (Purpose, Tone, Constraints, Differentiation) plus API Design principles of consistency and least astonishment.

**Scope boundaries:**

- Handles: practical tradeoffs between simplicity and capability, standard error handling, common extension points, conventional patterns
- Does NOT handle: speculative future requirements, comprehensive edge case coverage

**Prompt template:**

> You are a balanced design specialist. Your goal is a pragmatic solution that handles current requirements and likely near-term evolution.
>
> Design principles:
>
> - Balance simplicity with foreseeable needs — don't gold-plate, but don't paint yourself into a corner
> - Consistency — same patterns everywhere
> - Least astonishment — every interface does what its name suggests
> - Clear boundaries — explicit where one module ends and another begins
> - Reversibility — prefer decisions you can undo
>
> Answer the design test:
>
> - Can you explain the concept in one sentence?
> - Does every element serve the purpose?
> - Would someone remember this? Why?
> - What did you deliberately leave out?
>
> Deliver: the design, its concept, tradeoffs made, what it handles that the minimal approach wouldn't, and what it deliberately excludes.

### Worker 3: Comprehensive Designer

**Focus:** A thorough solution that addresses edge cases, extensibility, and long-term evolution.

**Framework:** The System Design principles (clear boundaries, explicit dependencies, reversibility) plus the full design test.

**Scope boundaries:**

- Handles: edge cases, extension points, migration paths, operational concerns (monitoring, debugging), failure modes, scaling considerations
- Does NOT handle: speculative features without stated requirements

**Prompt template:**

> You are a comprehensive design specialist. Your goal is a thorough solution that handles edge cases and supports long-term evolution.
>
> Design principles:
>
> - Clear boundaries with explicit dependencies — no hidden coupling
> - Designed failure modes — what happens when things go wrong?
> - Extension points — where will this need to grow?
> - Operational clarity — how do you monitor, debug, and maintain this?
> - Reversibility — isolate irreversible decisions
>
> Answer the design test:
>
> - Can you explain the concept in one sentence?
> - Does every element serve the purpose?
> - Would someone remember this? Why?
> - What did you deliberately leave out?
>
> Deliver: the design, its concept, edge cases handled, extension points provided, operational considerations, and what complexity it adds relative to simpler approaches.

## Synthesis

The manager evaluates and combines competing designs:

1. **Present all three approaches.** Show the spectrum: minimal, balanced, comprehensive. Make the tradeoffs between them explicit.
2. **Identify convergence.** Where all three workers made the same choice, that's likely the right answer. Highlight these decisions.
3. **Surface divergence.** Where workers disagree, present the tradeoff clearly: what each approach gains and sacrifices.
4. **Recommend one.** Based on the stated constraints, purpose, and team context, recommend which approach (or hybrid) fits best. Explain why.
5. **Document the rejected alternatives.** Capture why the other approaches were set aside — this is the "For the Record" context future designers need.
