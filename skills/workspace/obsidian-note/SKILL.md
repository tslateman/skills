---
name: obsidian-note
description: Write, append, or create notes in the user's Obsidian vault (path from `$OBSIDIAN_VAULT`). Use whenever the user asks to save something to Obsidian, capture a note in their vault, log something to today's daily note, write up a decision, insight, or meeting note, turn a conversation or article into a permanent note, or says things like "add this to my vault," "save this to my notes," or "capture this in Obsidian" — even if they don't name the skill explicitly.
---

# Write to Obsidian

Every vault has its own folders, frontmatter, and naming. This skill reads those
conventions from the vault itself before each write. It does not carry a copy of
them, because a copy drifts the next time the user changes something.

Treat the vault as a git repo whose commits belong to the user. Never
`git commit` as part of this skill. Never touch `.obsidian/`. Never move or
rename an existing note unless asked.

## 1. Find the vault

Try these in order and stop at the first that works.

1. `$OBSIDIAN_VAULT`.
2. A directory that contains `.obsidian/`. Search `~/Documents`, `~`, and
   `~/Library/Mobile Documents` to a depth of 3.
3. Ask the user for the path.

Resolve it once. Use it for every path below. If step 2 finds more than one
vault, list them and ask.

## 2. Read the vault's conventions

Read whichever of these the vault has. Do not fail when one is absent.

| Look for                                         | Gives you                     |
| ------------------------------------------------ | ----------------------------- |
| `CLAUDE.md` or `README.md` at the vault root     | Stated rules and hub notes    |
| A note naming frontmatter, tagging, or templates | Required fields per note type |
| A templates folder                               | The shape for each note type  |
| The newest file in the daily-notes folder        | Live frontmatter and header   |

Find the first two with a filename search for `frontmatter`, `tagging`,
`convention`, or `template`. These files are the source of truth. When something
you are about to write conflicts with them, follow them.

When the vault documents none of this, infer from the three most recently
modified notes in the target folder and say what you inferred.

## 3. Learn the folder structure

List the vault's top-level directories. Do not assume a scheme.

Many vaults use PARA: `Areas/` for ongoing domains, `Projects/` for time-bound
work, `Resources/` for reference, plus an archive folder. Daily notes usually
sit in `Daily/` or `Journal/`, one file per day. If the vault has folders by
these names, use them the same way.

If the vault explains its own distinctions in a note, read that note instead of
guessing.

## 4. Decide where the content goes

- **Quick capture** — a link, a passing thought, a stray idea. Append to today's
  daily note. Do not create a file.
- **Durable knowledge** — an insight, a decision, meeting notes, a writeup, a
  concept worth its own page. Create a file in the right folder from the
  matching template.
- **Ambiguous** — append to the daily note. Most vaults promote daily content
  into permanent notes during review, so a capture today is the normal first
  step, not a lost one.

## 5. Handle today's daily note

Every write touches it. A quick capture goes into it. A new permanent note gets
a link from it. Check that today's file exists before anything else, and create
it if it does not.

Read the most recent existing daily note first. Copy its frontmatter, its header
format, and its prev/next link line if it has one. Do not hardcode a format
here.

Append captures under the heading the vault already uses for them. Find that
heading in recent daily notes. When there is none, append at the end of the file
under a heading you name once and then reuse.

## 6. Create a permanent note

1. Pick the folder.
2. Read the matching template, if the vault has one.
3. Name the file to match the existing files in that folder. Look at them first.
   Do not switch a folder from Title Case to kebab-case or the reverse.
4. Fill in frontmatter per the vault's rules for that note type.
5. Link the new note from today's daily note. This is the default entry point
   whatever the note is about. Link from somewhere else only when the user names
   a different source. When the note comes from an older day's capture, link
   back to that day instead.
6. Search for an existing note with this title or a close synonym before you
   create one. Prefer appending to a near match. Duplicate notes split the links
   that would have led somewhere. `get-or-create-note` runs that search properly
   and returns here only when nothing matches.

## 7. Report

Report the path you wrote to or appended to. Say which conventions you read, and
name anything you had to infer.

## Prose the user will publish

Vault notes are usually private capture and need no check. When a note is headed
somewhere else — a post, a proposal, a letter, anything going out under the
user's name — offer `/voice` before writing it, and `/slop-check` if the note
argues a position. Do not run either unprompted on daily capture.
