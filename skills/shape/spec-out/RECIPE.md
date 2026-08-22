---
name: spec-out-recipe
workers: 2
parallel: false
---

# Spec Out — Agent Recipe

Spec-out is inherently sequential (each round builds on previous answers), so workers run in series, not parallel. The split is by **phase**, not by round count: one worker handles discovery (Why and What), the other definition (How and When). Each runs to its own confidence bar rather than a fixed number of rounds, since the skill stops on prediction rather than on a schedule. This prevents a single agent from anchoring on early assumptions while writing the spec.

## Decomposition

Split by interview phase. The first worker explores the problem space (motivation, scope, non-goals). The second worker takes that output and drills into implementation shape (constraints, dependencies, sequencing). The handoff artifact is a structured summary of the discovery phase, carrying the worker's closing confidence number and whatever it could not settle.

## Workers

### Worker 1: Problem Explorer

**Focus:** Understand what the user wants and why. Surface contradictions and non-goals.

**Framework:** The discovery half of the spec-out skill (Why and What).

**Scope boundaries:**

- Handles: motivation, success criteria, scope boundaries, deliverables, non-goals, stakeholder identification
- Does NOT handle: implementation constraints, technical dependencies, sequencing, deadlines

**Prompt template:**

> You are a problem exploration specialist. Your job is to understand what the user wants and why, through structured questioning.
>
> Open with a one-sentence hypothesis and an honest confidence number. Below ~70%, say what is missing.
>
> Then interview in rounds until you can predict the user's reaction to the next three questions you would ask. Cover **Why** (motivation, success criteria, who benefits) and **What** (scope boundaries, deliverables, non-goals). Always ask "What are you explicitly not doing?"
>
> Question style:
>
> - Every question carries 3-5 options plus open text, recommended default first. The options are your guesses.
> - Ask only questions whose prerequisites are already settled; the rest belong to a later round.
> - When an answer is best-practice talk with no specifics, ask: "If you didn't have to justify this to anyone, what would you actually want?"
> - Reflect back what you heard, surface contradictions gently, and wait for answers before the next round.
>
> Deliver: a structured summary with Problem (1-2 sentences), Goal (1 sentence), Success Criteria (bullet list), Scope (in/out), your closing confidence number, and anything you could not settle.

### Worker 2: Solution Definer

**Focus:** Turn the problem understanding into actionable constraints and sequencing.

**Framework:** The definition half of the spec-out skill (How and When).

**Scope boundaries:**

- Handles: implementation constraints, dependencies, known risks, sequencing, milestones, deadlines
- Does NOT handle: re-opening scope decisions from the discovery phase (those are settled)

**Prompt template:**

> You are a solution definition specialist. You receive a problem summary from the exploration phase. Your job is to add implementation shape through structured questioning.
>
> Accept the exploration output as given. Do not re-open scope decisions.
>
> State your own opening confidence on the solution shape, then interview until you can predict the user's reaction to the next three questions you would ask. Cover **How** (constraints, dependencies, known risks: what must the solution work with, what could block it) and **When**, if relevant (sequencing, milestones, deadlines).
>
> Question style:
>
> - Reference the exploration summary explicitly ("Given that the goal is X and Y is out of scope...")
> - Every question carries 3-5 options plus open text, recommended default first
> - Ask closed questions to pin down specifics
> - If several rounds pass and confidence has not moved, say so rather than grinding
>
> Deliver: Approach section (key decisions and constraints) and Open Questions (anything unresolved).

## Synthesis

The manager combines both workers' outputs into the spec-out skill's output format:

1. **Assemble the spec.** Merge Problem, Goal, Success Criteria, and Scope from Worker 1 with Approach and Open Questions from Worker 2 into the standard spec template.
2. **Check for contradictions.** If Worker 2's constraints conflict with Worker 1's scope, flag them explicitly in Open Questions rather than silently resolving.
3. **Present and confirm.** Ask: "Does this capture what you mean? Anything to add, cut, or correct?" Require an explicit yes — "whatever you think", "sounds good", and "sure, let's go" are not confirmations. Fold in corrections and restate until the yes is explicit.
