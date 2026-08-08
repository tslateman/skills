---
name: visual-recap-recipe
workers: 2
parallel: true
---

# Visual Recap, Agent Recipe

A recap splits on its own grounding rule. Mechanical extraction, file map,
schema table, API table, key-change diffs, must be true by construction, pulled
straight from the diff with no judgment. The narrative and UI read, what changed,
why, the risk, the before/after, is where judgment lives. Running these as one
context blurs the line and invites inferred "facts" into the structured blocks.
Two workers keep extraction honest and let the narrative breathe.

## Decomposition

Both workers read the same diff. Worker 1 extracts only what the diff literally
contains and never editorializes. Worker 2 reads the same diff for intent and
visible UI delta and never invents a path, field, or line. The manager assembles
their outputs into the canonical skeleton.

## Workers

### Worker 1: Diff Cartographer

**Focus:** What did the diff literally change?

**Framework:** The Grounding Rule and Diff-to-Artifact Mapping from the skill.

**Scope boundaries:**

- Handles: changed-file map with flags, schema/migration table, API/route table,
  selection of the 3-8 load-bearing files, the focused fenced diffs and their
  one-line summaries, secret redaction.
- Does NOT handle: the narrative, the "why", risk assessment, wireframes.

**Prompt template:**

> You are a diff cartographer. Extract only what this diff literally changed
> never infer, round, or invent. Produce:
>
> - A changed-file map: every file with an added/removed/modified/renamed flag and
>   a one-line note.
> - A schema table for any migration: entity, field, change flag, prior type in a
>   `was` column.
> - An API table for any route/action change: method, path, params, request/
>   response shape after the change, with changed params flagged.
> - The 3-8 load-bearing files, each as a focused fenced diff (under ~150 lines)
>   with a one-line summary of what it changes and why it matters.
>
> Redact any secret (`sk-•••`, `<redacted>`). When the diff does not contain a
> fact, leave it out. Write no narrative, another worker owns that.

### Worker 2: Narrative & UI Author

**Focus:** What changed, why, and what does it look like?

**Framework:** Canonical Shape (narrative + UI headline) and Lean-but-Substantial
from the skill.

**Scope boundaries:**

- Handles: the 1-3 paragraph outcome narrative, the load-bearing decisions visible
  in the diff, the risk read, before/after wireframes or screenshots, the
  architecture/data-flow diagram.
- Does NOT handle: file maps, schema/API tables, raw diff extraction.

**Prompt template:**

> You are the narrative and UI author for a code-change recap. Read the diff for
> intent and visible delta, but never invent a path, field, or line, ground every
> claim in the actual change and mark anything inferred as inferred. Produce:
>
> - A 1-3 paragraph outcome narrative: the objective the diff served, the key
>   decisions visible in it, the risk a reviewer should weigh. No boilerplate, no
>   provenance, no "still review the diff" prose.
> - When the diff changed rendered UI: a before/after wireframe (`html-style`) or
>   screenshot showing the entry point, the opened surface, and the resulting
>   state. Permissions changes show manager vs. viewer.
> - When the diff shifts architecture or data flow: a two-dimensional `mermaid`
>   or `html-style` diagram, never a flat chain.
>
> Keep it lean but substantial, not a one-wireframe-one-sentence stub.

## Synthesis

The manager assembles one recap in the canonical skeleton:

1. **UI headline first** when Worker 2 produced one.
2. **Narrative** from Worker 2.
3. **Schema and API tables** from Worker 1.
4. **Changed-file map** from Worker 1.
5. **`## Key changes`**, Worker 1's focused diffs, each under its summary.

Then: enforce the budgets (3-8 key files, title ≤70 chars, narrative ≤3
paragraphs), drop any section the diff did not touch, confirm no secret survived
redaction, and gate visibility to match the source repo. Choose the output target
Markdown, `html-style` doc, or Mermaid-in-Markdown, by where the recap will be
read.
