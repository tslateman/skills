# Plan & design-doc discipline

How a plan, RFC, or design doc reads, not how it looks. The look comes from the
chosen style template; this is the writing bar. Adapted from BuilderIO/skills
`document-quality.md`, with their block-vocabulary specifics stripped.

## A serious technical document, not marketing

Write it the way a strong implementation plan reads: outcome-first, prose-first,
self-contained, specific. State the objective and what "done" means, the scope and
non-goals, the proposed approach with the key decisions and their rationale,
ordered steps that name real files, symbols, and data shapes, the risks, and a
closing verification step. Replace vague prose with specifics, never ship a step
like "make it work." No hero art, slogans, value props, or landing-page headings
unless explicitly asked.

## Every document stands alone

A reader who opens the document from a link with no chat history must understand
it. Even when revising, the output is a plan to do the work, not a changelog of
the conversation. Cut phrases like "as discussed above", "this revision",
"preserve the prior plan", "unlike the previous version". Fold the right decisions
in as normal objective, approach, and scope prose. Avoid negative framing that
only makes sense against absent context ("not the old mode"), state the positive
model directly.

## Make abstract documents legible

If the idea is broad, strategic, or for a third-party reviewer, put one concrete
snapshot near the top, a real example, a before/after, a single screen, before
dense architecture, mode tables, or roadmaps. Then put mechanics and detail in
separate sections below. Preserve the user's level of abstraction: a motivating
use case is not automatically the architecture. Separate the reusable core from
specific apps, providers, or launch examples; label which is which.

## Lead with reuse

For each step, name what it reuses, existing modules, schema, components,
helpers, before what it adds, so the document explains the genuinely new delta
instead of redescribing what already exists.

## Decide the hard-to-reverse bets first

For non-trivial backend, data, or API work, call out the decisions expensive to
undo once data or callers depend on them, wire format, public ids, data-model
shape, auth and ownership boundaries, and get those right even if most of the
feature ships later. Then scope to the smallest first cut that proves the approach
without foreclosing it, stating what is in and what is explicitly deferred.

## Open questions live in one place

Surface unresolved decisions that would change the plan in a single "Open
Questions" section, each with a recommended default. That section is the only
place open questions are enumerated, no second list scattered through the
narrative, never the same question twice. A one-line pointer up top ("a few
decisions are still open, see Open Questions") is fine. For a complex plan, do a
final pass: if architecture, scope, UX, data shape, or rollout still depends on a
choice, either commit to it with rationale or add it to that section.

## Diagrams are two-dimensional

Use a diagram only when a relationship needs a visual. Prefer paired before/after
panels, layered diagrams, swimlanes, dependency maps, matrices, or grouped
regions. Do not default to a left-to-right chain; use a line only when the
relationship is truly a sequence. Keep labels short and clear of nodes and
connectors. (See `mermaid` or an html-style diagram block for the rendering.)

## Verification exercises the real workflow

The closing verification section should go beyond typecheck and unit tests when
the work changes UI, data, sync, providers, or multi-step flows. Include at least
one end-to-end smoke that matches the user journey, a real fixture, a browser
interaction, a save/sync action, an on-disk or database assertion. Name the
command or manual path when known.
