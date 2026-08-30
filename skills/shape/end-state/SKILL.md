---
name: end-state
description: Write the end state at the layer where disciplines converge, then peel it into a release ladder where every rung names what it enables and what it defers. Use when a team argues the surface instead of the concept, when features accrete ad hoc into a functional salad, when a roadmap lists additions but never deferrals, or on "what's the end state", "design the whole thing first", "what are we not building yet", "write the press release". Do not use to decide whether to build at all — that is spec-out — or to turn one release into tasks, which is slice.
argument-hint: "[product, feature, or nothing to use the conversation]"
---

# End State — The Whole Thing First, Then the Peel

A spec says what to build. It does not produce a shared picture of the finished
thing, and without one, every increment is argued on its own merits. Features
arrive because someone asked, not because a release enabled them, and the
product becomes a **functional salad**: everything in it, nothing composing.

The cure is to write the whole thing first and peel back — but written at a
layer the whole team can hold, not the layer one discipline draws in.

## Use this vs. its neighbors

- Deciding whether to build at all → `spec-out`.
- Exploring options before committing → `brainstorm`.
- Choosing shape and tone for an interface → `design`.
- Turning one release into tasks that can be picked up → `slice`.
- Naming the whole and sequencing releases out of it → here.

Runs after `spec-out`, before `slice`. `slice` decomposes one rung of the ladder
this skill builds.

## 1. Write the end state at the convergence layer

Describe what someone can do when this is finished. Not the screen, not the
schema, not the mechanism — the observable outcome, in the language of whoever
benefits.

**The test: can you state the end state without naming a screen, a component, or
a mechanism?** If not, you are specifying the layer people will argue about.

A mockup is specific about the wrong layer. It shows one instantiation, so the
room debates the instantiation, and everyone leaves with a different idea of
what the thing _is_ — the artifact showed a surface and let each person infer
the point. Prose describing an outcome underspecifies on purpose: readers build
different mental images that agree on what matters.

The press release is the sharpest known form of this. Written in the voice of
the finished announcement, it is grammatically a _description_ rather than a
proposal, so it carries no discipline's fingerprints — an engineer, a designer,
and a PM produce indistinguishable ones. That is what lets it converge a room
that a mockup splits.

Completion criterion: a reader from a different discipline can restate what the
product does without looking at the document.

## 2. Force the disclosure

A polished artifact lets you skip questions. List them and answer them beside
the end state — the FAQ half.

At minimum: who is this for, what did they do before, what breaks, what must be
true for this to work, what does it cost, who else is affected.

This is where feasibility belongs. The order is the mechanism: value in the
description, cost in the questions, both in one sitting. A meeting has no
enforced reading order, so the first substantive objection is reliably
feasibility, and cost-first framing kills options a value-first reading would
have survived. Deferring cost entirely is the opposite failure — an unpriced
promise paid later in quiet descoping.

Completion criterion: every question has an answer or an explicit "unknown".
Recorded unknowns are the point, not a gap to smooth over.

## 3. Make one claim falsifiable

The end state must contain at least one claim that shipping could prove wrong.

Without it, "off-vision" becomes a veto that discards disconfirming evidence,
and the document's authority grows as its accuracy falls.

If nothing in the document could be falsified by building, it is a mood, not a
constraint.

## 4. Peel to a release ladder

Work backwards from the end state to the first release. Each rung names two
things:

| Release | Enables | Defers |
| ------- | ------- | ------ |
| R1      | …       | …      |
| R2      | …       | …      |

**The deferred column is load-bearing.** An MVP names the increment; a slice
names the remainder. A remainder nobody inventories is a heap that admits
anything, which is how the salad returns. A release that lists only what it adds
has not been peeled — it has been guessed.

Two rules for the ladder:

- Every rung is a coherent subset of the end state, demonstrable alone. Not a
  partial version of everything.
- Everything in the end state appears in exactly one Enables cell, or in a
  Defers cell with no rung after it — in which case say so and cut it from the
  end state.

Completion criterion: every capability in the end state is accounted for on the
ladder.

## 5. When the end state is genuinely unknown

This discipline assumes an unknown _solution_ with known _demand_. Where demand
itself is unknown, coherence is the wrong objective: each increment's job is to
produce information, and a deliberately incoherent portfolio of probes beats a
coherent subset of a guess.

Middle case, and the common one: structure knowable, content not. Commit the
invariants — who it is for, the hard constraints, the forced-disclosure answers
— and leave the feature list open. Build the ladder over the invariants.

Say which case you are in before writing the ladder.

## 6. Amending it later

The document is not an enforcement mechanism, and treating it as one is theater.
What makes it hold:

- **Numbered claims.** An unnumbered document cannot be amended, only rewritten,
  and rewriting to match what shipped is the failure being prevented.
- **Supersession, not replacement.** Keep the prior text, mark it superseded,
  date it, say why — the same discipline as an ADR. Reach for `adr` when the
  amendment is a decision worth its own record.
- **Amendment costs more than one increment and less than a rewrite.** Too cheap
  and the document tracks whatever shipped; too expensive and people route
  around it.
- **Check the dates.** An amendment dated after the release it authorizes is the
  signature of quiet backfilling. This is the one part that scripts.

## Rules

- State the end state without naming a screen, a component, or a mechanism.
- Never publish a ladder rung without its Defers cell.
- Every capability in the end state lands in exactly one Enables cell.
- Record unknowns as unknowns. Do not reason into the gap.
- One falsifiable claim, minimum.
- Do not inherit sequencing from Amazon's published process — it has none. The
  PR/FAQ template carries no milestone or phasing question, and the ladder is
  the part you are adding.

## The check that matters

Count what dies while writing, before anyone reads it. A document that has never
killed or reshaped work is an artifact without a mechanism.
