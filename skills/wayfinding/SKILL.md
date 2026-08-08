---
name: wayfinding
description: Audit whether someone dropped into an arbitrary file can tell where they are and where to go next. Use when the user says "onboarding is painful", "agents get lost in this repo", "nobody can find their way around", "add breadcrumbs", or when an /ia pass fixed the structure but readers still stall.
---

# Wayfinding

## Overview

`/ia` asks whether the structure is sound. Wayfinding asks a different question:
standing at an arbitrary point inside that structure, can a reader tell where
they are?

The two come apart. A repository can hold a flawless hierarchy that nobody
navigates, because nobody enters at the top. Readers arrive from a stack trace,
a grep hit, a code review link, or a search result. Agents arrive the same way.
Dan Brown's front-doors principle states it plainly: assume half your visitors
land somewhere other than the home page. In a codebase the figure is closer to
all of them.

Grounded in Kevin Lynch's _The Image of the City_, Arthur & Passini's wayfinding
decision model, and Pirolli & Card's information foraging theory. See
`references/scent-and-landmarks.md` for the full treatment.

## The Four Questions

At any point in the system, a reader needs four answers. Every wayfinding
finding maps to one.

| Question               | Satisfied by                                      | Failure symptom                          |
| ---------------------- | ------------------------------------------------- | ---------------------------------------- |
| **Where am I?**        | Landmarks — a header, module doc, or unique name  | Reader opens three files to orient       |
| **What is here?**      | Preview — the file states its own job             | Reader skims the whole file to find out  |
| **Where can I go?**    | Scent — links and names that predict their payoff | Reader opens candidates at random        |
| **How do I get back?** | Back-links — a path up to the parent context      | Reader restarts from the repository root |

Answer all four at a point and the reader moves. Miss one and they stall or
guess.

## Information Scent

Pirolli and Card's central finding: people follow proximal cues that predict
distal value, exactly as a forager follows a scent trail. They abandon a path
when the scent weakens, and they abandon it _before_ reaching the content.

A name emits scent when a reader can predict what it holds without opening it.

**The three-things test.** From the name alone, name three things inside. If you
cannot, the scent is weak.

| Weak scent   | Why                              | Strong scent          |
| ------------ | -------------------------------- | --------------------- |
| `utils/`     | Predicts nothing; holds anything | `date-parsing/`       |
| `core/`      | Every project's code is core     | `graph-traversal/`    |
| `handlers/`  | Names the shape, not the subject | `webhook-handlers/`   |
| `helpers.ts` | Defined by what it is not        | `retry-backoff.ts`    |
| `misc.md`    | Announces its own incoherence    | `platform-caveats.md` |

Weak scent is worse than a missing name. A reader who sees `utils/` and needs
date parsing must open it to rule it out — and must open it again next time,
because nothing was learned.

## Lynch's Five Elements, Mapped

Lynch found that people build mental maps of cities from five element types. A
codebase carries all five; naming them turns a vague "this repo is confusing"
into specific findings.

| Element       | In a city          | In a system                                            | Audit question                                          |
| ------------- | ------------------ | ------------------------------------------------------ | ------------------------------------------------------- |
| **Paths**     | Streets, transit   | Import chains, call graphs, request flows              | Can a reader follow one path end to end?                |
| **Edges**     | Rivers, walls      | Module and package boundaries, API seams               | Is the boundary visible from inside, or only in config? |
| **Districts** | Neighborhoods      | Subsystems with a shared idiom and vocabulary          | Does each district read as one voice?                   |
| **Nodes**     | Squares, junctions | Entry points — `main`, routers, CLI dispatch, handlers | Are entry points named as such, or buried?              |
| **Landmarks** | Towers, monuments  | The one file everyone knows and returns to             | Does the district have one, and is it obvious?          |

A district without a landmark is the most common finding. Readers hold no anchor
in that region and re-derive their bearings on every visit.

## The Cold-Entry Audit

The core procedure. Simulate arrival rather than reasoning about the structure
from above.

### 1. Sample entry points

Pick 5–10 files the way a real reader arrives, not the way a maintainer would
choose:

- Files named in recent stack traces or error logs
- Top grep hits for the project's most common domain term
- Files changed in the last handful of commits
- The deepest file in the tree
- A file chosen at random from the largest directory

### 2. Simulate cold entry

For each, read **only that file** — no parent README, no directory listing, no
prior context. Then answer the four questions from what the file itself
provides.

### 3. Score

| Score | Meaning                                                     |
| ----- | ----------------------------------------------------------- |
| **3** | All four questions answered from this file alone            |
| **2** | Oriented, but one question needs a second file              |
| **1** | Knows what the file does; no idea where it sits             |
| **0** | Cannot tell what the file does or what system it belongs to |

Report the distribution, not the average. A repository with ten 3s and three 0s
has a specific district problem; a uniform field of 1s has a systemic one.

### 4. Trace the exits

From each sampled file, name the next file a reader would need. Then check
whether the current file gives any signal pointing there. An unsignposted
dependency is a broken path.

## Remedies

Ordered by leverage, highest first.

1. **Give each district a landmark.** One `README.md` per subsystem stating what
   the district owns, its entry point, and its vocabulary. This fixes "where am
   I" for every file inside at once.
2. **Rename the weak-scent nodes.** A `utils/` split into two named directories
   pays off on every future search. Hand the term choices to `/lexicon`.
3. **Open files with their own job.** A one-line module docstring stating the
   file's responsibility answers "what is here" without a full read. Note that
   this is orientation, not commentary — it states responsibility, never
   implementation.
4. **Name entry points as entry points.** `main`, `cli`, `routes`, `server` beat
   clever names. Nodes should announce themselves.
5. **Add back-links where the path up is non-obvious.** A generated file should
   name its generator; a deep config should name what consumes it.
6. **Make edges visible from inside.** If a boundary matters, the files on either
   side should say so — through placement, naming, or an explicit interface
   module.

## Output Format

```markdown
## Wayfinding Audit

### Scores

| File | Where am I? | What is here? | Where can I go? | How do I get back? | Score |
| ---- | ----------- | ------------- | --------------- | ------------------ | ----- |

### Districts Without Landmarks

- `[path]` — [n] files, no orienting document → Add [what it should state]

### Weak Scent

- `[name]` — [what a reader cannot predict] → `[proposed name]`

### Broken Paths

- From `[file]`, the next stop is `[file]`, unsignposted → [where to add the signal]

### Recommended Order

1. [Highest-leverage remedy and the number of files it orients]
```

## Boundaries

- **`/ia`** designs the structure. Wayfinding assumes the structure is fixed and
  asks whether it can be traversed. Run `/ia` first when the tree itself is
  wrong; run wayfinding when the tree is right and readers still stall.
- **`/zoom-out`** orients one reader in one module, on demand, by building the
  map for them. Wayfinding changes the territory so the map is unnecessary.
  Repeated `/zoom-out` requests in the same region are a wayfinding finding.

## See Also

- `/ia`: structure; wayfinding is orientation within it
- `/zoom-out`: on-demand orientation for a reader; wayfinding is durable orientation for everyone
- `/lexicon`: scent depends on terms; a shared vocabulary makes names predictive
- `/naming`: supplies the replacement names a scent finding calls for
- `skills/FRAMEWORKS.md`: Full framework index
