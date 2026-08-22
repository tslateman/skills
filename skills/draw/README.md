# Draw

**Make the picture.**

| Skill        | For                                              |
| ------------ | ------------------------------------------------ |
| `mermaid`    | Diagrams that render natively in GitHub markdown |
| `excalidraw` | Hand-drawn, editable architecture overviews      |

**Mermaid for anything living in a repo** — it renders in GitHub without a
build step, and the source diffs. **Excalidraw when someone will drag the boxes
around afterward.**

Deciding _what_ to draw is a different job: see
[`system-map`](../navigate/README.md) for choosing the levels and the audience.

`excalidraw` ships Python and Node scripts under `excalidraw/scripts/`. The
skill resolves that directory relative to itself rather than from a fixed path
or a harness variable, so it works wherever the skills are installed.
