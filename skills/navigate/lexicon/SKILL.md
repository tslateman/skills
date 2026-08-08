---
name: lexicon
description: Enforce one term, one meaning across code, docs, UI, API, and commits. Use when the user says "we call this three different things", "align our terminology", "build a glossary", "what do we actually mean by X", or when a review surfaces the same concept under multiple names.
---

# Lexicon

## Overview

A lexicon is the controlled vocabulary of a system: the set of terms the project
agrees to use, each bound to one meaning, with every rejected variant pointing
back to its preferred form.

`/ia` governs labels within one information space. A lexicon governs terms
_across_ spaces — code identifiers, documentation prose, UI strings, API field
names, error messages, commit subjects, and memory. When those surfaces drift
apart, readers stop trusting any of them.

Grounded in ANSI/NISO Z39.19 (controlled vocabularies) and Eric Evans's
ubiquitous language. See `references/controlled-vocabulary.md` for the full
vocabulary types and term-record schema.

## The Four Failure Modes

Every terminology problem is one of these. Name the mode before proposing a fix.

| Mode          | Shape                               | Example                                                           | Cost                                     |
| ------------- | ----------------------------------- | ----------------------------------------------------------------- | ---------------------------------------- |
| **Collision** | One term, two meanings              | `session` means both an HTTP session and a work session           | Readers apply the wrong mental model     |
| **Split**     | Two terms, one meaning              | `job`, `task`, and `run` all name the same queued unit            | Search finds a third of what exists      |
| **Drift**     | A term's meaning moved, name stayed | `sync` once meant "copy files", now means "reconcile graph state" | Old docs teach the wrong thing           |
| **Orphan**    | A term lives on one surface only    | Docs say "workspace"; code has no such identifier                 | The concept has no implementation anchor |

Collisions are the most expensive and the least visible. A split announces
itself the moment someone greps. A collision reads as correct until it fails.

## Term Records

A lexicon entry is a record, not a definition line:

```markdown
### Episode

**Definition**: A bounded working session that groups memories into a narrative.

**Scope note**: Distinct from a conversation. One conversation may open several
episodes; an episode may span conversations.

**Use for**: session, work-session, thread
**Broader**: memory
**Narrower**: checkpoint
**Related**: topic, timeline

**Surfaces**: `begin_episode`/`end_episode` tools, `episodes` table,
`/lore capture` output, README "Episodes" section
```

The `Use for` line does the real work. It is the synonym ring: a reader or agent
searching a rejected variant lands on the preferred term instead of concluding
the concept does not exist.

## Workflow

### 1. Extract

Harvest candidate terms from every surface, not just the code:

- Identifiers: type names, function names, module names, database tables, config keys
- Prose: headings and repeated noun phrases in README, docs, ADRs
- Interface: UI labels, CLI subcommands and flags, API fields, error message subjects
- History: commit subjects and issue titles, which record what people say aloud

Note which surface each hit came from. A term appearing on one surface only is
an orphan candidate.

### 2. Cluster

Group terms that appear to name the same concept. Two signals:

- **Co-occurrence** — terms used in the same sentence or the same function tend to be distinct
- **Substitutability** — if swapping the terms leaves every sentence true, they are one concept

### 3. Judge

For each cluster, classify against the four failure modes. State the evidence:
which files, which lines. A terminology finding without a citation is an
opinion.

### 4. Decide

Choose the preferred term per concept. Criteria in priority order:

1. **What domain experts say aloud** — the ubiquitous-language test beats every other consideration
2. **Precision** — the term that admits fewest readings
3. **Incumbency** — the term already carrying the most surface area, if the first two are a tie
4. **Length** — shorter, when everything else ties

Record the rejected variants as `Use for`. Never delete them silently; a
deprecated term that vanishes from the record becomes an orphan again the next
time someone reads old code.

### 5. Enforce

A glossary nobody consults is a dead artifact. Bind it:

- Place it where writers already are — `GLOSSARY.md` at repo root, or a
  `## Vocabulary` section in `CLAUDE.md` if the list is under a dozen terms
- Add deprecated variants to a grep check in lint or CI
- Cite the glossary from the skill or contributing guide that governs writing
- When a term changes, update the record in the same commit as the rename

## Output Format

```markdown
## Lexicon Review

### Collisions — one term, two meanings

- `[term]` means [A] in [file:line] and [B] in [file:line]
  → Keep `[term]` for [A]; rename [B] to `[new term]`

### Splits — two terms, one meaning

- `[a]`, `[b]`, `[c]` all name [concept] ([n] occurrences across [m] files)
  → Preferred: `[a]`. Reason: [criterion]

### Drift — meaning moved, name stayed

- `[term]` documented as [old] in [file], implemented as [new] in [file]
  → Update [surface]; add a scope note

### Orphans — term on one surface only

- `[term]` appears in [surface] with no counterpart in [surface]
  → [Implement it | Retire it | Map it to `[existing term]`]

### Proposed Records

[Term records for every concept the review touched]
```

## When to Reach for This

- Onboarding notes keep needing a translation table
- Search for a concept returns a fraction of the places it lives
- Two subsystems built by different people describe the same data differently
- An API rename is proposed and nobody can say what the field means
- A `/naming` pass keeps surfacing the same word with different intent

## Anti-Patterns

**Glossary as dumping ground.** A list of every noun in the project teaches
nothing. Record terms that carry a decision — where a reader could reasonably
guess wrong.

**Definitions that restate the name.** "Episode: an episode in the system."
A definition must add the constraint the name omits.

**Renaming without a synonym ring.** Rename `task` to `job` and every old
document, issue, and search habit breaks. The `Use for` line is what makes a
rename survivable.

**Enforcing vocabulary on borrowed surfaces.** Third-party APIs and standards
keep their own terms. Map them at the boundary; do not rewrite them inward.

## See Also

- `/naming`: judges whether one name is good; lexicon judges whether a term set is consistent
- `/ia`: labeling within one space; lexicon aligns terms across spaces
- `/wayfinding`: weak terms emit weak scent — a lexicon pass sharpens both
- `skills/FRAMEWORKS.md`: Full framework index
