# Workspace

**Control the session and its artifacts.**

| Skill                    | Does                                                        |
| ------------------------ | ----------------------------------------------------------- |
| `freeze`, `unfreeze`     | Restrict edits to one directory for the session             |
| `tether`, `untether`     | Bridge another project's context into this session          |
| `demo`                   | Record an mp4 of a UI change actually working               |
| `html-style`             | Three house styles for standalone HTML documents            |
| `obsidian-note`          | Write notes into an Obsidian vault, following its own rules |
| `retro`, `vamp`, `sweep` | Reflect, choose what to play next, check for damage         |
| `writing-great-skills`   | Reference for writing skills well                           |

**`freeze` is the one to reach for during focused debugging** — it stops an
agent wandering into files you did not ask it to touch.

Two skills read environment variables rather than assuming a layout:
`obsidian-note` reads `$OBSIDIAN_VAULT`, `tether` reads `$DEV_ROOT`.

`html-style` ships three complete templates — Blueprint (dark, technical),
Drafting Table (light, editorial), Phosphor (terminal, mono). Pick by audience,
fill the template, keep the tokens.
