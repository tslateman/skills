---
name: prose-recipe
workers: 3
parallel: true
---

# Prose — Agent Recipe

Sharpening prose decomposes into three independent lenses. A single editor context-switches between clarity, consistency, and maintainability — often softening cuts to avoid disrupting flow. Parallel workers apply each lens without compromise, then the manager reconciles.

## Decomposition

Split the sharpening pass by editorial concern. Each worker reads the same draft but cuts from a different angle. The three concerns are independent — an LLM-ism has nothing to do with structural consistency, and a bloated transition has nothing to do with naming precision.

## Workers

### Worker 1: Clarity Worker

**Focus:** Cut everything that does not serve the core point.

**Framework:** The "Cut Structure, Keep Substance" and "LLM-ism Catalog" sections from the prose skill.

**Scope boundaries:**

- Handles: throat-clearing openers, contrastive pivots, needless stakes declarations, hedged authority, filler transitions, redundant framing paragraphs, setup sentences
- Does NOT handle: naming consistency, structural organization, technical accuracy

**Prompt template:**

> You are a clarity specialist sharpening prose by subtraction. Your sole concern is removing words that do not serve the core point.
>
> Identify and cut:
>
> - Throat-clearing openers ("When we think about X, we need to consider...")
> - Contrastive pivots ("That's not X — that's Y")
> - Needless stakes declarations ("The stakes are real.")
> - Hedged authority ("It's worth noting that...")
> - Filler transitions and setup paragraphs
> - Restatements of points already made
>
> For each cut, state what was removed and confirm no meaning was lost. If a cut changes meaning, flag it instead of making it.
>
> Ignore naming, structural consistency, and organization — other workers cover those.

### Worker 2: Consistency Worker

**Focus:** Ensure uniform voice, terminology, and structure throughout.

**Framework:** The "Substance Over Voice" and "Trust the Author's Cuts" principles from the prose skill, plus the prose skill's rules on parallel construction and consistent tense.

**Scope boundaries:**

- Handles: inconsistent terminology (same concept called different names), tense shifts, voice shifts (active/passive mixing), uneven heading levels, inconsistent list formatting, mixed tone
- Does NOT handle: cutting for brevity, content accuracy, naming choices

**Prompt template:**

> You are a consistency specialist reviewing prose for uniformity. Your concern is that the same patterns, terms, and voice appear throughout.
>
> Check:
>
> - Does each concept use the same term everywhere? Flag synonyms used for variety when precision requires repetition
> - Is the voice consistent? Active throughout, or passive throughout — not mixed
> - Are parallel structures truly parallel? (lists, headings, sentence patterns)
> - Is the heading hierarchy consistent? Same level for same type of content
> - Is the tone uniform? Technical prose should not shift to casual mid-paragraph
>
> For each inconsistency, show the conflicting instances and recommend which form to standardize on.
>
> Ignore verbosity and content decisions — other workers cover those.

### Worker 3: Maintainability Worker

**Focus:** Ensure the prose remains useful and navigable for future readers.

**Framework:** The "Formulaic structure" pattern from the LLM-ism catalog, plus the prose skill's principles on definite and specific language.

**Scope boundaries:**

- Handles: vague referents ("this", "it" without clear antecedent), buried key points, missing context that future readers need, sections that could be reordered for scannability, overly abstract language where a concrete example would serve
- Does NOT handle: cutting for brevity, voice and tone consistency

**Prompt template:**

> You are a maintainability specialist reviewing prose for future readers. Your concern is whether someone encountering this text in six months can extract what they need quickly.
>
> Check:
>
> - Are key points scannable? Important information should not be buried in paragraph middles
> - Are referents clear? Every "this", "it", and "that" should have an unambiguous antecedent
> - Is abstract language justified? Where a concrete example, name, or number would be clearer, flag it
> - Is the structure navigable? Can a reader skip to the section they need?
> - Is context present? Would a reader without today's conversation understand this?
>
> For each finding, explain what a future reader would misunderstand or miss.
>
> Ignore verbosity cuts and consistency — other workers cover those.

## Synthesis

The manager combines worker outputs into a single sharpened draft:

1. **Apply clarity cuts first.** Remove everything Worker 1 flagged, confirming no meaning loss. Clarity cuts take priority because they reduce the surface area the other workers operate on.
2. **Apply consistency fixes.** Standardize terms, voice, and structure per Worker 2's recommendations. Where a clarity cut created a new inconsistency, resolve it.
3. **Apply maintainability improvements.** Clarify referents, surface buried points, and add concrete specifics per Worker 3's findings. Keep additions minimal — every word added must earn its place.
4. **Resolve conflicts.** If the clarity worker cut a phrase the maintainability worker flagged as needed context, restore it in tighter form. Brevity wins unless meaning is lost.
5. **Run the sharpen test.** Read each sentence in the final draft: can you remove it without losing meaning? If yes, remove it.
