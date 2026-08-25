---
name: cite-or-cut
description: Cite every claim a draft makes or cut it — strategy verdicts, unbounded rankings, invented frameworks, aphoristic closers, and headings that boast. Use when writing or reviewing prose, docs, commits, PR bodies, or research reports, and on "cite or cut", "check my claims", "am I overclaiming", "cut the strategy voice".
---

# Cite or cut

One test. For every sentence asserting something about the world, name the
number, source, or line of code behind it. If nothing backs it, delete it.

This catches what a vocabulary check misses. "The price signal is unclaimed and
defensible" contains no banned word and is still worthless, because the writer
checked three products and wrote a sentence about all of them.

## What to flag

| Pattern                                                                                               | The question it fails                    | Fix                                     |
| ----------------------------------------------------------------------------------------------------- | ---------------------------------------- | --------------------------------------- |
| Strategy verdict: _defensible_, _table stakes_, _the real contest_, _worth defending_, _the position_ | Which competitors did you check?         | Delete. State the fact you did check.   |
| Unbounded ranking: _the only_, _nobody else_, _the first_, _unmatched_, _everyone_                    | Did you look at all of them, or four?    | Bound it to what you read.              |
| Invented framework: a 2×2, quadrant, tier, or axis you coined                                         | Did a source use these axes, or did you? | Delete. The table already said it.      |
| Aphoristic closer: a short flourish ending a section                                                  | Does it carry a fact the section lacks?  | Delete.                                 |
| Boasting heading: _The axis only X covers_, _Where X is exposed_, _Why X wins_                        | Does it name the subject?                | Rename to the subject: "Context cost".  |
| Matched sections: N bold leads of equal length, each closing on a verdict                             | Do the subjects really weigh the same?   | Give each the length its subject earns. |

## The mechanical pass

Run first, then read. It is a trigger list, so judge every hit rather than
cutting on sight.

```bash
grep -nEi 'defensib|table stakes|the (real )?(contest|question|point) is|worth defending|unclaim|moat|nobody else|the only (one|thing|product)|unmatched|is the point|paradigm|north star' "$@"
```

Then read every heading, and read the last sentence of every section. Those two
places hold most of the rest.

## Fixing

Delete first. The tables and numbers around a cut sentence already carry it, so
most cuts need no replacement. Rewrite only when the paragraph loses a fact.

Bound what survives. "Nobody prices context" becomes "the three registries I
read print no token cost." The second is smaller, checkable, and true.

Report what you cut, so the writer can restore anything they can source.

## When to stop

The test terminates: a sentence either names its evidence or it does not, and a
claim fixed once cannot be found again. Passes multiply only when the check
drifts off that question. Three rules hold it there.

**Every finding names one of the six patterns above.** A problem that maps to
none of them is a different job — a factual error, a style preference, a
structural rewrite. Report it and hand it off. Do not fix it here.

**Receipt existence is in scope. Receipt quality is not.** "This claim has a
source" reaches a fixed point. "This claim could have a better source" never
does. Upgrading a citation is worth doing once, deliberately, as its own task.

**Stop when a pass makes no deletions.** This skill removes. A pass that only
rewords is sanding, and the draft gets weaker with each one.

Run it once per draft. Later runs read only the lines that changed.

## Leave alone

- A claim standing next to its number or source.
- A recommendation the writer asked for, stated as a recommendation.
- Plain strong sentences. Evidence-backed confidence is not overclaiming.
