---
name: slop-check
description: >
  Score a finished draft for AI writing tells and report line-anchored
  findings. Detection and scoring only — it judges prose, it does not
  rewrite it. Use before publishing anything that goes out under your
  name: posts, PR descriptions, docs, external email, vault notes headed
  for an audience. Triggers: "slop check", "does this read as AI",
  "score this draft", "check for LLM tells", "would anyone know I wrote
  this". Do NOT use to tighten or rewrite a draft — that is /prose.
---

# Slop Check — Score a Draft for AI Tells

`/prose` writes and cuts. This skill judges. It reads a finished draft, scores it, and hands back line-anchored findings for `/prose` to fix. Keep the modes separate: scoring while rewriting produces a draft that scores itself well.

## Run the horoscope test first

**Could anyone have written this, for anyone?**

If yes, stop scanning for patterns. Generic writing passes every vocabulary check ever written, and no word swap rescues it. A failed horoscope test sets the verdict floor at **Revise** no matter what the score says, and the finding to report is the argument, not the prose.

A draft passes when it contains at least one of: a claim the author would have to defend, a specific system or number, or a position someone could disagree with.

## Score

Count per 1000 words. Scale thresholds proportionally for shorter pieces.

| Finding                                     | Points |
| ------------------------------------------- | ------ |
| Structural tell, first of its kind          | +3     |
| Structural tell, repeat of the same pattern | +1     |
| Lexical tell                                | +1     |
| Cluster (3+ lexical tells in one para)      | +2     |
| Horoscope test failure                      | +5     |

Structure counts triple because it is harder to miss and harder to fake. A writer who reaches for "delve" once has a vocabulary habit; a writer whose every paragraph runs three sentences of equal length is not writing.

Repeats count once at full weight and +1 after, so **variety of tells drives the verdict, not volume of one tic**. Five different structural patterns score 15 and earn a rewrite. The same pivot five times scores 7 — a verbal habit in a sound argument, which is a revision. Report every instance either way; the author needs the full list to fix them.

| Score | Verdict | Action                                                                    |
| ----- | ------- | ------------------------------------------------------------------------- |
| 0–5   | Ships   | Report the score and stop. Do not manufacture findings.                   |
| 6–12  | Revise  | Hand the named findings to `/prose`.                                      |
| 13+   | Rewrite | The draft is unedited generation. Restate the argument and start from it. |

## Structural tells (+3)

| Pattern                | How it shows                                                 | Fix                                            |
| ---------------------- | ------------------------------------------------------------ | ---------------------------------------------- |
| Contrastive pivot      | "Not just X — it's Y", "This isn't A, it's B"                | State what it is. Cut the negation setup.      |
| Rule of three          | Tricolons and three-item lists in every section              | Use the number of items the argument has.      |
| Uniform rhythm         | Every sentence 15–20 words, every paragraph 3 sentences      | Vary length. Let one sentence land short.      |
| Symmetrical bullets    | Every bullet the same length, most with a bold-colon prefix  | Break the symmetry or write prose instead.     |
| Fragment spam          | Short fragments used as emphasis. Repeatedly. Like this.     | Rejoin into sentences. Keep at most one.       |
| Manufactured voice     | "Here's the thing." "Let's be honest." "I'll be blunt."      | Delete. The bluntness should be in the claim.  |
| Throat-clearing opener | "When we think about X, it's important to consider..."       | Start at the verb.                             |
| Hedged authority       | "It's worth noting that", "It's important to remember"       | Drop the hedge. State the point.               |
| Restating summary      | A closing paragraph that repeats the body in shorter form    | Cut it, or replace with the transferable rule. |
| Scaffolding leak       | **Bold-colon:** prefixes carrying the structure of the piece | Let the sentences carry it.                    |

The first four overlap `/prose`'s LLM-ism catalog by design — that skill fixes them, this one counts them.

## Lexical tells (+1)

There is no banned-word list here, deliberately. Blacklists decay as models route around them and they fire constantly on legitimate technical prose.

Apply Strunk's test instead: **does the word do work in this sentence?** Remove it. If the meaning survives intact, count it.

Usual suspects worth checking against that test — never counted on sight: delve, tapestry, leverage, seamless, robust, landscape, unlock, unleash, elevate, pivotal, transformative, game-changer, streamline, empower, navigate, harness, crucial.

Half of these are load-bearing in some domains. "Leverage" in a finance note, "robust" about error handling, "landscape" in an ecosystem map — these carry meaning. Count the decorative use, not the word.

## Never counted

**Em dashes.** The tell is dead and the crackdown now produces more damage than the signal ever caught — NeurIPS 2026 desk-rejected 178 position papers behind detector scores that em-dash density helped inflate. Report em-dash density as an uncounted note when it exceeds roughly one per paragraph, so the author can decide. Never score it, and never strip em dashes as a fix.

Also uncounted:

- Anything inside code blocks, quoted material, command output, or API names
- Deliberate parallelism in specs, checklists, and reference tables, where symmetry is the point
- Short sentences in a draft that varies its rhythm; only sustained fragment use is a pattern
- Domain terms of art, however overused they are elsewhere

## Never scored at all

Two sibling skills mandate patterns this one penalizes. Scoring their output measures compliance with the wrong standard.

| Source        | Conflict                                                                               |
| ------------- | -------------------------------------------------------------------------------------- |
| `/ste` output | The 20-word cap and one-instruction-per-sentence rule produce uniform rhythm by design |
| `/bro` output | Rule 4 requires "basically…", "ok so…" — this skill calls that manufactured voice      |

Decline the scan and say why. A procedure and a plain-language re-explanation are judged by whether the reader can act on them, not by whether they read as authored.

## Output

Lead with the verdict. Anchor every finding to a line.

```
Slop score: 8 / Revise
Horoscope test: pass

Structural (+3 each)
- L12 contrastive pivot — "This isn't a tooling problem, it's a boundary problem"
- L31 restating summary — final paragraph repeats L8-L14

Lexical (+1 each)
- L19 "seamlessly" — remove, sentence unchanged
- L22 "robust" — decorative here, unlike L40

Uncounted
- em dash: 9 across 6 paragraphs
```

When the score lands at Ships, say so in one line and stop. A detector that always finds something is not measuring anything.

## Run the scanner first

```bash
prose-scan slop FILE          # add --json for machine-readable output
```

`prose-scan` ships at `bin/prose-scan` in this repo. Put it on your `PATH`, or
invoke it by path.

It settles the mechanical layer: contrastive pivots, throat-clearing openers, hedged authority, manufactured voice, scaffolding leaks, and sentence-length spread — with repeat capping already applied. It reports lexical suspects unscored, because deciding whether "leverage" is decorative needs a reader. Exit code is 1 above the Ships threshold, so it can gate a commit.

Start from its score, then add what only judgment catches: the horoscope test, rule of three, restating summaries, and whether a flagged construction is doing real work. The scanner never lowers a verdict — it finds a floor.

Cap rewrites at one retry. By the third pass a model stops removing slop and starts substituting fresh slop.

## When not to use

- Tightening, cutting, or rewriting a draft → `/prose`
- Commits, scratch notes, and anything only you read. Slop matters for prose someone else reads under your name.
- Visual and layout slop in generated HTML → `html-style`

## See Also

- `/prose` — the fixing half; findings from here go there
- `html-style` — the same judgment applied to documents rather than sentences
