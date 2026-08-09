---
name: maintainability
description: Judge whether code will stay cheap to change, applying Ousterhout's A Philosophy of Software Design, Fowler's Refactoring, and Martin's Clean Code. Use when you ask "will this age well", "is this maintainable", "maintainability review", or when weighing module boundaries and interfaces during program design. Names findings and the future edits they tax; hands cures to refactor and quick passes to simplify. Do NOT use for bug hunts (that is code-review) or for executing a restructure (that is refactor).
---

# Maintainability Judgment

Answers one question: how expensive will the next change be? Scope is a diff or a module. Two modes: design (judge a proposed shape before code exists) and review (judge a diff or module). This skill names and ranks problems; it never executes the restructure.

## Use this vs. its neighbors

- Bug or correctness risk to find -> `code-review`.
- Sweep a whole codebase, not one diff, for deepening candidates -> `improve-codebase-architecture`.
- Judge whether the domain owns its own invariants -> `domain-model`.
- Look up the depth and information-hiding principles themselves -> `ousterhout-software-design`.
- Execute a named restructure with behavior held constant -> `refactor`.
- Quick reuse/simplification pass on a just-written diff -> `simplify`.
- Judge how a design or diff will age, with book-grounded names and a ranked verdict -> here.

## The measure

Complexity is anything about structure that makes code hard to understand and modify (Ousterhout). It shows as three symptoms; hunt them worst-first:

1. **Unknown unknowns**: it is not obvious what must change, or what might break when you do.
2. **Change amplification**: one conceptual change forces edits in many places.
3. **Cognitive load**: how much a developer must hold in mind to change it safely.

All three trace to two causes: dependencies (a part cannot be understood alone) and obscurity (important information is not visible where it is needed).

**The future-edits test** anchors every judgment: name the 2-3 most likely next changes to this area, then count the files and sites each would touch. Those counts are the verdict. A structure is never "bad"; it "taxes the tenant-scoping migration at 11 edit sites".

## Design mode

Invoked before code exists: program design, module boundaries, interface sketches. Judge each proposed module by:

- **Depth**: value = functionality divided by interface. A deep module hides a lot behind a small interface. An interface as complex as its implementation adds surface without hiding anything.
- **Information hiding**: list what a caller must know to use the module correctly. Every item on that list is a dependency; the shortest list wins.
- **Leakage**: the same knowledge required in two places (a format read in one class and written in another) is a leak. Reshape so one module owns the knowledge.
- **Somewhat general-purpose**: interface general, implementation only what today's need requires. Reject both speculative generality and an interface shaped by one caller's quirks.
- **Pull complexity downward**: better for the module to be complicated than its interface or callers. Config options and exceptions thrown upward are complexity exported to someone else.
- **Define errors out of existence**: prefer a contract where the error state cannot occur over a handler for it.

## Review mode

Walk the diff or module hunting the three symptoms. Use Fowler's smells as the detection vocabulary. The maintainability-critical smells: shotgun surgery (change amplification incarnate), divergent change, speculative generality, data clumps, primitive obsession.

Emit one finding per problem:

- **Name**: the book term (smell name, shallow module, leakage, exported complexity)
- **Site**: `file:line`
- **Tax**: the concrete future edit it makes expensive, with the site count from the future-edits test
- **Cure handoff**: `refactor` with the named smell, `tidy` for a sub-refactoring cleanup, `simplify`, or "accept and note"

Rank findings by the cost of the taxed edit. If nothing clears the bar, say so plainly; no filler findings.

## Tiebreaks

Where the books disagree, Ousterhout wins:

- Judge function size by abstraction depth, not line count. A long, deep function beats five shallow ones. Never recommend extraction to shrink a number; extract only when it separates concerns a reader currently must interleave.
- Keep from Martin: intention-revealing names, one level of abstraction per function, no flag arguments, command-query separation, test code held to production quality.
- Comments: the `code-comments` rule overrides all three books, including Ousterhout's comment-first stance. Never recommend adding design-rationale comments.
- Guards: the `no-dead-defensiveness` rule is "define errors out of existence" enforced. Never recommend a guard the contract already rules out.

## Gotchas

AI-written code is more locally coherent than human code, so the surface signals that normally say "scrutinize here" are absent exactly where scrutiny matters. Judge structure, never polish.

- **Defensive slop**: blanket `try/except`, `?? []` defaults, lazy casts. These maximize the chance the code runs, convert bugs into silent defaults, and erode the type system. Flag the contract, not the style: the fix is upstream, redefining the state so the guard has nothing to catch.
- **Shallow modules**: pass-through methods, one-line delegation layers, `Manager`/`Helper`/`Util` classitis. A decomposition into many tiny classes reads as tidy and is often net complexity. Test: does the layer change the abstraction? A layer that only forwards gets inlined.
- **Change amplification by copy**: agents extend systems by copying the sibling pattern. Before approving a near-duplicate, grep for the pattern and count instances. At three or more, the finding is "consolidate via `refactor`", not "add the fourth copy".
- **Tactical patches**: a special case added at the call site instead of a fix inside the abstraction. Each patch is locally rational; the trail is the tornado. Test: does this change make the next similar bug impossible, or only this one invisible?
