# Workspace

**Control the session and its artifacts.**

| Skill                    | Does                                                        |
| ------------------------ | ----------------------------------------------------------- |
| `demo`                   | Record an mp4 of a UI change actually working               |
| `html-style`             | Three house styles for standalone HTML documents            |
| `obsidian-note`          | Write notes into an Obsidian vault, following its own rules |
| `get-or-create-note`     | Find the vault note for a URL, title, or topic, or make it  |
| `wizard`                 | Script the steps only a human can take                      |
| `arena`                  | Race N candidates at one task, then graft the losers' best  |
| `retro`, `vamp`, `sweep` | Reflect, choose what to play next, check for damage         |
| `writing-great-skills`   | Reference for writing skills well                           |

**`arena` is for the artifact one attempt would get wrong.** N agents take the
same prompt with different design directions, a read-only judge scores them
against a rubric written before anyone ran, and the best ideas from the losing
candidates get folded into the winner by hand. The rejection notes are the point
as much as the result.

**The two note skills read the vault, not this repo.** They resolve the vault
from `$OBSIDIAN_VAULT` or a directory containing `.obsidian/`, then read that
vault's own folders, frontmatter, and templates before writing. No convention is
hardcoded here, so they work against a vault laid out any way.

**`get-or-create-note` searches, `obsidian-note` writes.** The lookup skill
resolves a URL, title, or topic against the vault and opens what it finds; only
when nothing matches does it hand the title, the source, and the notes worth
linking to over to `obsidian-note`. Creation rules live in one file, not two.
Reach for the lookup first when handed a link — the duplicate it prevents costs
more than the search.

`html-style` ships three complete templates — Blueprint (dark, technical),
Drafting Table (light, editorial), Phosphor (terminal, mono). Pick by audience,
fill the template, keep the tokens.

`wizard` ships a tested bash library the same way, so authoring one is only a
matter of writing its stages. Reach for it when the agent stalls on something
only you can do — a dashboard you must be logged into, a secret shown once.
The script replaces re-explaining that procedure to the next agent.

**`retro`, `vamp`, and `sweep` all fire at a phase boundary**, and none of them
decides what to do with the context afterward. That decision — continue, clear,
hand off, delegate, or compact — has its own ordered tree in
[docs/phase-boundaries.md](../../docs/phase-boundaries.md). Run `retro` before
any lossy move: what it extracts survives the compaction that flattens the rest.
