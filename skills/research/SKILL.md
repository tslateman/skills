---
name: research
description: Systematic technical investigation: evidence gathering, option comparison, and actionable recommendations. Use when the user asks to "research X", "investigate Y", "compare X vs Y", "how does X work", or needs analysis of libraries, APIs, frameworks, or architectural approaches.
---

# Technical Research

## Overview

Systematic technical research for staff-level software engineering decisions. Gather evidence, synthesize findings, and present actionable recommendations.

## Research Workflow

### 1. Scope the Question

Before searching, clarify:

- What decision does this research inform?
- What constraints exist (language, framework, team expertise)?
- What "good enough" looks like, avoid rabbit holes

### 2. Gather Evidence

Use multiple sources in parallel:

**Web search**, current state, recent changes, community sentiment

```
WebSearch: "[topic] 2026" or "[library] vs [alternative]"
```

**Documentation**, authoritative specs and APIs

```
Context7: resolve-library-id then query-docs
WebFetch: official docs, RFCs, specifications
```

**Codebase**, existing patterns and constraints

```
Grep/Glob: how similar problems are solved today
```

### 3. Evaluate Sources

Weight sources by reliability:

1. Official documentation, specs, RFCs
2. Maintainer statements, changelogs, release notes
3. Reputable tech blogs, conference talks
4. Community discussions (HN, Reddit, Discord)
5. AI-generated content, outdated tutorials

**Red flags:** No date, no author, SEO-heavy content, contradicts official docs

### 4. Synthesize Findings

Structure output for decision-making:

```markdown
## Summary

[1-2 sentence answer to the core question]

## Key Findings

- Finding 1 (source)
- Finding 2 (source)
- Finding 3 (source)

## Comparison (if applicable)

| Criterion    | Option A | Option B |
| ------------ | -------- | -------- |
| [Key factor] | ...      | ...      |

## Recommendation

[Clear recommendation with rationale]

## Open Questions

[What remains uncertain, what to monitor]
```

### 5. Cite Sources

Always include sources:

```markdown
Sources:

- [Official Docs](url)
- [Relevant Article](url)
```

## Research Patterns

### Library/Framework Evaluation

Investigate:

1. **Maintenance**, Last release, commit frequency, issue response time
2. **Adoption**, npm downloads, GitHub stars, production users
3. **Documentation**, Quality, examples, migration guides
4. **Bundle size**, For frontend, check bundlephobia
5. **TypeScript**, Native support or @types package quality
6. **Breaking changes**, Major version history, upgrade difficulty

### API/Service Comparison

Investigate:

1. **Pricing**, Free tier limits, scaling costs
2. **Rate limits**, Requests/second, daily quotas
3. **Latency**, P50/P99, geographic distribution
4. **Reliability**, SLA, status page history
5. **Auth**, OAuth, API keys, complexity
6. **SDK quality**, Official vs community, maintenance

### Architectural Decisions

Investigate:

1. **Prior art**, How do similar systems solve this?
2. **Trade-offs**, What does each approach sacrifice?
3. **Reversibility**, How hard to change later?
4. **Team fit**, Existing expertise, learning curve
5. **Operational cost**, Monitoring, debugging, scaling

## Reference Material

For detailed research patterns and techniques, see:

- **`references/patterns.md`**, Common research scenarios with examples

## See Also

- `/adr`: Research informs the decision; ADR captures it
- `skills/FRAMEWORKS.md`: Full framework index
- `RECIPE.md`: Agent recipe for parallel decomposition (2 workers)
