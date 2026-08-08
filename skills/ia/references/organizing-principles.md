# Organizing Principles

_Wurman's LATCH, Brown's eight principles, and Morville's ontology-taxonomy-
choreography triad. These complement Rosenfeld & Morville's four systems; see
`rosenfeld-morville.md` for those._

## Wurman: LATCH

Richard Saul Wurman, who coined "information architecture," claimed there are
exactly five ways to organize information. Every scheme reduces to one of them.

| Way           | Basis                     | Best for                                   | Fails when                               |
| ------------- | ------------------------- | ------------------------------------------ | ---------------------------------------- |
| **Location**  | Physical or logical place | Spatial data, system topology, file paths  | The reader does not know where to look   |
| **Alphabet**  | Name                      | Large reference sets with known item names | The reader knows the need, not the name  |
| **Time**      | Sequence or date          | Changelogs, processes, history, tutorials  | Recency does not track relevance         |
| **Category**  | Kind or similarity        | Browsing, discovery, most documentation    | Categories overlap or boundaries blur    |
| **Hierarchy** | Magnitude or importance   | Rankings, severity, priority, size         | Items resist a single ordering dimension |

Wurman's point is not that five is a magic number. It is that the choice is
finite and therefore deliberate. When a structure feels arbitrary, name which
of the five it uses. Structures that use none are unorganized; structures that
mix two at one level are the most common IA defect.

**Mapping to Rosenfeld & Morville:** Location, Alphabet, and Time are exact
schemes — objective, mutually exclusive, easy to build and easy to use when the
reader knows what they want. Category and Hierarchy are ambiguous schemes —
harder to build, but the only ones that support browsing and discovery.

**The rule:** one per level. A directory sorted by category whose siblings are
sorted by time forces the reader to hold two models at once.

## Brown: The Eight Principles

Dan Brown's _Eight Principles of Information Architecture_ (Bulletin of ASIS&T, 2010) — heuristics for the design side, where the four systems are the analysis
side.

### 1. Objects

**Treat content as a living thing with a lifecycle, behavior, and attributes.**

Content is not inert text to arrange. Ask what type each thing is, what
attributes it has, and how it changes over time. Types with different lifecycles
belong in different places even when their subjects overlap.

### 2. Choices

**Offer meaningful choices, focused on a particular task, and keep the number
small.**

Hick's law applies. A navigation list of twenty peers is not richer than one of
five; it is unusable. When a level exceeds roughly seven options, either the
level needs subdivision or the options need merging.

### 3. Disclosure

**Show a preview that helps people understand what kind of information is
hidden underneath.**

Progressive disclosure. A section heading, a directory name, or a summary line
should let a reader decide whether to descend — without descending. This is the
design-side twin of information scent.

### 4. Exemplars

**Show examples of the content inside categories.**

A category named "Integrations" tells the reader less than "Integrations —
Slack, GitHub, Linear." Naming two or three members converts an abstract
category into a concrete one, and does so faster than any definition.

### 5. Front Doors

**Assume at least half of visitors arrive somewhere other than the home page.**

Every page carries orientation: what this is, what section it belongs to, and
where the rest lives. In a codebase almost every reader arrives sideways — from
a stack trace, a grep hit, a diff. See `/wayfinding`, which takes this principle
as its starting point.

### 6. Multiple Classification

**Offer several different classification schemes to browse the content.**

People seek the same thing along different dimensions. One reader wants the API
docs by endpoint, another by task, a third by the object being manipulated.
A single tree serves one of them. Tags, indexes, and cross-references serve the
rest without duplicating the content.

### 7. Focused Navigation

**Keep navigation menus simple and never mix different things.**

One navigation element, one logical basis. A sidebar that mixes document types,
audiences, and lifecycle stages in one list teaches the reader that the list has
no meaning.

### 8. Growth

**Assume the content on the site will grow. Make sure the site is scalable.**

Design for the corpus you will have, not the one you have. Ask of every scheme:
what happens at ten times this volume? A structure that works for five items and
collapses at fifty is a structure with a deadline. Growth is the principle most
often skipped and the one that produces the most expensive rework.

**Applying the eight:** they are design heuristics, not a checklist to score.
In review, reach for the two or three that name the failure at hand — most
commonly Choices (too many peers), Front Doors (context assumed), and Growth
(scheme has no headroom).

## Morville: Ontology, Taxonomy, Choreography

Peter Morville's later framing, useful for information spaces that behave rather
than merely sit.

### Ontology — the rules and relationships

What entities exist, what they mean, and how they relate. This is the semantic
layer: definitions, constraints, and the edges between concepts. An ontology
answers "what is a `job`, and what may it be attached to?"

Weak ontology shows up as terminology drift — the same concept under three
names, or one name covering two concepts. `/lexicon` is the working tool here.

### Taxonomy — the arrangement

How those entities are grouped and nested for browsing. This is the layer the
four systems address most directly, and where most IA effort lands.

Taxonomy without ontology produces a tidy structure over incoherent concepts:
the folders look right and the contents contradict each other.

### Choreography — the interaction over time

How the space behaves as people move through it and across channels. Which
sequences are supported, what happens on arrival from elsewhere, how a reader
resumes something started on another surface.

Choreography is the layer most often absent. Documentation is typically designed
as a static corpus, then used as a sequence — onboarding day one, then day
thirty, then the on-call incident at 3 a.m. Those are three journeys through the
same taxonomy, and each needs its own path signposted.

**Diagnostic value of the triad:** when a space feels wrong but the taxonomy
audits clean, the defect is in one of the other two layers. Confusion about what
things mean is ontology; confusion about what to do next is choreography.

## Further Reading

- Wurman, _Information Anxiety_ (1989) — LATCH, and the case for finite schemes
- Brown, "Eight Principles of Information Architecture," _Bulletin of ASIS&T_ 36(6), 2010
- Morville, _Ambient Findability_ (2005) — findability across channels
- Resmini & Rosati, _Pervasive Information Architecture_ (2011) — cross-channel choreography in depth
