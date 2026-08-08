# skills

**Judgment skills for working with coding agents.**

Twenty-three skills across four concerns: review what an agent wrote, judge
whether it will last, keep the prose yours, and control the session.

Agents are fast and agreeable. They clear failure signals, produce plausible
structure, and write competent generic prose. Each skill here asks a question
that a passing build, a clean diff, or a readable draft does not answer.

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

Cursor: copy `skills/` into `.cursor/skills/`.
Gemini CLI: `gemini skills install https://github.com/tslateman/skills.git --path skills`

Two skills call `bin/prose-scan`. Put it on your `PATH` to use them.

---

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

## Craft — will this survive contact with the next change

| Skill                              | Question                                                     | Grounded in                     |
| ---------------------------------- | ------------------------------------------------------------ | ------------------------------- |
| `/maintainability`                 | Will this stay cheap to change?                              | Ousterhout, Fowler, Martin      |
| `/ousterhout-software-design`      | Is the module deep or is the interface doing the work?       | A Philosophy of Software Design |
| `/refactor`                        | Execute a named restructure, behavior held constant          | Fowler, _Refactoring_           |
| `/strategic-architecture-analyzer` | Procedural transliteration, anemic models, leaked invariants | Deep modules, domain engines    |
| `/system-map`                      | Can two people hold the same picture of this system?         | C4 model                        |

`/maintainability` finds problems and hands cures to `/refactor`, which executes
them in verified steps. `/system-map` is a communication artifact for a named
audience, never a quality verdict.

## Writing — does this go out under your name

| Skill         | Question                             |
| ------------- | ------------------------------------ |
| `/slop-check` | Could anyone have written this?      |
| `/voice`      | Did **you** write this?              |
| `/ste`        | Can the reader execute it?           |
| `/narrate`    | Can you explain what you just built? |

Run `/slop-check` before `/voice` — a draft failing on genericness fails on
authorship too, and its findings are cheaper to fix.

`/voice` judges against a corpus you supply at `~/.claude/voice-traits.md`. It
ships the taxonomy, never anyone's traits; derive your own before first use.

`/ste` writes ASD-STE100 Simplified Technical English for text a reader
executes — runbooks, error messages, migration steps, agent instructions. It
strips nuance by design, so keep it away from anything that argues a position.

`/narrate` is a comprehension gate: explain the change in your own words before
committing it. Aimed squarely at code you accepted but did not read.

## Workspace — control the session

| Skill                  | Does                                                        |
| ---------------------- | ----------------------------------------------------------- |
| `/freeze`, `/unfreeze` | Restrict edits to one directory for the session             |
| `/tether`, `/untether` | Bridge another project's context into this session          |
| `/demo`                | Record an mp4 of a UI change actually working               |
| `/html-style`          | Three house styles for standalone HTML documents            |
| `/obsidian-write`      | Write notes into an Obsidian vault, following its own rules |
| `/bro`                 | Re-explain the last answer in plain language                |

`/freeze` is the one to reach for during focused debugging — it stops an agent
wandering into files you did not ask it to touch.

`/html-style` ships three complete templates: Blueprint (dark, technical),
Drafting Table (light, editorial), Phosphor (terminal, mono). Pick by audience,
fill the template, keep the tokens.

`/obsidian-write` reads `$OBSIDIAN_VAULT`. It defers to the vault's own
frontmatter and template conventions rather than carrying its own copy.

---

## Scope

These are judgment skills. They are not a build system, a test runner, or
general code review.

- **Generic bug hunt** → `/code-review`
- **Test strategy and design** → [`/duet:testing`](https://github.com/tslateman/duet)
- **Information architecture, naming, prose clarity** → [duet](https://github.com/tslateman/duet)

They compose with [duet](https://github.com/tslateman/duet): run `/code-review`
for correctness, then the language review for the debt the linter was told to
ignore.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and
[docs/skill-anatomy.md](docs/skill-anatomy.md). Review skills follow a fixed
spine; a new language earns one when it has a _characteristic_ silencer, not
merely a linter.

## Prior art

Shaped by [mattpocock/skills](https://github.com/mattpocock/skills) and
[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills).

## License

MIT
