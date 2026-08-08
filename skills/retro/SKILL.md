---
name: retro
description: Reflect on recent work—capture learnings and surface what to think about next
---

# Session Retrospective

## Overview

Reflect on the work just completed in this conversation. Extract insights, not summaries.

## What I Learned

Identify 2-4 concrete technical insights from this session:

- Patterns discovered or reinforced
- Gotchas or surprises encountered
- Techniques that worked well (or didn't)
- Connections to other parts of the codebase

Focus on _insights_, not a summary of actions taken.

## What to Think About Next

Surface 2-4 open threads worth considering:

- Unfinished work or TODOs
- Edge cases or risks not yet addressed
- Potential improvements or refactors
- Questions that came up but weren't resolved

Be specific—name files, functions, or concepts rather than speaking abstractly.

## Memory Health Check

Before asking about persistence, check the current project's MEMORY.md:

1. **Read the file** from the project's auto memory directory
2. **Count lines** -- if over 50, note the size
3. **Scan for staleness signals**:
   - Items containing "resolved", "fixed", "done", "completed"
   - Date references from more than 30 days ago
   - Sections that duplicate CLAUDE.md headers
4. **Report briefly**: "MEMORY.md: [N] lines, [issues found or 'healthy']"

If issues are found, include them in the question to the user -- e.g., "MEMORY.md has 3 stale items. Want to prune them while persisting new insights?"

---

After generating the retro, ask the user if any insights are worth persisting to auto memory. Use AskUserQuestion with options like "Yes, update MEMORY.md", "Yes, and prune stale items", and "No, just this session".

If yes, read the current MEMORY.md from the project's auto memory directory and intelligently merge the new insights—don't duplicate existing points, add new ones under the appropriate sections.
