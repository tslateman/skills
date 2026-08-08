---
name: brainstorm-recipe
workers: 2
parallel: true
---

# Brainstorm — Agent Recipe

A single brainstormer anchors on early ideas and stops exploring. Two workers applying different lenses produce genuinely distinct directions, making the clustering step richer and the priority matrix honest. One worker pushes outward (what's possible?), the other pulls inward (what's practical?).

## Decomposition

Split by lens orientation. One worker runs the expansive lenses (Inversion, Analogy, Amplification) that break assumptions. The other runs the grounding lenses (Constraint, Simplification) that find the smallest useful version. Both address the same problem statement.

## Workers

### Worker 1: Expansive Thinker

**Focus:** Break assumptions. Find non-obvious directions.

**Framework:** The Inversion, Analogy, and Amplification lenses from the brainstorm skill.

**Scope boundaries:**

- Handles: opposite approaches, cross-domain analogies, 10x ambition scenarios, surprising reframings
- Does NOT handle: feasibility filtering, effort estimation, resource constraints

**Prompt template:**

> You are an expansive brainstormer. Generate ideas that break assumptions and find non-obvious directions.
>
> Apply three lenses to the problem:
>
> - **Inversion**: What if we did the opposite? What would we stop doing?
> - **Analogy**: What other domain solved a similar problem? How?
> - **Amplification**: What if we 10x'd the ambition? What becomes possible?
>
> Generate 3-5 ideas per lens. Tag each idea with its lens. Do not filter or evaluate. Bad ideas unlock good ones.
>
> Deliver: a flat numbered list of ideas tagged by lens.

### Worker 2: Grounding Thinker

**Focus:** Find the smallest useful versions. Work within real constraints.

**Framework:** The Constraint and Simplification lenses from the brainstorm skill.

**Scope boundaries:**

- Handles: resource-limited scenarios, minimum viable versions, stripped-down approaches, "what if we had half the time" framings
- Does NOT handle: blue-sky thinking, cross-domain analogies, assumption breaking

**Prompt template:**

> You are a grounding brainstormer. Generate ideas that find the simplest, most practical paths forward.
>
> Apply two lenses to the problem:
>
> - **Constraint**: What if we had half the time, budget, or people? What still works?
> - **Simplification**: What's the smallest version that still matters?
>
> Generate 4-5 ideas per lens. Tag each idea with its lens. Do not filter or evaluate. Simple ideas are not lesser ideas.
>
> Deliver: a flat numbered list of ideas tagged by lens.

## Synthesis

The manager combines worker outputs into the brainstorm skill's output format:

1. **Merge both idea lists into a single numbered sequence.** Interleave rather than concatenate; this prevents the clustering step from splitting cleanly along worker boundaries.
2. **Cluster into 3-5 groups.** Name each cluster with a short phrase. Clusters should cut across lenses, not mirror them.
3. **Build the priority matrix.** Score each cluster on Impact and Effort. Present as a 2x2 (quick wins, strategic bets, fill-ins, avoid).
4. **Surface the top three ideas.** One sentence on what, one on why. Pick across clusters and across workers.
