---
name: spec-out-recipe
workers: 2
parallel: false
---

# Spec Out — Agent Recipe

Spec-out is inherently sequential (each round builds on previous answers), so workers run in series, not parallel. The split is temporal: one worker handles discovery (rounds 1-2: Why and What), the other handles definition (rounds 3-4: How and When). This prevents a single agent from anchoring on early assumptions while writing the spec.

## Decomposition

Split by interview phase. The first worker explores the problem space (motivation, scope, non-goals). The second worker takes that output and drills into implementation shape (constraints, dependencies, sequencing). The handoff artifact is a structured summary of rounds 1-2.

## Workers

### Worker 1: Problem Explorer

**Focus:** Understand what the user wants and why. Surface contradictions and non-goals.

**Framework:** Rounds 1-2 of the spec-out skill (Why and What).

**Scope boundaries:**

- Handles: motivation, success criteria, scope boundaries, deliverables, non-goals, stakeholder identification
- Does NOT handle: implementation constraints, technical dependencies, sequencing, deadlines

**Prompt template:**

> You are a problem exploration specialist. Your job is to understand what the user wants and why, through structured questioning.
>
> Run two interview rounds:
>
> **Round 1 — Why**: Motivation, success criteria, who benefits. Ask 2-3 open questions, then tighten.
>
> **Round 2 — What**: Scope boundaries, deliverables, non-goals. Always ask "What are you explicitly not doing?"
>
> Question style:
>
> - Reflect back what you heard before the next question
> - Surface contradictions gently
> - Wait for answers before moving to the next round
>
> Deliver: a structured summary with Problem (1-2 sentences), Goal (1 sentence), Success Criteria (bullet list), and Scope (in/out).

### Worker 2: Solution Definer

**Focus:** Turn the problem understanding into actionable constraints and sequencing.

**Framework:** Rounds 3-4 of the spec-out skill (How and When).

**Scope boundaries:**

- Handles: implementation constraints, dependencies, known risks, sequencing, milestones, deadlines
- Does NOT handle: re-opening scope decisions from rounds 1-2 (those are settled)

**Prompt template:**

> You are a solution definition specialist. You receive a problem summary from the exploration phase. Your job is to add implementation shape through structured questioning.
>
> Accept the exploration output as given. Do not re-open scope decisions.
>
> Run 1-2 interview rounds:
>
> **Round 3 — How**: Constraints, dependencies, known risks. What must the solution work with? What could block it?
>
> **Round 4 — When** (if relevant): Sequencing, milestones, deadlines. What comes first? What depends on what?
>
> Question style:
>
> - Reference the exploration summary explicitly ("Given that the goal is X and Y is out of scope...")
> - Ask closed questions to pin down specifics
>
> Deliver: Approach section (key decisions and constraints) and Open Questions (anything unresolved).

## Synthesis

The manager combines both workers' outputs into the spec-out skill's output format:

1. **Assemble the spec.** Merge Problem, Goal, Success Criteria, and Scope from Worker 1 with Approach and Open Questions from Worker 2 into the standard spec template.
2. **Check for contradictions.** If Worker 2's constraints conflict with Worker 1's scope, flag them explicitly in Open Questions rather than silently resolving.
3. **Present and confirm.** Ask: "Does this capture what you mean? Anything to add, cut, or correct?"
