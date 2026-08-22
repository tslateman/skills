---
name: get-or-create-note
description: Find the vault note for a URL, title, or topic and open it — or create it when none exists. Use for "do I have a note on this", "get or create a note for this article", "is this already in my vault", "pull up my note on X", or when handed a link and asked whether it has been captured. With no argument, works from what the conversation has been about. Searches first and creates second; delegates the actual writing to obsidian-note.
argument-hint: "[url, note title, or topic — defaults to the conversation's subject]"
---

# Get or Create Note

Answers one question: does a note for this already exist? Searching is the
point. Creating is what happens when the search comes up empty. A vault
fragments quietly, and a near-duplicate is worse than a missing note because it
splits the links that would have led anywhere.

## Find the vault

Use the same resolution `obsidian-note` uses: `$OBSIDIAN_VAULT`, else a
directory containing `.obsidian/`, else ask. Resolve it once.

Read the vault's `CLAUDE.md` or `README.md` if it has one. It names the hub
notes worth checking first.

Search with `rg`. Exclude `.obsidian/` and non-markdown files. Exclude the
vault's archive folder on the first pass, then search it when the earlier passes
find nothing. Identify that folder by name from the top-level listing; common
names are `Archive`, `z.Archive`, and `_archive`.

## Resolve the argument first

Four input shapes, each with its own search. Decide which one you have before
searching.

| Input       | Looks like                      |
| ----------- | ------------------------------- |
| **URL**     | Starts `http://` or `https://`  |
| **Title**   | A phrase that names a note      |
| **Topic**   | A subject, broader than a title |
| **Nothing** | No argument given               |

When the argument could be a title or a topic, run both searches. They are cheap
and they fail differently.

## URL

**Never search for the URL as given.** A vault stores the same source under
different spellings, and an exact-string search reports "no note" for a page
already captured. Reduce the URL to its stable core and search for that.

1. **Extract the identifying part.** For YouTube, the video id — `youtu.be/ABC123`
   and `youtube.com/watch?v=ABC123` are one source under two spellings. For
   everything else, host plus path with `www.` removed.
2. **Drop tracking and position parameters**: `si`, `t`, `feature`, `ref`,
   `fbclid`, `gclid`, and any `utm_*`. These vary per share and never identify
   the source.
3. **Drop the fragment and any trailing slash.**
4. **Search the frontmatter field the vault uses for provenance first.** It is
   usually `source:`. Confirm the field name from a note that has one.
5. **Then search note bodies**, where links that never reached frontmatter live.

A search for the video id alone finds captures the full URL would miss. Prefer
the narrowest substring that still identifies the source.

## Title

Match filenames case-insensitively, and treat spaces, hyphens, and underscores
as equivalent. Vaults accumulate more than one naming style, so a case-sensitive
match reports a false negative.

Search filenames first, then first-level headings, then wikilink targets. A note
referred to as `[[Some Idea]]` from several places may not exist yet, and those
inbound links tell you the note is wanted and where it should link from.

Check whether the vault uses an `aliases:` frontmatter field before relying on
it. Many vaults do not.

## Topic

Search note bodies and `tags:` frontmatter for the subject and its obvious
synonyms.

Then look for a hub note. Many vaults keep one note per topic that indexes the
rest, often in a tags or index folder, or linked from the vault's root note. A
hub is usually the right answer to "do I have anything on this" even when no
dedicated note exists.

Report the hub alongside any specific matches. Appending to a hub often beats
creating a thin new note.

## No argument

Derive the subject from what the conversation has been about — the problem
worked on, the decision reached, the article read — and say what you derived
before acting on it. A wrong inference that creates a note pollutes the vault,
and nothing prompts the user to notice.

Then run the title and topic searches against that subject. If a note is found,
open it; inference that lands on an existing note needs no confirmation. **If
nothing is found, propose the note and wait.** State the title, the folder, and
the one-line summary, and create only once the user agrees.

## Reporting what you found

**One clear match** — read it into context and report its path. Say what it
already covers, so the user can tell whether it answers them or needs extending.
Offer to append rather than assuming.

**Several matches** — list them with paths and a one-line description each, then
stop. Do not guess, and do not create a new note because the matches look
imperfect. Ask which one, or whether none of them fit.

**No match** — say so plainly, name what you searched, and move to creation. "No
note found" after searching only the exact URL is a false negative; state the
reduced form you actually searched for so the user can judge.

## Creating

**Delegate to `obsidian-note`. Do not reimplement it here.** That skill owns the
folder choice, the template, the frontmatter rules, the daily-note link, and the
convention files it reads before writing. Those rules change, and a second copy
of them in this file would drift.

Hand it what the search established:

- the title, matching the convention of the folder it will land in
- the source URL, when the input was a URL
- the existing notes the search turned up, so the new note can link to them
  instead of floating free
- whether this is durable knowledge or a quick capture, since that decides
  new-file-versus-daily-note

A new note that links to nothing is how the fragmentation this skill prevents
gets started. The search results are the link set. Pass them along.

## Gotchas

- **Searching the raw URL** is the failure that matters most. It returns nothing
  for a captured source and sends you straight to creating the duplicate.
- **Stopping at the first pass.** No filename match does not mean no note. Check
  headings, wikilink targets, and body text before concluding.
- **Creating on a near-miss.** A note covering 80% of the subject is a note to
  extend. Fragmenting is the expensive direction, and merging later costs more
  than appending now.
- **Silent inference.** With no argument, always say what subject you derived.
  The user is the only check on that guess.
- **Do not `git commit`**, do not touch `.obsidian/`, and do not rename or move
  existing notes to make a match tidier.
- **Report the path** you opened or created, every time.
