---
name: ia
description: Evaluate and improve how information is organized for findability. Use when the user asks to "organize this", "restructure docs", "improve navigation", "where should this go", "review file structure", or when documentation grows beyond a single page.
---

# Information Architecture

## Overview

Information architecture is the structural design of shared information environments. When someone asks "where does this go?" or "I can't find anything", that's an IA problem.

Grounded in Rosenfeld, Morville & Arango's _Information Architecture_ (4th ed.) and the Diataxis documentation framework. See `references/rosenfeld-morville.md` for the core systems and `references/organizing-principles.md` for LATCH, Brown's eight principles, and Morville's triad.

**Three layers, before the systems.** Morville separates an information space into ontology (what the entities mean and how they relate), taxonomy (how they are grouped), and choreography (how the space behaves as people move through it over time). Most IA effort lands on taxonomy. When a space audits clean structurally and still feels wrong, the defect sits in one of the other two: confusion about what things mean is ontology, confusion about what to do next is choreography.

## The Four Systems

Every information space has four structural systems; evaluate each when reviewing or designing. `references/rosenfeld-morville.md` carries the full treatment (schemes, structures, label types, navigation modes, search components); this is the working summary.

1. **Organization**: how content is grouped. Choose one primary scheme per level (exact: alphabetical, chronological, geographic; ambiguous: by topic, task, audience). Mixing schemes at one level confuses navigation.
2. **Labeling**: what things are called. Describe content, not container ("Authentication", not "Section 3"); match the words users search for; introduce jargon inside, not at top levels.
3. **Navigation**: how people move. Global (always visible), local (within a section), contextual (inline links), supplemental (index, site map, search). Three clicks to any content, or flatten the hierarchy.
4. **Search**: how people find without browsing. Grep-friendly file names (`signal-contract.md`, not `doc-7.md`), headings that match search terms, synonym cross-references, consistent metadata.

### LATCH: The Five Ways

Wurman's claim is that information admits exactly five organizing bases. When a structure feels arbitrary, name which one it uses.

| Way           | Basis                     | Best for                                  | Fails when                               |
| ------------- | ------------------------- | ----------------------------------------- | ---------------------------------------- |
| **Location**  | Physical or logical place | System topology, file paths, spatial data | The reader does not know where to look   |
| **Alphabet**  | Name                      | Large reference sets with known names     | The reader knows the need, not the name  |
| **Time**      | Sequence or date          | Changelogs, processes, tutorials          | Recency does not track relevance         |
| **Category**  | Kind or similarity        | Browsing, discovery, most documentation   | Categories overlap or boundaries blur    |
| **Hierarchy** | Magnitude or importance   | Rankings, severity, priority, size        | Items resist a single ordering dimension |

Location, Alphabet, and Time are the exact schemes; Category and Hierarchy are the ambiguous ones. **One per level.** A directory sorted by category whose siblings are sorted by time forces the reader to hold two models at once.

### Taxonomy Construction

When reviewing a project's organization, evaluate whether the taxonomy is sound:

1. **Can every item be placed in exactly one group?** If not, categories
   overlap. Tighten the scheme.
2. **Are items at the same level comparable in scope?** "utils" alongside
   "authentication" mixes granularity.
3. **Does depth exceed three levels?** Over-splitting signals the taxonomy
   is too fine-grained. Flatten by merging related categories.
4. **Can a newcomer predict where to find something?** If not, the grouping
   reflects how the author thinks, not how readers seek.
5. **Can a newcomer predict where to put something new?** If not, the scheme
   has gaps or ambiguous boundaries.

**Card sort heuristic:** If three people disagree on where an item belongs, the
categories are ambiguous. Rename or restructure until placement is obvious.

## Brown's Eight Principles

The four systems analyze an existing space. Brown's eight principles design one. Reach for the two or three that name the failure at hand rather than scoring all eight.

