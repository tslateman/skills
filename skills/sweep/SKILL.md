---
name: sweep
description: Post-op check for artifacts, damage, and stale references after agent work
---

# Post-Op Sweep

## Overview

Audit the working tree after agent work completes. Find what the agents left behind.

## 1. Blast Radius

Map every file touched, across all repos affected:

```bash
git diff --stat
```

```bash
git diff --cached --stat
```

If other repos were modified (check recent tool output or plan files for cross-repo work), run `git diff --stat` there too.

Flag anything unexpected, files not mentioned in the plan or task.

## 2. Fixture and Example Damage

Check whether test fixtures, example files, seed data, or sample configs were modified:

- Look for changes to files with names like `example`, `fixture`, `seed`, `sample`, `mock`, `test-data`
- Changes that null out values, remove content, or alter structure are likely test side-effects
- These should almost always be reverted

## 3. Stale References

Search for references that became outdated by the work:

- **Plan files** referencing work as "pending" or "TODO" that's now done
- **CLAUDE.md / README** listing features as planned that are now implemented
- **Comments** saying "not yet implemented" for code that now exists
- **Config or docs** pointing to old file paths, function names, or APIs that changed

## 4. Debug Artifacts

Scan for artifacts agents leave behind:

- `console.log`, `print()`, `echo "DEBUG"` statements
- Temporary files (`*.tmp`, `*.bak`, `/tmp/` references)
- Commented-out code blocks that serve no purpose
- Test data written to production data directories

## 5. Scope Bleed

Identify changes outside the task scope:

- Unrelated formatting changes
- Dependency updates not requested
- Refactors beyond what the plan called for
- Changes in other repos' working trees that predate this session

## 6. Plan Criteria

If plan files exist for the work just completed, check acceptance criteria:

- Read each criterion
- Verify whether it was met (by reading code, not re-running tests)
- Flag any unmet criteria

## Report

Present findings as a short checklist:

- **Clean**, no issues found (say so and stop)
- **Fix**, items that need correction (damaged fixtures, stale refs, debug artifacts)
- **Note**, items worth awareness but not blocking (scope bleed, unrelated changes)

Be terse. Name files and line numbers. Skip categories with no findings.

## See Also

The post-agent triad: sweep checks for collateral damage, the other two check fidelity and threads.
