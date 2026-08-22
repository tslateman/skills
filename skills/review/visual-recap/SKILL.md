---
name: visual-recap
description: Turn a PR, branch, commit, or git diff into a structured visual recap so a reviewer scans the shape of the change before reading raw lines. Use when asked to "recap this PR/branch", "show me what changed", or to summarize a large multi-file diff at a higher altitude than line-by-line review.
---

# Visual Recap

A recap is a structured summary built **from** a diff, not toward one. Forward
planning describes the change you are about to make; a recap describes the change
that was just made, one altitude above line-by-line review. A reviewer scans the
shape of the change, UI delta, schema delta, contract delta, file footprint
before spending attention on the literal lines.

Adapted from BuilderIO/skills `visual-recap`. The discipline is theirs; the
output targets are yours. There is no hosted plan renderer here, so author plain
artifacts.

## When to use

Build a recap when a PR or commit is large, multi-file, or touches schema, API
contracts, or architecture, and a reviewer benefits from seeing the change mapped
to structure before reading the diff. Skip it for small, single-file, or obvious
diffs, a recap is review overhead, and a tiny change reviews faster as plain
diff. Never pad a trivial diff into a recap.

Default scope is the whole work unit: original implementation plus later fixes,
tests, and follow-ups, not only the most recent commit. Use the diff plus
context to separate work-unit changes from unrelated pre-existing edits, and
exclude the unrelated ones. State the assumption if scope is ambiguous.

## The Grounding Rule

Structured blocks are **true by construction** only when derived mechanically
from the actual changed lines. Build the file map, schema table, API table, and
diffs from the real diff, real paths, real fields, real method and path, real
before/after text. Never infer, round, or invent them. The model writes only the
prose: the "why", the narrative, the risk read. A confidently wrong recap is
dangerous, because a reviewer who trusts the summary skips the line the summary
got wrong. When the diff does not contain a fact, leave it out. Mark anything
inferred rather than extracted as inferred.

## Canonical shape and budgets

A strong recap follows one skeleton, top to bottom. Drop any section the diff
does not touch.

1. **UI headline**, before/after wireframe or screenshot, first, when the diff
   changed rendered UI.
2. **Outcome narrative**, 1-3 paragraphs: what changed and why, the key
   decisions visible in the diff, the risk a reviewer should weigh. The only
   place you write freely.
3. **Schema / contract changes**, a `data-model` table for migrations, an
   endpoint table for API/route changes.
4. **Changed-file map**, every changed file with an added/removed/modified/
   renamed flag and a one-line note, so the footprint reads at a glance.
5. **Key changes**, focused diffs of the 3-8 load-bearing files, each under a
   one-line summary of what it changes and why.

Budgets that keep it reviewable:

- 3-8 key-change diffs. Fewer than 3 on a large change under-serves the reviewer;
  more than 8 stops being a summary.
- Keep each excerpt focused, prefer under ~150 lines; summarize or link the rest
  of a long file instead of dumping it.
- Title at most ~70 characters; narrative 1-3 short paragraphs.

## Lean, but substantial

Add no boilerplate: no intro, disclaimer, provenance, file-count, or "this is an
aid, still review the diff" prose. The title, narrative, and file map already
carry that. Add a prose note only when it tells the reviewer something the
structured blocks do not, the objective, a real compatibility risk, a load-
bearing decision visible in the diff.

Lean is not thin. A recap is not one wireframe plus one sentence, that
under-serves the reviewer as much as boilerplate over-serves them. A 40-file
change needs the file map and the key-change diffs, not a three-block stub that
forces the reviewer back into the raw diff anyway.

## Diff to Artifact Mapping

Map each kind of change to the artifact that carries it, derived from the real
diff.

- **Schema / migration** → a Markdown table of the resulting entities and fields,
  flagging each row added / modified / removed / renamed and the prior type in a
  `was` column for a changed type. The table is the headline; show the literal
  SQL diff only when the exact statement still matters.
- **API / action / route** → a table with method, path, params, and request/
  response shape after the change. Flag each changed param or response; mark
  removed routes deprecated and explain in prose.
- **Architecture or data-flow shift** → a `mermaid` graph or an `html-style`
  diagram, two-dimensional (paired before/after, layered, or swimlane), never a
  flat left-to-right chain. Do not use a diagram as a stand-in for rendered UI.
- **Rendered UI change** → a before/after wireframe (via `html-style`) or a
  screenshot showing the visible delta before any code. Show the entry point, the
  opened surface, and the resulting state, not just the first affordance. When
  permissions change, show what managers do and what viewers see instead.
- **Any meaningful code hunk** → a fenced diff with a one-line summary above it
  saying what it changes and why, so the reviewer reads intent first. Never leave
  a diff unlabeled. Group several key-file diffs under a `## Key changes` heading.
- **Brand-new file** → an annotated walkthrough of the new code (a few high-signal
  notes on the lines that matter), not a one-sided diff. Reserve real diffs for
  before/after hunks where the removed lines still carry meaning.
- **Files added / removed / renamed** → the changed-file map with a flag and a
  short note per entry.

## Security

- **Gate visibility.** A recap of a private repo can expose unreleased schema,
  internal endpoints, and architecture, treat it like the source it summarizes.
  Do not post it anywhere broader than the source. When linking it on a private
  PR, say reviewers may need org access for it to load.
- **Never transcribe secrets.** A diff can contain API keys, tokens, webhook
  URLs, signing secrets, or `.env` values. Redact them (`sk-•••`, `<redacted>`)
  in every diff, file note, table, and prose block. Obviously fake placeholders
  only, never the real value.

## Output Targets

- **Markdown**, the default. A PR comment, or an Obsidian note linked from the
  daily note. Tables, fenced diffs, and a Mermaid block all render on GitHub.
- **`html-style` HTML doc**, when the recap is a standalone artifact worth
  keeping: pick Blueprint, Drafting Table, or Phosphor from that skill and fill
  the matching template. Use it when wireframes or rich before/after panels carry
  the story.
- **`mermaid`**, for the architecture or data-flow diagram inside either of
  the above.

Never hand the recap over as a vague chat summary when the change is large, the
structure is the value. A flat "here's what changed" paragraph is the thing a
recap replaces, not a lighter version of one.
