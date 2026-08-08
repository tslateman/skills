# skills

**Judgment skills for working with coding agents.**

Forty-six skills across seven concerns: catch what an agent got wrong, judge
whether the code will last, find your way around it, write what goes out under
your name, decide what to build, draw the picture, and control the session.

Agents are fast and agreeable. They clear failure signals, produce plausible
structure, and write competent generic prose. Each skill here asks a question
that a passing build, a clean diff, or a readable draft does not answer.

Every skill is grounded in a named framework. The full map is in
[skills/FRAMEWORKS.md](skills/FRAMEWORKS.md).

## Install

### Claude Code

```
/plugin marketplace add tslateman/claude-plugins
/plugin install skills@tslateman
```

Or straight from this repo:

```
/plugin marketplace add tslateman/skills
```

### Any other agent

Skills are plain Markdown with YAML frontmatter and work anywhere skills, rules,
or instruction files are supported.

```bash
npx skills@latest add tslateman/skills
```

Cursor: copy any group into `.cursor/skills/`.
Gemini CLI: `gemini skills install https://github.com/tslateman/skills.git --path skills/review`

Because the groups are real directories, every other agent can install one at a
time — take `skills/review` alone if the review suite is all you want.

`/slop-check` and `/ste` call `bin/prose-scan`. Put it on your `PATH` to use them.

---

## Layout

```text
skills/
├── review/      inspect existing work and report what is wrong
├── craft/       judge whether code survives the next change
├── navigate/    find your way around unfamiliar code
├── writing/     decide whether prose is ready to publish
├── shape/       decide what to build before building it
├── draw/        make the picture
└── workspace/   control the session and its artifacts
```

Each group carries a `README.md` explaining what it owns and which skill to
reach for. `.claude-plugin/plugin.json` declares the seven directories in its
`skills` field, so Claude Code discovers all 46.

## Review — catch what coding agents get wrong

Six skills hunting one debt class: **local-fix debt**, the minimal edit that
clears a failure signal without fixing its cause. Give an agent a compiler
error and it finds the shortest path to green — usually a silencer, and every
language offers a different one.

| Skill                | Audit          | Hunts                                                                                           |
| -------------------- | -------------- | ----------------------------------------------------------------------------------------------- |
| `/go-review`         | Local-Fix Debt | Discarded errors, string-matched error handling, panic as control flow, leaked goroutines       |
| `/python-review`     | Local-Fix Debt | Blind except, `type: ignore`, `Any` in signatures, `.get()` defaults hiding KeyErrors           |
| `/rust-review`       | Local-Fix Debt | Clone-to-satisfy-the-borrow-checker, bare `unwrap`, `#[allow]` suppression                      |
| `/typescript-review` | Local-Fix Debt | `as any`, non-null assertions, floating promises, untyped JSON at boundaries                    |
| `/shell-review`      | Silent Failure | `2>/dev/null`, missing `set -euo pipefail`, unquoted expansions, GNU-vs-BSD assumptions         |
| `/test-review`       | Falsifiability | Assertions that cannot fail, mocked units under test, sleep-based timing, regenerated snapshots |

Each runs the language's linter with a targeted rule set, then sorts every
trigger into **fine**, **mechanical fix**, or **restructure** — the third named
with its blast radius and never applied without asking. Repeated triggers
collapse into one finding: five `as any` on the same response are one
unvalidated boundary.

The full argument is in [docs/local-fix-debt.md](docs/local-fix-debt.md).

Three broader passes sit alongside them: `/code-review` for knowledge-transfer code
review, `/vibe-check` for whether the whole change holds up, `/visual-recap` for
the shape of a large diff before reading lines. See
[skills/review/README.md](skills/review/README.md).

## Craft — will this survive contact with the next change

[skills/craft/](skills/craft/README.md)

| Skill                              | Question                                                     |
| ---------------------------------- | ------------------------------------------------------------ |
| `/maintainability`                 | Will this stay cheap to change?                              |
| `/ousterhout-software-design`      | Is the module deep, or is the interface doing the work?      |
| `/improve-codebase-architecture`   | Which modules are worth deepening?                           |
| `/strategic-architecture-analyzer` | Procedural transliteration, anemic models, leaked invariants |
| `/refactor`                        | Execute a named restructure, behavior held constant          |
| `/design`                          | Is the interface right before it ships?                      |
| `/testing`                         | Which test properties matter here, and what do they cost?    |

`/maintainability` finds problems and hands cures to `/refactor`, which executes
them in verified steps against a green suite.

## Navigate — find your way around unfamiliar code

