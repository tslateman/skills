# Scent and Landmarks

_Core concepts from Kevin Lynch's_ The Image of the City _(1960), Arthur &
Passini's_ Wayfinding _(1992), and Pirolli & Card's information foraging theory
(Xerox PARC, 1995–1999)._

## Lynch: The Legible Environment

Lynch interviewed residents of Boston, Jersey City, and Los Angeles, asking each
to draw their city from memory. The drawings converged on five element types —
and the cities people drew confidently were not the beautiful ones or the
orderly ones. They were the **legible** ones: environments whose parts could be
recognized and organized into a coherent pattern.

Legibility is not simplicity. A legible city can be large and intricate,
provided its structure declares itself as you move through it.

### The Five Elements

- **Paths** — the channels along which people move. The dominant element; people
  organize everything else relative to the paths they travel.
- **Edges** — linear boundaries: shores, walls, breaks in continuity. Edges that
  can be crossed at known points unify; edges that cannot divide.
- **Districts** — medium-to-large sections with a recognizable shared character.
  People know when they have entered one.
- **Nodes** — strategic points a traveler can enter: junctions, crossings,
  concentrations. Decision points.
- **Landmarks** — external reference points, not entered but sighted. Their value
  is singularity: one memorable thing against a contrasting background.

### Imageability

Lynch's term for the quality that makes an environment evoke a strong mental
image. Three components:

1. **Identity** — the object is distinguishable from its surroundings
2. **Structure** — its spatial relation to the observer and other objects is clear
3. **Meaning** — it holds practical or emotional significance for the observer

A file with a distinctive name, an evident position in the hierarchy, and a job
the reader cares about is imageable. Miss one and the file evaporates from
memory the moment it closes.

## Arthur & Passini: Wayfinding as Decision-Making

Arthur and Passini reframed wayfinding from "spatial orientation" to
**problem-solving**. A traveler executes a loop:

1. **Decision-making** — form a plan of action
2. **Decision execution** — translate the plan into behavior at the right place
3. **Information processing** — read the environment to confirm or revise

The critical claim: wayfinding fails at the point where a decision must be
made and the environment supplies nothing to decide with. Signage placed where
there is no decision is waste; a decision point with no signage is a stall.

**Consequence for systems.** Documentation effort should concentrate at decision
points — the directory where a reader must choose a subtree, the interface where
several implementations exist, the entry file where several flows diverge.
Documenting a leaf file that admits only one next step is low value.

Their second theme is **progressive disclosure of destination**. A traveler does
not need the full route at the start; they need enough to make the next decision
correctly, and confirmation after each. An orientation document that dumps the
entire architecture serves nobody, because no reader holds a decision that
large.

## Pirolli & Card: Information Foraging

Optimal foraging theory, borrowed from ecology, applied to how people seek
information. An animal balances energy gained against energy spent; an
information seeker balances value found against time spent.

### Information Scent

The core construct. **Scent** is the reader's estimate of the value and cost of a
path, formed from proximal cues — a link label, a file name, a heading — before
committing to it.

Three empirical findings that matter for systems:

1. **People act on scent, not on content.** The decision to open a file is made
   entirely from its name and context. A superb file behind a weak name goes
   unread.
2. **People abandon a path when scent weakens.** Not when it dead-ends — when it
   stops improving. Two vague hops in a row and the reader restarts.
3. **Scent degrades with distance.** Cues predicting content three levels down
   are weaker than cues predicting content one level down. Deep hierarchies
   demand stronger naming at every level, which is why depth costs more than it
   appears to.

### Enrichment vs. Foraging

Foragers can either search harder in the current patch or improve the patch
itself. Pirolli calls the second **enrichment**.

Most documentation effort goes to foraging aids — search, indexes, better
grep. Enrichment is renaming the patch so the search is unnecessary. Enrichment
compounds; foraging aids do not.

## Brown: The Principle of Front Doors

From Dan Brown's _Eight Principles of Information Architecture_ (2010):

> Assume at least half of your visitors will arrive at some page other than the
> home page.

Brown's implication is that every page must carry enough context to orient a
reader who skipped everything above it: what site this is, what section, and how
to get to the rest.

In a codebase the ratio is more extreme. Readers arrive by stack trace, grep,
diff, code review link, and search — almost never by walking the tree from the
root. Every file is a front door, and the ones that fail are the ones written as
if the reader had already read the README.

## Applying the Three Together

| Symptom                                     | Diagnosis                            | Source           |
| ------------------------------------------- | ------------------------------------ | ---------------- |
| "I don't know what part of the app this is" | District without a landmark          | Lynch            |
| "I opened four files to find the right one" | Weak scent at a node                 | Pirolli & Card   |
| "The docs explain everything but this"      | Signage away from the decision point | Arthur & Passini |
| "I understand the file, not the system"     | Missing structure, present identity  | Lynch            |
| "New people re-ask the same question"       | A decision point with no signal      | Arthur & Passini |
| "Nobody reads the README"                   | Readers never enter through it       | Brown            |

## Further Reading

- Lynch, _The Image of the City_ (MIT Press, 1960) — ch. 3 on the five elements
- Arthur & Passini, _Wayfinding: People, Signs, and Architecture_ (1992)
- Pirolli & Card, "Information Foraging," _Psychological Review_ 106(4), 1999
- Brown, "Eight Principles of Information Architecture," _Bulletin of ASIS&T_ 36(6), 2010
