# skills

Agents are fast and agreeable. They clear failure signals, produce plausible
structure, and write generic prose. A green build, a clean diff, and a readable
draft are each things an agent can hand you without having solved your problem.

Every skill is grounded in a named framework. The map is in
[skills/FRAMEWORKS.md](skills/FRAMEWORKS.md).

## Install

```
/plugin marketplace add tslateman/skills
```

<details>
<summary><strong>Any other agent</strong></summary>

Skills are plain Markdown with YAML frontmatter and work anywhere skills, rules,
or instruction files are supported.

```bash
npx skills@latest add tslateman/skills
```

The groups are real directories, so take one at a time. `skills/review` alone is
a complete thing if the review suite is all you want.

Cursor: copy any group into `.cursor/skills/`.
Gemini CLI: `gemini skills install https://github.com/tslateman/skills.git --path skills/review`

</details>

`/voice` needs a corpus you supply at `$VOICE_TRAITS`, or
`~/.config/voice-traits.md` when that is unset.

`/slop-check` and `/ste` use a deterministic scanner when one is on `PATH`, and
report judgment-only findings when none is. Nothing here needs installing.

## What goes wrong

### The build went green and nothing got fixed

Hand an agent a compiler error and it finds the shortest path to green. Usually
a silencer: `as any`, `# type: ignore`, `.unwrap()`, `2>/dev/null`. Each edit is
one line and defensible on its own, the debt is in the aggregate, and the tool
that got silenced is the one tool that can never find it.

Six skills hunt this, one per language, because every language sells a different
escape hatch. Each runs the linter with a targeted rule set, then judges every
trigger as fine, mechanical fix, or restructure. A repeated trigger is one
finding, not many: five `as any` on one response are one unvalidated boundary.

[`/go-review`](skills/review/) · [`/python-review`](skills/review/) ·
[`/rust-review`](skills/review/) · [`/typescript-review`](skills/review/) ·
[`/shell-review`](skills/review/) · [`/test-review`](skills/review/) — the
argument is in [docs/local-fix-debt.md](docs/local-fix-debt.md).

Two skills work the other side of the clock. `/doubt` spawns a fresh-context
adversary before a decision lands, biased to disprove and deliberately not told
what you concluded. `/blast-radius` asks what a change breaks outside the diff,
and refuses to answer from reading alone — it names the one fact the change is
safe because of, then makes you prove it by running code.

### It works, and the next change will be expensive

Three judges, split by scope rather than by taste. `/maintainability` takes a
diff and ranks findings by the future edits each one taxes.
`/improve-codebase-architecture` takes a whole tree and returns the modules worth
deepening. `/domain-model` asks whether the code holding the state also holds the
rules about it.

They find; `/refactor` and `/tidy` execute. `/refactor` refuses to start without
a green suite, and `/legacy` is where it sends you when there is none.
`/deprecate` handles the other direction: whether the code should exist at all,
and how to remove it without breaking the callers who depend on behavior you
never promised.

→ [skills/craft/](skills/craft/README.md)

### Nobody can find their way around it

`/ia` designs the structure. `/wayfinding` asks whether a reader dropped into an
arbitrary file can tell where they are, which is how agents always arrive.
`/naming` judges one name, `/lexicon` judges a term set across code, docs, UI,
and API.

→ [skills/navigate/](skills/navigate/README.md)

### It reads like nobody wrote it

`/slop-check` scores a draft and deliberately refuses to rewrite it; `/prose` is
the fixing half. Run them in that order — a draft failing on genericness fails
`/voice` too, and its findings are cheaper to fix.

→ [skills/writing/](skills/writing/README.md)

### We built the wrong thing

`/spec-out` interviews sequentially, each round building on the last answers.
`/brainstorm` runs independent lenses in parallel. Diverge before you converge,
and never in the same pass.

→ [skills/shape/](skills/shape/README.md)

## The rest

[`/mermaid`](skills/draw/README.md) and
[`/excalidraw`](skills/draw/README.md) make the picture.
[skills/workspace/](skills/workspace/README.md) controls the session: `/arena`
races N candidates at one task and grafts the losers' best ideas into the
winner, `/wizard` scripts the steps only a human can take, `/obsidian-note`
writes into an Obsidian vault by reading that vault's own conventions first.

## Groups

| Group                                   | Owns                                      | Skills |
| --------------------------------------- | ----------------------------------------- | -----: |
| [review](skills/review/README.md)       | What is wrong with work that exists       |     11 |
| [craft](skills/craft/README.md)         | Whether code survives the next change     |     13 |
| [navigate](skills/navigate/README.md)   | Finding your way around unfamiliar code   |      6 |
| [writing](skills/writing/README.md)     | Whether prose is ready to publish         |      7 |
| [shape](skills/shape/README.md)         | Deciding what to build                    |      7 |
| [draw](skills/draw/README.md)           | Making the picture                        |      2 |
| [workspace](skills/workspace/README.md) | Controlling the session and its artifacts |     10 |

Each group README names what it owns and which skill to reach for.
`.claude-plugin/plugin.json` declares all seven, so Claude Code discovers all 56.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and
[docs/skill-anatomy.md](docs/skill-anatomy.md). Review skills follow a fixed
spine; a new language earns one when it has a _characteristic_ silencer, not
merely a linter.

## Prior art

Shaped by [mattpocock/skills](https://github.com/mattpocock/skills) and
[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills).
`/technical-writing`, `/blast-radius`, `/arena`, and the verification pair are
adapted from [pstack](https://github.com/cursor/plugins/tree/main/pstack) by
Lauren Tan, MIT.

Supersedes [duet](https://github.com/tslateman/duet), whose skills were migrated
here after a utilization pass over a month of session transcripts.