| Principle                   | Claim                                                     | Violation looks like                                    |
| --------------------------- | --------------------------------------------------------- | ------------------------------------------------------- |
| **Objects**                 | Content has a lifecycle, behavior, and attributes         | Types with different lifecycles filed together          |
| **Choices**                 | Few, meaningful options focused on one task               | Twenty peers in one navigation list                     |
| **Disclosure**              | Preview what is underneath without requiring descent      | Headings that reveal nothing until opened               |
| **Exemplars**               | Name examples of what a category contains                 | "Integrations" with no hint of which                    |
| **Front doors**             | Half your readers skipped everything above                | Pages that assume the README was read                   |
| **Multiple classification** | Offer several ways to browse the same content             | One tree serving three different seeking patterns       |
| **Focused navigation**      | One navigation element, one logical basis                 | A sidebar mixing types, audiences, and lifecycle stages |
| **Growth**                  | Design for the corpus you will have, not the one you have | A scheme that works at five items and dies at fifty     |

Growth is the principle most often skipped and the one that produces the most expensive rework. Ask of every scheme: what happens at ten times this volume?

## Diataxis for Documentation

When the content is documentation, apply the Diataxis framework to classify pages:

| Mode        | Orientation   | Purpose                  | Form           |
| ----------- | ------------- | ------------------------ | -------------- |
| Tutorial    | Learning      | Teach through doing      | Lesson         |
| How-to      | Task          | Solve a specific problem | Recipe         |
| Explanation | Understanding | Clarify concepts         | Discussion     |
| Reference   | Information   | Describe the machinery   | Austere, exact |

**Each page serves one mode.** Mixing tutorial prose into a reference page degrades both. When a page feels unfocused, it likely conflates two modes.

## Review Workflow

### 1. Map the Current State

Inventory the information space:

- List all content (files, sections, pages)
- Identify the primary organization scheme at each level
- Note orphans (content with no navigation path to it)
- Note duplicates (same information in multiple places)
- Note gaps (questions users would ask that have no answer)
- Note the journeys (day-one onboarding, day-thirty reference, 3 a.m. incident) — the same taxonomy traversed three ways

### 2. Evaluate the Four Systems

For each system, ask:

| System       | Question                                              |
| ------------ | ----------------------------------------------------- |
| Organization | Is the grouping scheme consistent at each level?      |
| Labeling     | Can a reader predict content from the label?          |
| Navigation   | Can someone reach any content in three steps?         |
| Search       | Do file names and headings match search terms?        |
| Growth       | Does the scheme survive ten times the current volume? |

### 3. Recommend Changes

Structure output as:

```markdown
## IA Review

### Structure Issues

- [Issue] — [Why it hurts findability] → [Recommended fix]

### Navigation Gaps

- [Missing path] — [Who needs it] → [Where to add it]

### Labeling Problems

- `[current label]` → `[better label]` — [Why]

### Content Gaps

- [Missing topic] — [Who needs it, when]

### Scalability Risks

- [Scheme] — [What breaks at 10x volume] → [Structure that survives]
```

## Common Patterns

### The Growing README

READMEs that accumulate everything eventually fail. When a README exceeds ~200 lines, extract:

- Setup instructions → `docs/setup.md` (how-to)
- Architecture overview → `docs/architecture.md` (explanation)
- API reference → `docs/api.md` (reference)
- Tutorial walkthrough → `docs/tutorial.md` (tutorial)

The README becomes a signpost: project description, quick start, and links to the rest.

### The Flat Docs Directory

A `docs/` with 20+ files at one level signals missing hierarchy. Group by topic or audience, not by creation date.

### The Deep Nest

More than three directory levels for documentation means the taxonomy is too fine-grained. Flatten by merging related pages or promoting important content.

### The Orphan Page

Content exists but nothing links to it. It might as well not exist. Every page needs at least one navigation path leading to it.

## Placement Decision Tree

When deciding where new content goes:

1. **Does similar content already exist?** → Extend it, don't duplicate
2. **What question does it answer?** → Place it where someone asking that question would look
3. **Who needs it?** → Place it in the audience's natural path
4. **What Diataxis mode is it?** → Group it with the same mode
5. **Can you name the parent directory in one word?** → If not, the taxonomy needs work

## See Also

- `/wayfinding`: IA designs the structure; wayfinding asks whether a reader dropped inside it can orient
- `/lexicon`: IA labels one space; lexicon aligns terms across every surface (Morville's ontology layer)
- `/naming`: IA labeling problems are naming problems
- `/design`: IA is structural design for information
- `/prose`: Clear writing makes content findable through scanning
- `skills/FRAMEWORKS.md`: Full framework index
