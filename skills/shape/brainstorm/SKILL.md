---
name: brainstorm
description: This skill should be used when the user asks to "brainstorm", "generate ideas", "ideate", "what are my options", "think of ways to", "explore possibilities", or wants divergent thinking on any topic. Also triggers on "what could we do about", "help me think through", or "creative options for".
argument-hint: "<topic or problem to brainstorm>"
---

# Brainstorm

Generate many ideas on a topic using multiple lenses, then cluster and prioritize.

## Process

### 1. Frame the Problem

Restate the topic as a clear problem statement or "How might we..." question. Confirm understanding before generating.

### 2. Diverge: Generate Ideas Across Lenses

Apply five distinct lenses to the topic. Each lens produces 3-5 ideas. Quantity matters more than quality at this stage.

**Lenses:**

| Lens           | Question it asks                                       |
| -------------- | ------------------------------------------------------ |
| Inversion      | What if we did the opposite? What would we stop doing? |
| Analogy        | What domain solved a similar problem? How?             |
| Constraint     | What if we had half the time/budget/people?            |
| Amplification  | What if we 10x'd the ambition? What becomes possible?  |
| Simplification | What's the smallest version that still matters?        |

Present all ideas as a flat numbered list, tagged by lens. No filtering yet.

### 3. Converge: Cluster and Name

Group the ideas into 3-5 natural clusters. Name each cluster with a short phrase that captures the shared move.

### 4. Prioritize

Score each cluster on two axes:

- **Impact**: How much does this move the needle?
- **Effort**: How hard is this to start?

Present as a 2x2 matrix (high impact/low effort = quick wins, etc.).

### 5. Surface the Top Three

Pick the three strongest individual ideas across clusters. For each, write one sentence on **what** it is and one on **why** it stands out.

## Output Format

```
## Problem
[Restatement]

## Ideas (divergent)
1. [Idea] — (Inversion)
2. [Idea] — (Analogy)
...

## Clusters
### [Cluster Name]
- Idea 1, Idea 5, Idea 12
### [Cluster Name]
...

## Priority Matrix
| Cluster | Impact | Effort | Quadrant |
| ------- | ------ | ------ | -------- |
| ...     | High   | Low    | Quick Win |

## Top Three
1. **[Idea]** — [Why it stands out]
2. **[Idea]** — [Why it stands out]
3. **[Idea]** — [Why it stands out]
```

## Guidelines

- Resist the urge to evaluate during divergence. Bad ideas unlock good ones.
- If the topic is vague, ask one clarifying question before generating.
- Tailor lenses to the domain. For technical problems, Constraint and Simplification carry more weight. For strategic problems, Inversion and Amplification open more space.
- If the user provides context (files, prior work), read it first and reference it in the ideas.

## See Also

- `/spec-out` — Evaluative counterpart; use after brainstorm to scope the best ideas into a spec
- `/research` — Evidence-gathering counterpart; use to validate brainstormed options with external data
- `/design` — Structural counterpart; use when the brainstorm output needs implementation shape
- `skills/FRAMEWORKS.md` — Full framework index
- `RECIPE.md` — Agent recipe for parallel decomposition (2 workers)
