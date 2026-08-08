# Information Architecture: For the Web and Beyond

_Core concepts from Rosenfeld, Morville & Arango, 4th edition (2015)._

## Definition

Information architecture is the structural design of shared information
environments — the combination of organization, labeling, search, and navigation
systems within information ecosystems.

## The Three Circles

IA lives at the intersection of three concerns:

- **Context** — Business goals, culture, technology, constraints, politics
- **Content** — Document types, volume, existing structure, ownership, governance
- **Users** — Audience, tasks, needs, information-seeking behavior, vocabulary

Neglect any circle and the architecture fails. Technical documentation organized
by engineering team structure (context-only) ignores how users seek information.
Documentation organized purely by user preference ignores content governance.

## The Four Systems

### Organization Systems

How we group and categorize content.

**Organization schemes** classify content into categories:

- **Exact schemes** — objectively divide information into mutually exclusive
  categories. Alphabetical, chronological, geographical. Easy to design, easy to
  use when you know what you want. Useless for exploration.
- **Ambiguous schemes** — divide information into categories that defy precise
  definition. By topic, by task, by audience, by metaphor. Harder to design,
  often more useful — they support browsing and discovery.

**Organization structures** define relationships between categories:

- **Hierarchy (taxonomy)** — Top-down, broadest to narrowest. The backbone of
  nearly all information architectures. Works when the domain is well-understood.
  Dangers: too broad (overwhelms at top level), too deep (buries content), too
  narrow (forces arbitrary splits).
- **Database model** — Bottom-up, metadata-driven. Each content item has
  attributes (type, date, author, topic). Supports multiple views of the same
  content. Requires consistent metadata discipline.
- **Hypertext** — Network of links between content. Flexible but can disorient.
  Best as a supplement to hierarchy, not a replacement.

**Design principles for hierarchies:**

- Balance breadth and depth. 7±2 items per level is a guideline, not a law.
  Prefer broader over deeper when uncertain.
- Mutually exclusive categories reduce confusion. "Where does this go?" should
  have one obvious answer.
- Use consistent granularity — don't mix high-level concepts with specific
  details at the same level.

### Labeling Systems

How we represent information — the names we give to categories, links, headings,
and index terms.

**Types of labels:**

- **Contextual links** — Hyperlinks within content. Should describe the
  destination, not the action ("Authentication guide" not "Click here").
- **Headings** — Establish hierarchy within a page. Must be scannable — a reader
  skimming headings should understand the page's structure.
- **Navigation labels** — The terms in menus and sidebars. Must be consistent in
  scope and tone across the same level.
- **Index terms** — Keywords, tags, metadata vocabulary. Enable search and
  cross-referencing. Require a controlled vocabulary to be useful.

**Labeling principles:**

- Narrow scope. A label that means everything means nothing. "Resources" and
  "Information" are too broad to help anyone navigate.
- Represent content, not container. "API Reference" describes what's inside.
  "Section 4" does not.
- Match user vocabulary. If users search for "login" and you label it
  "authentication", they won't find it. Use the words people use.
- Consistency. Same term, same meaning, everywhere. If "guide" means a tutorial
  in one place and a reference in another, navigation breaks.

### Navigation Systems

How users move through the information space.

**Embedded navigation** — Built into pages:

- **Global** — Present on every page. Provides orientation ("where am I?") and
  access to major sections. Usually: top nav, sidebar, breadcrumbs.
- **Local** — Within a section. Previous/next links, section table of contents,
  sibling page links.
- **Contextual** — Within content. "See also" links, inline references to related
  topics.

**Supplemental navigation** — Outside the content structure:

- **Site maps** — Complete overview of the architecture. Useful for finding
  content when browsing fails.
- **Indexes** — Alphabetical list of topics with pointers. Cross-cuts the
  hierarchy.
- **Guides** — Curated paths through content for specific audiences or tasks.

**Navigation principles:**

- Every page should answer: Where am I? Where can I go? How did I get here?
- Consistency reduces cognitive load. Navigation that changes structure between
  sections forces re-learning.
- Progressive disclosure. Show the immediate choices; reveal detail on demand.

### Search Systems

How users formulate queries and filter results.

Even small information spaces benefit from searchable content — consistent
naming, grep-friendly file names, meaningful headings.

**Search components:**

- **Query interface** — What the user types. Support natural language, not just
  exact matches.
- **Query language** — Filters, facets, operators. Tags, types, date ranges.
- **Result display** — Sorted by relevance. Enough context to decide which result
  to follow.

**For codebases and documentation:**

- File names are search terms. `signal-contract.md` is findable;
  `doc-7.md` is not.
- Headings are search results. A grep for "authentication" should land on a
  heading that orients the reader immediately.
- Synonyms need bridges. If the concept has multiple names, cross-reference them.
- Metadata (frontmatter, tags) enables programmatic search beyond full-text.

## Information-Seeking Behaviors

Users approach information in different ways. Good IA supports all of them.

- **Known-item seeking** — "I know exactly what I want. Where is it?"
  → Needs: search, consistent naming, indexes
- **Exploratory seeking** — "I think I need something about X. Let me browse."
  → Needs: clear hierarchy, descriptive labels, browsable navigation
- **Exhaustive research** — "I need everything about X."
  → Needs: indexes, cross-references, related content links
- **Re-finding** — "I saw this before. Where was it?"
  → Needs: stable URLs/paths, consistent locations, bookmarkable sections

## Content Modeling

Before designing the architecture, model the content:

- **Content types** — What kinds of things exist? (Tutorials, references, ADRs,
  READMEs, API docs, configuration guides)
- **Attributes** — What metadata describes each type? (Author, date, status,
  audience, topic)
- **Relationships** — How do types relate? (A tutorial references an API; an ADR
  supersedes another ADR)

Content modeling reveals the natural structure. If you model first and design
second, the architecture follows the content rather than forcing content into an
arbitrary structure.

## Evaluation Heuristics

When reviewing an information architecture:

1. **Can a newcomer find what they need without asking someone?** — If not, the
   navigation and labeling have failed.
2. **Can you predict what's inside a section from its label?** — If not, the
   labeling is too vague.
3. **Is there only one obvious place for any given content?** — If not, the
   organization has overlapping categories.
4. **Can you reach any content within three navigation steps?** — If not, the
   hierarchy is too deep.
5. **Are there orphan pages with no path leading to them?** — If so, they're
   invisible.
6. **Do similar items live together?** — If scattered, the grouping scheme is
   inconsistent.
7. **Does the structure match user mental models?** — Organized by team, or by
   task? Users think in tasks.
