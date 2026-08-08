# Wireframe quality bar

How to draw a UI mockup, current screen, a before/after pair, a flow, inside an
html-style document. Adapted from BuilderIO/skills `wireframe.md`; retargeted to
the house `:root` tokens (no external renderer, no `--wf-*` tokens, no rough.js).

A wireframe is a semantic-HTML mockup styled by the document's own tokens. You
write real layout and real product content; the document's `:root` palette and
fonts style it. Never escape into raw hex or a per-element `font-family`; the
chosen style (Blueprint / Drafting Table / Phosphor) owns color and type.

## Footprint, match what the user actually sees

Pick the frame footprint from the real surface, never default to desktop+mobile:

- **browser**, a web page that needs browser chrome around it.
- **desktop**, a full desktop app page or app shell.
- **mobile**, a phone screen, only when the work is genuinely mobile.
- **popover**, a small floating menu, dropdown, or inline popover.
- **panel**, a side panel, inspector, or sidebar widget.

A sidebar popover renders as a small surface, not a desktop page plus a phone
frame. Emit a mobile variant only when responsive behavior actually changes the
layout. For a component, show one broader app-context frame only when placement
affects understanding, then the focused component states.

## Compose real content

- Reproduce the actual product: real labels, real counts, real dates, real button
  text grounded in the screen you read, never lorem or gray placeholder bars
  (except a genuine skeleton/loading state, which is intentional neutral geometry).
- Lay out with inline `style` flex/grid, `display:flex; flex-direction:column;
gap:10px; padding:16px`, and use literal CSS lengths for spacing, not theme
  spacing variables.
- Wrap content in a root container with real inner padding (14-16px),
  `box-sizing:border-box`, `height:100%`, and `gap` between rows, so the first row
  never sits flush against the frame border.
- Color comes from the document's `:root` tokens (`var(--ink)`, `var(--muted)`,
  `var(--line)`, `var(--accent)`, …). Never hard-code hex inside a wireframe and
  never set `font-family`.
- No decorative shadows. Mockups read as flat bordered surfaces; use spacing,
  borders, and labels for separation. Show a shadow only when the real product UI
  already has it and it is essential to the change.

## Modify, don't redesign

When the task changes an existing screen, reproduce the current layout and
footprint first, then change only the delta and call it out with a single
annotation. Do not restack the page into a new layout. For net-new surfaces,
compose from the real app shell, inspect the actual sidebar density, toolbar
actions, and overflow menus before drawing.

Keep product screens pure: a wireframe shows the app state a user would see. Do
not embed file contracts, architecture arrows, repo labels, or implementation
callouts inside the screen. Those go in a caption, a separate diagram, or the
document body.

## Before / after must be comparable

The before/after pair is the headline of a UI recap or design doc.

- Use the same frame size, scale, padding, radius, and density on both sides
  unless the change itself alters those.
- Preserve the unchanged controls in both states so the reviewer sees exactly what
  moved or appeared. Do not show a new control as a generic box floating elsewhere.
- Place the new affordance where the implementation puts it, a new header action
  belongs in the top-right header slot aligned with the title, not in the body.
- Name the states with a heading above each frame (Before / After). Never bake a
  Before/After pill or title into the wireframe HTML, a label inside reads as part
  of the product UI and lands in a random corner.
- Lay narrow surfaces (mobile, popover, panel) side by side; stack wide surfaces
  (desktop, browser) vertically at full width so a large frame is never crushed.

## Chrome bars and layout safety

- **Persistent chrome bars span the full frame width.** Top bars, headers, and
  bottom tab/nav bars are full-width chrome, not centered content. Lay each as one
  flex row filling the frame and push trailing actions to the right edge with a
  flex spacer (`<div style="flex:1"></div>`). In a before/after pair the bar stays
  full-width in both states; the spacer absorbs the difference.
- **Pin bottom bars to the bottom.** Make the frame a flex column at `height:100%`,
  give the scrolling body `flex:1`, and place the bar as the last child (or
  `margin-top:auto`) so it sits flush at the bottom, not floating under content.
- **Fill the frame, keep labels on one line.** Compose enough real HTML to fill the
  surface top to bottom with even rhythm, no large empty band. For toolbars, tab
  rails, breadcrumbs, chip rows, and filenames, set `white-space:nowrap` so a
  deliberately single-line row never wraps into stacked text.
- **Lay children out safely.** Flex/grid with `gap`, `min-width:0`, sensible
  overflow. Avoid negative margins, absolute positioning, or fixed child widths
  that collide across light/dark or zoom.

## Skeleton / loading states

Fill the frame with neutral, textless placeholder geometry, boxes and bars built
as `<div>`s with `background:var(--line)` and explicit heights/widths, no labels
or copy. A skeleton is the one place gray bars are correct.
