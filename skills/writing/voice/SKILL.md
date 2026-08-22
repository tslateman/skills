---
name: voice
description: >
  Check whether a draft sounds like you, not merely whether it sounds human.
  Compares prose against observable habits derived from your own writing. Use
  before publishing anything under your name where authorship matters: letters,
  proposals, posts, notes to colleagues. Triggers: "voice check", "does this
  sound like me", "is this my voice", "would anyone know I wrote this".
  Distinct from /slop-check, which tests genericness — a draft can be specific,
  defendable, and still sound like a competent stranger.
---

# Voice — Does This Sound Like You

`/slop-check` asks whether anyone could have written this. This skill asks whether **you** wrote it. Those come apart: prose can pass every slop test — specific, concrete, defendable — and still read as a capable outsider writing about your work.

## Your traits file

This skill judges a draft against a corpus you supply. It does not ship anyone's traits.

Find the traits file in this order. Stop at the first one that exists.

1. `$VOICE_TRAITS`
2. `${XDG_CONFIG_HOME:-$HOME/.config}/voice-traits.md`
3. `$HOME/.claude/voice-traits.md`, the path earlier versions used

When none exists, derive it first (below) and write it to entry 2. A voice check against no corpus is guesswork with a confident format.

Keep the file outside version control. It quotes your private writing, and it will name people.

## Deriving the corpus

Sample your own unedited prose — letters, journal entries, sent messages, anything written without an audience in mind. Twenty samples is enough to see habits; five is not.

```bash
find "${VOICE_CORPUS:-$HOME/Documents}" -name '*.md' -newermt '-2 years' \
  | while IFS= read -r f; do printf '%s\t%s\n' "$(wc -w <"$f" | tr -d ' ')" "$f"; done \
  | sort -rn | head -20
```

Two cautions when assembling the corpus:

- **Metadata does not establish authorship.** Notes marked as your own routinely contain pasted model output. Identify your writing by reading it, not by its frontmatter.
- **Polished documents are the worst corpus.** Anything edited for an audience has had the tells sanded off. Rough, dated, private writing carries the most signal.

Voice moves. Re-derive before a check that matters rather than trusting a file written a year ago.

## What to look for

Ten categories of observable habit. Fill each with your own instances, quoted verbatim, when building the traits file.

| #   | Category                    | The question                                                                          |
| --- | --------------------------- | ------------------------------------------------------------------------------------- |
| 1   | **Metaphor discipline**     | Do you carry one figure all the way through, or reach for several?                    |
| 2   | **Syntactic tics**          | Dropped subjects, fragments, run-ons — what does your sentence-opening look like?     |
| 3   | **Stance moves**            | Do you concede against yourself mid-argument, or land every claim at full confidence? |
| 4   | **Polish level**            | Do rough edges survive — malapropisms, half-idioms — or is everything sanded?         |
| 5   | **Specificity habits**      | Do numbers arrive bare, or with the constraint that makes them real?                  |
| 6   | **Question forms**          | Genuine forks that split a situation, or rhetorical questions you answer at once?     |
| 7   | **Rhythm**                  | Long build then a short verdict? Even paragraphs? Front-loaded conclusions?           |
| 8   | **Audience shifts**         | What changes when you address a group rather than one reader?                         |
| 9   | **Punctuation fingerprint** | Em dashes, hyphens, semicolons, parentheses — which do you actually reach for?        |
| 10  | **Register by context**     | Do work and personal writing run as one style or two?                                 |

Categories 2 and 9 are the fastest tells in both directions. Models rarely drop subjects and heavily favor em dashes, so a draft that matches your syntax and your punctuation is hard to fake and hard to counterfeit.

Category 9 is where this skill and `/slop-check` deliberately diverge. There, punctuation is a dead signal — every writer uses em dashes. Here it is authorship evidence, because the question is not "is this human" but "is this _you_."

## Output

```text
Voice: recognizable / plausible / stranger

Present
- extended metaphor — queue back pressure held across all six sections
- named specifics — the ingest gateway, the retry budget

Missing
- no dropped subjects anywhere in 460 words
- no self-undercutting; every claim lands at full confidence
- em dash x9 against a usual hyphen-and-parenthesis habit

Sounds like a stranger
- L23 "Move ownership upstream without moving the control function upstream
  and you have not shifted left" — correct, and nothing in the corpus
  builds a sentence this way
```

Three verdicts only. **Recognizable** — a reader who knows your writing would place it. **Plausible** — nothing contradicts, nothing confirms. **Stranger** — competent prose by someone else.

Cite the trait number and quote the evidence. A verdict without quoted lines is an impression.

## The failure mode to refuse

Do not inject typos, forced casualness, or manufactured roughness to raise the score. Salting a draft with "basically" and a deliberate misspelling produces something worse than clean prose: a forgery with a tell. Writers doing this at scale are creating a new detectable signature, not escaping the old one.

The fix for a stranger verdict is structural — find the metaphor the author would have reached for, cut the claim they would have conceded, add the constraint they would have attached to the number. If none of that is available, the honest report is that the draft is not theirs and cannot be made theirs by editing.

## Relation to the other writing skills

| Skill         | Question                              |
| ------------- | ------------------------------------- |
| `/prose`      | Is it clear and as short as it can be |
| `/slop-check` | Could anyone have written this        |
| `/voice`      | Did **you** write this                |
| `/ste`        | Can the reader execute it             |
| `/bro`        | Can the reader understand it          |

Run `/slop-check` first. A draft that fails on genericness will fail here too, and its findings are cheaper to fix.

## See Also

- `/slop-check` — genericness; this skill assumes it already passed
- `/prose` — clarity; a recognizable voice can still be overlong
