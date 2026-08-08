---
name: code-review
description: Framework for code review that captures context future maintainers need: concerns raised, alternatives rejected, risks accepted. Use for PRs, local changes, or architecture review when the decision matters more than the diff. Produces structured feedback with must-address issues, suggestions, and observations "for the record."
---

# Structured Code Review

## Overview

Code review that captures context, not just correctness. Grounded in Bacchelli & Bird's research on modern code review, which found that code review's primary value is knowledge transfer, not defect detection. Beyond finding bugs, document the _why_, concerns raised, alternatives considered, risks accepted. This creates organizational memory for future maintainers.

Use this for PRs, local changes, or architecture review, any code where you want to preserve the reasoning, not just the verdict.

## Review Workflow

### 1. Understand the Change

Before commenting, understand intent:

- What problem does this solve?
- What was the previous state?
- What constraints shaped the solution?

```
Read the PR description, linked issues, and recent commits.
If context is missing, ask before reviewing.
```

### 2. Evaluate on Multiple Dimensions

**Correctness**, Does it work?

- Logic errors, edge cases, error handling
- Does it match stated requirements?

**Design**, Is this the right approach?

- Does it fit existing patterns in the codebase?
- Are there simpler alternatives?
- Will this scale if assumptions change?

**Maintainability**, Can others work with this?

- Is the code readable without comments?
- Are names clear and consistent?
- Is complexity justified?

**Risk**, What could go wrong?

- Performance implications
- Security considerations
- Breaking changes, backwards compatibility
- Operational concerns (monitoring, debugging)

### 3. Document Your Review

Structure feedback for the record:

```markdown
## Summary

[1-2 sentence assessment: approve, request changes, or needs discussion]

## What This Changes

[Brief description of the change and its purpose]

## Feedback

### Must Address

- [Blocking issue] — [Why it matters]

### Should Consider

- [Non-blocking suggestion] — [Trade-off or alternative]

### Observations

- [Pattern noticed, question raised, or context captured]

## Concerns for the Record

[Risks accepted, alternatives rejected, assumptions made; future maintainers need this]

## Alternatives Considered

[Other approaches discussed and why they were rejected]
```

### 4. Calibrate Feedback

**Blocking issues** (Must Address):

- Bugs that will cause failures
- Security vulnerabilities
- Breaking changes without migration
- Violations of hard requirements

**Suggestions** (Should Consider):

- Better approaches that aren't urgent
- Style preferences beyond project standards
- Optimizations without clear need

**Observations** (For the Record):

- "This assumes X remains true"
- "If Y changes, this will need rework"
- "We chose this over Z because..."

## Review Patterns

### PR Review (with GitHub CLI)

```bash
# View PR details
gh pr view [number]

# View PR diff
gh pr diff [number]

# View PR comments
gh api repos/{owner}/{repo}/pulls/{number}/comments

# Add review comment
gh pr review [number] --comment --body "..."

# Approve or request changes
gh pr review [number] --approve
gh pr review [number] --request-changes --body "..."
```

### Local Code Review

For code not yet in a PR:

1. Read the changed files
2. Check git diff for what's new
3. Understand context from surrounding code
4. Apply the review dimensions above

### Architecture Review

For larger changes:

1. Map the change across files
2. Trace data flow and control flow
3. Identify coupling and dependencies
4. Consider failure modes
5. Document assumptions explicitly

## Anti-Patterns

**Rubber stamping**, Approving without understanding. If you don't have time, say so.

**Style nitpicking**, Bikeshedding on preferences not in project standards. Automate style with linters.

**Drive-by criticism**, Pointing out problems without suggesting solutions or understanding constraints.

**Scope creep**, Requesting changes unrelated to the PR's purpose. File separate issues.

**Assumption silence**, Noticing risks but not documenting them. Future you will wish you had.

## The "For the Record" Principle

The most valuable reviews capture what _won't_ be obvious later:

- "We discussed using X but chose Y because of constraint Z"
- "This is a temporary solution until the Q2 migration"
- "Performance is acceptable for current load but watch metric M"
- "This duplicates code in file F; intentional to avoid coupling"

When warnings are ignored, the review becomes evidence. When they're heeded, it becomes context. Either way, document it.

## Output Quality

A good review:

- Distinguishes blocking issues from suggestions
- Explains _why_, not just _what_
- Captures context that isn't in the code
- Helps the author improve, not just comply
- Creates value for future readers

## See Also

- `/naming`: Code review surfaces naming problems; naming review deepens code review
- `/adr`: Reviews that capture architectural decisions belong in ADRs
- `/prose`: Write review comments clearly using Strunk's rules
- `skills/FRAMEWORKS.md`: Full framework index
- `RECIPE.md`: Agent recipe for parallel decomposition (3 workers)
