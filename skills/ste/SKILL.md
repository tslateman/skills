---
name: ste
description: >
  Write in ASD-STE100 Simplified Technical English — the aerospace controlled
  language for text a reader executes rather than considers. Use for
  procedures, runbooks, error messages, warnings, CLI help, migration steps,
  incident response, and agent-facing instructions (CLAUDE.md, skill bodies,
  tool descriptions). Triggers: "STE", "ASD-STE100", "simplified technical
  english", "write this as a procedure", "make these instructions
  unambiguous". Do NOT use for essays, analysis, ADR rationale, or anything
  that argues a position — STE strips nuance by design. That is /prose.
---

# STE — Simplified Technical English

ASD-STE100 is a controlled English developed for aircraft maintenance documentation. Issue 9 published January 2025: 53 writing rules in 9 sections, plus a dictionary of roughly 900 approved words where each word carries one meaning and one part of speech.

It was designed for a technician whose first language is not English, working against a clock, holding a tool. That reader cannot afford to parse a sentence twice. Every rule follows from that.

## Decide whether STE applies

Ask: **does the reader execute this, or think about it?**

| Reader executes → STE                 | Reader thinks → `/prose`     |
| ------------------------------------- | ---------------------------- |
| Procedures, runbooks                  | Essays, analysis, arguments  |
| Error messages, warnings              | ADR rationale, design docs   |
| CLI help, API reference               | Commit bodies explaining why |
| Migration and incident steps          | Postmortem narrative         |
| Agent instructions, tool descriptions | Anything persuading a reader |

Applying STE to an argument destroys it. An essay drawing an analogy between two systems would come out as a list of true sentences with the reasoning removed. Never reach for this skill to "simplify" prose that carries a claim.

## The rules that carry the weight

| Rule                         | Limit                                                        |
| ---------------------------- | ------------------------------------------------------------ |
| One instruction per sentence | Split every compound step. Two actions, two sentences.       |
| Sentence length              | 20 words maximum in procedures, 25 in descriptive text.      |
| Paragraph length             | 6 sentences maximum, one topic.                              |
| Noun clusters                | 3 words maximum. Break longer ones with prepositions.        |
| Voice                        | Active. Imperative for instructions.                         |
| Tense                        | Simple tenses only. No present perfect.                      |
| Participles and gerunds      | Past participles as adjectives only. No -ing forms as nouns. |
| Articles                     | Keep them. Telegraphic style is banned.                      |
| Vocabulary                   | One word, one meaning. One term per concept, never varied.   |
| Hedging                      | No should/may/might in an instruction. Use must, or delete.  |
| Safety text                  | Warnings and cautions go before the step they protect.       |
| Sequences                    | Vertical lists, not comma-separated runs.                    |

Rule numbers live in the official PDF. Cite the number only when reading from that document — never reconstruct one from memory.

## The dictionary

Roughly 900 approved words, each with a single meaning and part of speech. **Do not bundle or reproduce it.** ASD owns the copyright; the standard is free to download but not to redistribute.

Two escapes keep domain vocabulary legal:

- **Technical names** (rule 1.5) — nouns for parts, systems, tools, and materials are approved without appearing in the dictionary. `kubelet`, `worktree`, `reservation` all pass.
- **Technical verbs** (rule 1.12) — verbs describing a domain action qualify the same way. `rebase`, `provision`, `deserialize` all pass.

Without the dictionary open, approximate it: pick the shortest common word, hold one term per concept across the whole document, and keep a project term list so the next writer holds the same terms.

## Workflow

1. Classify the text as procedure or description. The limits differ.
2. Split every compound instruction into one action per sentence.
3. Rewrite to imperative and active voice.
4. Enforce the counts: 20 or 25 words, 6 sentences, 3-word noun clusters.
5. Fix vocabulary: one term per concept, hedging modals removed, clusters expanded.
6. Move every warning and caution ahead of the step it protects.
7. Reread as the intended reader — second language, under time pressure, hands occupied.

## Check the counts mechanically

```bash
prose-scan ste FILE               # 20-word procedural limit
prose-scan ste FILE --descriptive # 25-word limit
```

`prose-scan` ships at `bin/prose-scan` in this repo. Put it on your `PATH`, or
invoke it by path. It counts what counting settles: sentence length against the active limit, paragraphs over 6 sentences, hedging modals, present perfect, passive constructions, and gerunds used as nouns. Exit code is 1 on any violation.

It does not check noun clusters or one-word-one-meaning. Both need part-of-speech judgment that a regex gets wrong more often than right, so they stay with the reader.

## What STE does not fix

It does not find missing steps, wrong ordering, or false content. A procedure can satisfy all 53 rules and still be wrong. Verify the content first, then constrain the language.

It also removes arguments rather than clarifying them. Nuance, hedging, and conditional reasoning are the targets, so text that needs them comes out worse.

## Relation to the other writing skills

| Skill         | Mode                   | Scope                               |
| ------------- | ---------------------- | ----------------------------------- |
| `/prose`      | Rewrite by subtraction | Any prose a human reads for meaning |
| `/slop-check` | Score and report       | Any prose published under your name |
| `/ste`        | Constrained generation | Text a reader or agent executes     |

A published benchmark measured 72.9% fewer STE violations per 100 words across 6 Claude models and 8 tasks when the standard was applied, with output tokens falling on every model. Treat the direction as real and the number as vendor-reported. The same repo's FAQ concedes that a single system-prompt line recovers much of the effect, so the value here is the rule set and the applies/does-not-apply boundary above, not novelty.

## Getting the standard

- Specification, free since Issue 6 (2013): <https://www.asd-ste100.org/>
- Boeing Simplified English Checker — commercial tooling, if enforcement ever needs to be mechanical

## See Also

- `/prose` — for prose that argues rather than instructs
- `/slop-check` — scoring; STE compliance and slop score measure different things
