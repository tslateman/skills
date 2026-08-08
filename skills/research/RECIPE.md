---
name: research-recipe
workers: 2
parallel: true
---

# Research — Agent Recipe

Technical research splits between external discovery and internal analysis. External research finds what's possible — libraries, APIs, approaches, community experience. Internal research finds what exists — current patterns, constraints, dependencies. Running both in parallel halves research time and prevents the common failure of recommending solutions that ignore codebase realities.

## Decomposition

Split research by information source. One worker searches outward (web, docs, community). The other searches inward (codebase, existing patterns, constraints). Both investigate the same question from opposite directions.

## Workers

### Worker 1: External Researcher

**Focus:** What exists outside the codebase? What do others do?

**Framework:** The "Gather Evidence" and "Evaluate Sources" sections of the research skill, covering web search, documentation, and source reliability.

**Scope boundaries:**

- Handles: library evaluation, API comparison, community sentiment, official documentation, best practices, prior art in other projects
- Does NOT handle: codebase analysis, existing pattern detection, internal constraint mapping

**Prompt template:**

> You are an external research specialist. Investigate the question by searching outside the codebase.
>
> Your sources, in order of reliability:
>
> 1. Official documentation, specs, RFCs
> 2. Maintainer statements, changelogs, release notes
> 3. Reputable tech blogs, conference talks
> 4. Community discussions
>
> For library/framework evaluation, assess: maintenance health, adoption, documentation quality, TypeScript support, breaking change history, bundle size (if frontend).
>
> For API/service comparison, assess: pricing, rate limits, latency, reliability, auth complexity, SDK quality.
>
> Cite every source. Flag anything that lacks a date, author, or contradicts official docs.
>
> Deliver findings as a structured list of key findings with sources, a comparison table if evaluating alternatives, and open questions.

### Worker 2: Internal Researcher

**Focus:** What does the codebase already do? What constraints exist?

**Framework:** The "Codebase" evidence source and "Architectural Decisions" pattern from the research skill.

**Scope boundaries:**

- Handles: existing patterns and precedents, dependency analysis, integration points, internal constraints, team conventions, related code
- Does NOT handle: external library evaluation, web search, community sentiment

**Prompt template:**

> You are an internal research specialist. Investigate the question by searching inside the codebase.
>
> Examine:
>
> - How does the codebase solve similar problems today? Find precedents
> - What dependencies, frameworks, and patterns are already in use?
> - What constraints do existing interfaces and contracts impose?
> - Where would a new solution integrate? What does it touch?
> - What conventions does the team follow for this kind of problem?
>
> Reference specific files and line numbers. Show code patterns, not descriptions.
>
> Deliver findings as: existing patterns found (with file references), constraints and integration points, and compatibility notes for any external solution.

## Synthesis

The manager combines worker outputs into a unified research report:

1. **Cross-reference external options against internal constraints.** An external solution that conflicts with existing patterns or breaks conventions needs that tension called out. Highlight compatible options.
2. **Merge findings into the research skill's output format.** Summary, Key Findings (from both sources), Comparison table, Recommendation, Open Questions.
3. **Ground the recommendation.** The recommendation must account for both external merit and internal fit. "Library X is best in isolation but Library Y fits our existing patterns" is a valid conclusion.
4. **Surface gaps.** If external research found options that internal research couldn't evaluate (e.g., no similar pattern exists in the codebase), flag this as an open question.
