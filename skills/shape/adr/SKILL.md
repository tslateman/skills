---
name: adr
description: Generate Architecture Decision Records that capture the reasoning behind technical decisions. Use when the user asks to "create an ADR", "document a decision", "record why we chose X", or discusses architectural trade-offs worth preserving.
---

# Architecture Decision Record Generator

Generate an Architecture Decision Record (ADR) based on the conversation context and any architectural decisions discussed.

## ADR Format

Create a markdown file with this structure:

```markdown
# ADR-[NUMBER]: [TITLE]

**Date:** [YYYY-MM-DD]
**Status:** [Proposed | Accepted | Deprecated | Superseded]
**Deciders:** [Who was involved]

## Context

What is the issue that we're seeing that is motivating this decision or change?

## Decision

What is the change that we're proposing and/or doing?

## Consequences

What becomes easier or more difficult to do because of this change?

### Positive

- [Benefit 1]
- [Benefit 2]

### Negative

- [Trade-off 1]
- [Trade-off 2]

### Risks

- [Risk and mitigation]

## Alternatives Considered

### [Alternative 1]

- **Description:** What was this option?
- **Rejected because:** Why didn't we choose it?

### [Alternative 2]

- **Description:** What was this option?
- **Rejected because:** Why didn't we choose it?

## References

- [Related PR, issue, or document]
- [Relevant discussion or prior art]
```

## Instructions

1. **Extract from context**: Use the conversation to identify:
   - The problem or decision being made
   - Options that were discussed
   - The chosen approach and rationale
   - Trade-offs acknowledged

2. **Find the ADR location**: Look for existing ADRs:
   - `docs/adr/` or `docs/decisions/`
   - `adr/` at project root
   - If none exist, suggest creating `docs/adr/`

3. **Number appropriately**: Check existing ADRs and use the next number

4. **Write concisely**: ADRs should be scannable:
   - Context: 2-4 sentences
   - Decision: 1-2 sentences
   - Consequences: Bullet points
   - Alternatives: Brief, focused on why rejected

5. **Capture the why**: The decision itself ages; the reasoning stays valuable

## See Also

- `/research`: Research informs the decision; ADR captures it
- `/review-decisions`: Reviews that surface architectural decisions belong in ADRs
- `skills/FRAMEWORKS.md`: Full framework index
