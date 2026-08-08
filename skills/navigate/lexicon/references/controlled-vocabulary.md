# Controlled Vocabulary

_Core concepts from ANSI/NISO Z39.19 (Guidelines for the Construction, Format,
and Management of Monolingual Controlled Vocabularies) and Eric Evans's
ubiquitous language._

## Why Control Vocabulary

Natural language offers many words for one concept and many concepts for one
word. Retrieval systems built on uncontrolled language fail in two directions:
searches miss relevant content (synonyms scattered) and return irrelevant
content (homographs conflated).

A controlled vocabulary trades expressive freedom for retrieval reliability. The
cost is real — writers lose their preferred word. The benefit is that anyone,
including a future maintainer or an agent, can find everything about a concept
by searching one term.

## Four Vocabulary Types

Z39.19 defines an escalating ladder. Choose the lightest type that solves the
problem; each step up costs maintenance.

### 1. Synonym Ring

A set of terms treated as equivalent for retrieval. No preferred term, no
hierarchy. Searching any member returns content tagged with any other.

Use when: you cannot control what writers say, but you can control what search
does. A synonym ring is the cheapest useful vocabulary.

Example: `{job, task, run, execution}` — a grep alias or search expansion that
covers all four.

### 2. Authority File

A list of preferred terms with cross-references from rejected variants. Adds the
`USE` / `USE FOR` relationship.

Use when: you can enforce which term appears in new writing, and need a single
canonical form per concept.

```text
job
  UF task
  UF run
  UF execution

task
  USE job
```

This is the level most software projects need. It is a `GLOSSARY.md`.

### 3. Taxonomy

Preferred terms arranged in a hierarchy — broader term (BT) and narrower term
(NT) relationships.

Use when: concepts nest, and readers benefit from browsing from general to
specific.

```text
memory
  NT episode
  NT checkpoint
  NT topic
```

### 4. Thesaurus

A taxonomy plus associative relationships (RT — related term) and scope notes
(SN) that state boundaries.

Use when: concepts relate laterally as well as hierarchically, and boundaries
between near-synonyms need explicit statement.

## Standard Relationship Notation

| Code  | Name          | Meaning                                          |
| ----- | ------------- | ------------------------------------------------ |
| `USE` | Use           | This term is rejected; use the one named         |
| `UF`  | Use for       | This preferred term covers the rejected variants |
| `BT`  | Broader term  | The parent concept                               |
| `NT`  | Narrower term | A child concept                                  |
| `RT`  | Related term  | Associated but neither broader nor narrower      |
| `SN`  | Scope note    | Where the term applies and where it stops        |

The scope note carries more weight than the definition. A definition says what a
term means; a scope note says what it excludes — which is what a reader deciding
between two near-synonyms actually needs.

## Term Selection Rules

Z39.19 selection guidance, adapted for software:

1. **Prefer nouns** — concepts are things. Reserve verbs for operations.
2. **Prefer singular for countable things, plural for collections** — `episode`
   the concept, `episodes` the table.
3. **Prefer the term users say, not the term the implementation implies** — a
   `sync` that reconciles is still called `sync` if everyone says `sync`.
4. **Avoid abbreviations unless the abbreviation is the ubiquitous form** — `API`
   yes, `cfg` no.
5. **Spell out the ambiguous, disambiguate the unavoidable** — when one word must
   carry two meanings across boundaries, qualify both: `http-session` and
   `work-session`, never a bare `session` on either side.

## Ubiquitous Language

Evans's addition to the picture: the vocabulary is not a retrieval aid bolted on
after the fact. It is the same language spoken by domain experts, written in the
code, and used in conversation — one language, no translation layer.

Three consequences:

- **A translation layer is a defect.** If developers say "record" and the
  business says "claim", one of them is wrong and the mismatch will produce bugs
  at the seam.
- **Vocabulary change is model change.** When a term stops fitting, the model
  underneath it has moved. Renaming without revisiting the model buries the
  signal.
- **Bounded contexts scope the vocabulary.** One term may legitimately mean two
  things in two subsystems, provided the boundary is explicit and translation
  happens at the seam. Collisions are only defects _within_ a context.

## Governance

A vocabulary decays without an owner and a cadence.

- **Owner** — one person or one file holds the authority. Distributed ownership
  produces distributed drift.
- **Admission** — a new term enters when it names a concept that existing terms
  cannot express without a qualifier.
- **Retirement** — a term retires to `UF` status, never to nothing. Deleted
  variants strand every reader holding the old word.
- **Cadence** — review at the same rhythm the domain changes. A stable domain
  needs a yearly pass; an evolving one needs a pass per release.

## Further Reading

- ANSI/NISO Z39.19-2005 (R2010) — the standard itself, free from NISO
- Evans, _Domain-Driven Design_ (2003) — ch. 2 on ubiquitous language, ch. 14 on bounded contexts
- Hedden, _The Accidental Taxonomist_ (3rd ed., 2022) — practical term-selection guidance
