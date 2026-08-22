---
name: html-style
description: Three house styles for hand-built HTML documents — plans, reports, design docs, presentations, decks, leverage/strategy write-ups. Use whenever you are generating a standalone HTML document (not product/app UI). Defines three styles — Blueprint (dark, technical), Drafting Table (light, editorial), Phosphor (terminal, mono) — with a use-case map, and ships a ready-to-fill template for each. Always start from the matching template; never hand-roll a fresh dark-SaaS-dashboard look.
---

# HTML House Styles

Three deliberate looks for standalone HTML documents, so generated output reads deliberate, not like generic AI slop. Pick a style by audience, copy its template, replace the content, keep the tokens.

This skill is for **documents** (plans, reports, design docs, decks). For product/landing-page UI use `blueprint-ui` or `frontend-design` instead.

## Never ship the slop signature

The default "AI dark dashboard" look is banned. Do not reach for any of these unless a chosen style explicitly calls for it:

- Navy/charcoal background (`#0b0f14`, `#0f1115`) with a teal or periwinkle accent (`#3fd0c9`, `#6c8cff`).
- Rounded cards (`border-radius: 12–14px`) that lift on hover (`translateY(-2px)`).
- Radial-gradient "glow" blobs behind cards.
- Status pills on tinted `rgba()` fills in a rainbow of hues.
- Sticky blurred (`backdrop-filter`) headers.

Shared rules across all three styles: **one accent color**, used sparingly. Strong typographic hierarchy over decoration. Restraint beats embellishment. Real content over filler.

## Pick the style by audience

| Use case                                                                                               | Style                  | Why                                                                                    |
| ------------------------------------------------------------------------------------------------------ | ---------------------- | -------------------------------------------------------------------------------------- |
| Internal technical plan, report, design doc, engineer audience                                         | **A · Blueprint**      | Default house style. Terminal-native, confident, matches the `blueprint-ui` aesthetic. |
| Anything in front of PMs, partners, execs, or external readers                                         | **B · Drafting Table** | Light, calm, editorial. Reads as credible and considered, not generated.               |
| Internal/personal artifact, scratch report, CLI/infra-flavored write-up where personality beats polish | **C · Phosphor**       | Maximally opinionated terminal look. Unmistakably an engineer's artifact.              |

When unsure, default to **A**. A full style guide may pair one dark (A or C) + one light (B) and choose per audience.

## A · Blueprint, dark, amber, technical

Template: `templates/blueprint.html`

- **Palette:** bg `#0a0a0a`, surface `#111111`, line `#1e1e1e`, bright `#333333`, ink `#e8e8e8`, muted `#8a8a8a`, dim `#525252`, accent amber `#f59e0b`, alt orange `#ea580c`.
- **Type:** Inter (body/headings), JetBrains Mono (labels, counters, code).
- **Signature moves:** dot-grid background; sharp edges (no rounded corners ever); dashed rules; monospace uppercase section labels over borders; `01/02` leading-zero counters; `$`-prefixed command blocks.

## B · Drafting Table, light, warm paper, oxblood, editorial

Template: `templates/drafting-table.html`

- **Palette:** paper `#f4efe3`, raised `#ece4d2`, ink `#1c1a16`, muted `#6f685a`, rule `#d4c9b3`, accent oxblood `#9a3b2e`, link ink-blue `#2f4858`.
- **Type:** Source Serif 4 (serif headlines), Newsreader (serif lede/quotes), Inter (body), JetBrains Mono (labels/code).
- **Signature moves:** warm paper field; hairline tan rules; serif headlines; generous whitespace; flat document flow (no floating cards); oxblood used only for emphasis, ink-blue only for links.

## C · Phosphor, dark, all-mono, terminal

Template: `templates/phosphor.html`

- **Palette:** bg `#0c0d0c`, surface `#121613`, line `#212a20`, bright `#33402f`, ink `#d4ddcf`, muted `#74806e`, accent phosphor green `#7fd897`.
- **Type:** IBM Plex Mono everywhere.
- **Signature moves:** all-monospace; one phosphor accent; status by inversion (accent fill on bg) rather than many hues; `//` comment eyebrows; box-drawing dividers; shell-prompt code blocks (`guest@cm:~$`). Keep color to the single green, let structure and monospacing carry it.

## How to use

1. Choose the style from the table above.
2. Copy the matching template from `templates/` as the starting file.
3. Replace the sample content. Keep the `:root` tokens and the component classes (`eyebrow`, `lede`, `chip`, `callout`, `steps`, `section-label`, etc.) intact.
4. Reuse the provided components rather than inventing new ones. If you need a component the template lacks, build it from the same tokens and in the same spirit.
5. State the generated date in the footer. Keep it honest and uncluttered.

## Wireframes and document discipline

Two reference files carry the quality bar for the harder parts of a document. The look still comes from the chosen style template; these govern the content.

- **`references/wireframe.md`**, drawing a UI mockup (current screen, before/after pair, or flow) inside a document: footprint presets (browser/desktop/mobile/popover/panel), real product content over filler, modify-don't-redesign, comparable before/after, full-width chrome, pinned bottom bars. Read it before authoring any wireframe. Wireframes are themed by the document's `:root` tokens, never raw hex or per-element fonts.
- **`references/plan-discipline.md`**, how a plan, RFC, or design doc reads, not how it looks: outcome-first, self-contained, an abstract→concrete snapshot near the top, reuse-first, hard-to-reverse bets decided early, open questions in one section with recommended defaults, two-dimensional diagrams, verification that exercises the real workflow. Read it before writing a plan or design-doc body.

## Prose inside the document

These styles govern the look. The words are a separate job: run `/slop-check` on
the body copy before shipping a document that carries an argument. A document
can clear every slop-test gate here and still read as generated.
