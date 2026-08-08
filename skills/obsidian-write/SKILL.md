---
name: obsidian-write
description: Write, append, or create notes in the user's Obsidian vault (path from `$OBSIDIAN_VAULT`). Use whenever the user asks to save something to Obsidian, capture a note in their vault, log something to today's daily note, write up a decision, insight, or meeting note, turn a conversation or article into a permanent note, or says things like "add this to my vault," "save this to my notes," or "capture this in Obsidian" — even if they don't name the skill explicitly.
---

# Write to Obsidian

## Vault

Path: `$OBSIDIAN_VAULT` if set, otherwise `~/Documents/Obsidian`. Resolve it once at the start and use it for every path below.

Treat the vault as a git repo whose commits belong to the user. Never `git commit` as part of this skill.

## Read the vault's own conventions before writing — don't rely on this file for them

The vault documents its own frontmatter and tagging rules, and it evolves. Copying those rules into this skill would drift out of sync the next time the user changes them. Instead, before creating or editing any note, read:

- `Resources/Frontmatter Tagging Guide.md` — required and optional frontmatter fields per note type (`daily`, `insight`, `review`, `decision`, etc.), the standard theme tags, and when to add each field
- `Resources/Templates/Templates.md` — index of available templates, then read the specific template file under `Resources/Templates/` matching what you're creating (e.g. `Claude Conversation.md` for capturing a chat session, `Knowledge Capture.md` for an external source, `Meeting Note Template.md` for meetings)

Treat these two files as the source of truth. If something you're about to write conflicts with what they say, follow them, not your prior assumptions.

## Folder structure (PARA)

- `Areas/` — active, ongoing life domains (not time-bound)
- `Daily/` — one file per day, named `YYYY-MM-DD.md`
- `Projects/` — time-bound initiatives with a specific outcome
- `People/` — notes about specific people
- `Resources/` — reference material, templates, tools
- `z.Archive/` — historical or inactive content

If it's unclear whether something belongs in Areas or Projects, check `Areas/Areas vs Projects.md` — the vault already defines the distinction, so use its definition rather than guessing.

## Decide: append to today's daily note, or create a new permanent note?

- **Quick capture** — a link, a passing thought, something that happened today, a stray idea worth not losing → append to `Daily/YYYY-MM-DD.md` under `## Quick Capture`. Don't create a new file for this.
- **Durable knowledge** — an insight, a decision, meeting notes, a writeup of an article or conversation, a concept worth its own page → create a new file in the right PARA folder using the matching template.
- **When ambiguous, default to the daily note.** The vault's own workflow promotes daily-note content into permanent notes during a weekly review (see the `status: needs-synthesis` field in the Frontmatter Tagging Guide) — so a quick capture today isn't a lost opportunity, it's the normal first step.

## Today's daily note is always in the loop

Every write touches today's daily note in some way — quick captures go straight into it, and permanent notes get a link from it (see below). Because of this, check whether `Daily/YYYY-MM-DD.md` for today exists _before_ doing anything else, and create it if it doesn't.

Check the most recent existing file in `Daily/` for the exact current frontmatter and header format before creating a new one — don't hardcode it here, since the format can change. As of this writing, daily notes open with frontmatter (`type: daily`, `tags: [journal]`) followed by a prev/next link line, e.g.:

```
← [[2026-07-21]] | [[2026-07-23]] →
```

Create today's note following that same pattern, with the date links pointing at yesterday's and tomorrow's note (as wikilinks, whether or not those files exist yet).

## Creating a new permanent note

1. Pick the PARA folder (above).
2. Pick and read the matching template from `Resources/Templates/`.
3. Name the file in Title Case with spaces, matching the existing files in that folder — don't switch to kebab-case or snake_case.
4. Fill in frontmatter per the Frontmatter Tagging Guide's rules for that note's `type`.
5. **Link the new note from today's daily note by default.** Add a `[[wikilink]]` to the new note under `## Quick Capture` (or wherever fits naturally) in `Daily/YYYY-MM-DD.md`. This is the default entry point into the note regardless of what the note is about — only skip it, or link from somewhere else instead, if the user specifies a different source to link from (e.g. "link this from the CASSANDRA project note instead"). If the note is explicitly derived from a _different_ day's daily note (e.g. promoting an older quick capture during a weekly review), link back to that day's note instead of today's, and don't also force a link from today's.
6. **Search for an existing note with this title or a close synonym before creating one.** Prefer appending to or linking from an existing note over creating a near-duplicate — duplicate notes fragment the vault's own knowledge graph.

## After writing

- Report the file path you wrote to (or appended to).
- Don't run `git commit` — leave that to the user.
- Don't touch `.obsidian/` (app configuration), and don't move or rename existing notes unless explicitly asked to.

## Prose the user will publish

Vault notes are usually private capture and need no check. When a note is headed
somewhere else — a post, a proposal, a letter, anything going out under your
name — offer `/voice` before writing it, and `/slop-check` if the note argues a
position. Don't run either unprompted on daily capture.