[skills/navigate/](skills/navigate/README.md)

| Skill         | Question                                             |
| ------------- | ---------------------------------------------------- |
| `/zoom-out`   | Where does this fit? Map it before reading details   |
| `/system-map` | Can two people hold the same picture of this system? |
| `/ia`         | Can anyone find this?                                |
| `/wayfinding` | Can a reader dropped anywhere tell where they are?   |
| `/naming`     | Is this name carrying its weight?                    |
| `/lexicon`    | Do we all mean the same thing by this term?          |

`/ia` designs the structure; `/wayfinding` asks whether it can be traversed from
an arbitrary entry point — which is how agents always arrive. `/naming` judges
one name, `/lexicon` judges a term set across code, docs, UI, and API.

## Writing — does this go out under your name

[skills/writing/](skills/writing/README.md)

| Skill         | Question                               |
| ------------- | -------------------------------------- |
| `/prose`      | Is it clear and as short as it can be? |
| `/slop-check` | Could anyone have written this?        |
| `/voice`      | Did **you** write this?                |
| `/ste`        | Can the reader execute it?             |
| `/narrate`    | Can you explain what you just built?   |
| `/bro`        | Can the reader understand it?          |

`/slop-check` scores and deliberately refuses to rewrite; `/prose` is the fixing
half. Run slop-check first — a draft failing on genericness fails `/voice` too,
and its findings are cheaper to fix.

`/voice` judges against a corpus you supply at `~/.claude/voice-traits.md`. It
ships the taxonomy, never anyone's traits; derive your own before first use.

`/ste` writes ASD-STE100 Simplified Technical English for text a reader
executes — runbooks, error messages, migration steps, agent instructions. It
strips nuance by design, so keep it away from anything that argues a position.

## Shape — decide what to build before building it

[skills/shape/](skills/shape/README.md)

| Skill                          | Question                                     |
| ------------------------------ | -------------------------------------------- |
| `/spec-out`                    | You have a vague idea — what is it actually? |
| `/brainstorm`                  | You know the goal — what are the options?    |
| `/research`                    | What should we use, and what does it cost?   |
| `/adr`                         | Why did we choose this, for the next reader? |
| `/automagic-problem-discovery` | What friction have you stopped noticing?     |

`/spec-out` interviews sequentially, each round building on the last answers.
`/brainstorm` runs independent lenses in parallel. The split is deliberate:
diverge before you converge, and never in the same pass.

## Draw — make the picture

[skills/draw/](skills/draw/README.md)

| Skill         | For                                              |
| ------------- | ------------------------------------------------ |
| `/mermaid`    | Diagrams that render natively in GitHub markdown |
| `/excalidraw` | Hand-drawn, editable architecture overviews      |

## Workspace — control the session

[skills/workspace/](skills/workspace/README.md)

| Skill                       | Does                                                        |
| --------------------------- | ----------------------------------------------------------- |
| `/freeze`, `/unfreeze`      | Restrict edits to one directory for the session             |
| `/tether`, `/untether`      | Bridge another project's context into this session          |
| `/demo`                     | Record an mp4 of a UI change actually working               |
| `/html-style`               | Three house styles for standalone HTML documents            |
| `/obsidian-note`            | Write notes into an Obsidian vault, following its own rules |
| `/retro`, `/vamp`, `/sweep` | Reflect, choose what to play next, check for damage         |
| `/writing-great-skills`     | Reference for writing skills well                           |

`/freeze` is the one to reach for during focused debugging — it stops an agent
wandering into files you did not ask it to touch.

`/html-style` ships three complete templates: Blueprint (dark, technical),
Drafting Table (light, editorial), Phosphor (terminal, mono). Pick by audience,
fill the template, keep the tokens.

`/obsidian-note` reads `$OBSIDIAN_VAULT` and defers to the vault's own
frontmatter and template conventions rather than carrying its own copy.

---

## Recipes

Eight skills ship a `RECIPE.md` — a decomposition spec telling a multi-agent
orchestrator how to split the work, what each worker owns, and how to
synthesize. See the table in [skills/FRAMEWORKS.md](skills/FRAMEWORKS.md).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and
[docs/skill-anatomy.md](docs/skill-anatomy.md). Review skills follow a fixed
spine; a new language earns one when it has a _characteristic_ silencer, not
merely a linter.

## Prior art

Shaped by [mattpocock/skills](https://github.com/mattpocock/skills) and
[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills).

Supersedes [duet](https://github.com/tslateman/duet), whose skills were migrated
here after a utilization pass over a month of session transcripts.

## License

MIT
