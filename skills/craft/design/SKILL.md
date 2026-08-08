---
name: design
description: Intentional design thinking for interfaces, components, and systems. Use when the user asks to "build a UI", "design a page", "create a component", "make this look good", "design an API", "design a system", or any task where aesthetic or structural design decisions matter.
---

# Design as Intention

## Overview

Design is choosing what to do and what to leave out. Every design decision — visual, structural, interactive — should be deliberate. Generic defaults are the enemy. The key is intentionality, not intensity.

## Design Thinking

Before implementing, commit to a direction:

1. **Purpose** — What problem does this solve? Who uses it?
2. **Tone** — What should it feel like? (Minimal, bold, playful, austere, warm, precise, raw)
3. **Constraints** — Technical limits, accessibility, performance
4. **Differentiation** — What makes this memorable? What's the one thing worth getting right?

Bold maximalism and refined minimalism both work. Timid middle ground does not.

## Visual Design

When building interfaces, fight generic AI aesthetics:

### Typography

Choose distinctive, characterful fonts. Pair a display font with a refined body font. Avoid defaults (Arial, Inter, Roboto, system fonts). Every font choice signals intent.

### Color

Commit to a cohesive palette. Use CSS variables for consistency. Dominant colors with sharp accents outperform timid, evenly-distributed palettes. Vary between light and dark — don't default to one.

### Motion

Focus on high-impact moments. One well-orchestrated page load with staggered reveals creates more delight than scattered micro-interactions. Prioritize CSS-only solutions. Use scroll-triggering and hover states that surprise.

### Composition

Unexpected layouts. Asymmetry. Overlap. Grid-breaking elements. Generous negative space OR controlled density — both work, but choose one.

### Texture

Create atmosphere and depth. Gradient meshes, noise textures, geometric patterns, layered transparencies, dramatic shadows. Never default to flat solid backgrounds.

**Never:** Overused font families, purple-gradient-on-white, predictable card grids, cookie-cutter components. No two designs should converge on the same choices.

## API Design

When designing interfaces between systems:

- **Consistency** — Same patterns everywhere. If one endpoint uses `create`, don't use `add` elsewhere
- **Least Astonishment** — Every method does what its name suggests, nothing more
- **Minimal surface** — Expose only what callers need. You can add later but can't remove
- **Fail fast** — Report errors at the point closest to the mistake
- **Self-documenting** — If the interface needs a comment, the design needs work

## System Design

When designing architecture or structure:

- **Single responsibility** — Each component does one thing well
- **Clear boundaries** — Where does one module end and another begin?
- **Explicit dependencies** — No hidden coupling, no global state
- **Reversibility** — Prefer decisions you can undo. Isolate the ones you can't

## The Test

After designing, ask:

- Can I explain the concept in one sentence?
- Does every element serve the purpose?
- Would someone remember this? Why?
- What did I deliberately leave out?

Match complexity to vision. Elaborate designs need elaborate execution. Simple designs need precision. Elegance comes from committing fully to the chosen direction.

## See Also

- `/naming` — Hard-to-name things signal design problems
- `/adr` — Capture design decisions and their reasoning
- `/review` — Reviews assess design quality alongside correctness
- `skills/FRAMEWORKS.md` — Full framework index
- `RECIPE.md` — Agent recipe for parallel decomposition (3 workers)
