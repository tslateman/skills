# skills

**Catch what coding agents get wrong.**

Six review skills for AI coding agents, each hunting one debt class: the
minimal local edit that makes a failure signal disappear without fixing what
caused it.

## The problem

Give an agent a compiler error, a failing lint, or a red test, and it will find
the shortest path to green. That path is usually a silencer, and every language
offers a different one:

| Language       | The pressure                       | The silencer it offers              |
| -------------- | ---------------------------------- | ----------------------------------- |
| **Go**         | Errors are values you must handle  | `_ = err`, bare `return err`        |
| **Python**     | The interpreter rarely pushes back | `except: pass`, `# type: ignore`    |
| **Rust**       | The borrow checker refuses to move | `.clone()`, `.unwrap()`, `#[allow]` |
| **TypeScript** | The type system is opt-out         | `as any`, `!`, `@ts-ignore`         |
| **Shell**      | Failure is silent by default       | `2>/dev/null`, `\|\| true`          |
| **Tests**      | Green is the only visible signal   | Assert whatever the code just did   |

Each edit works. The build goes green, the linter goes quiet, the suite passes.
The bug moves downstream and arrives later without a stack trace.

This is **local-fix debt**, and it is invisible to the tool that was silenced —
which is precisely why a linter alone will not find it. See
[docs/local-fix-debt.md](docs/local-fix-debt.md).

## What these skills do

Each skill runs two passes:

1. **Mechanical** — the language's own linter with a rule set targeted at this
   debt class, plus greps for the triggers no linter can judge.
2. **Judgment** — every trigger sorted into three buckets:
   - **Fine** — idiomatic, or the pragmatic choice is documented
   - **Mechanical fix** — a safe local rewrite
   - **Restructure** — the silencer exists because the design fights the data
     flow. Named, scoped, never applied without asking. This bucket is why the
     review exists.

Repeated triggers collapse into one finding. Five `as any` on the same API
response are one unvalidated boundary, not five problems.

## Skills

| Skill                | Audit          | Hunts                                                                                           |
| -------------------- | -------------- | ----------------------------------------------------------------------------------------------- |
| `/go-review`         | Local-Fix Debt | Discarded errors, string-matched error handling, panic as control flow, leaked goroutines       |
| `/python-review`     | Local-Fix Debt | Blind except, `type: ignore`, `Any` in signatures, `.get()` defaults hiding KeyErrors           |
| `/rust-review`       | Local-Fix Debt | Clone-to-satisfy-the-borrow-checker, bare `unwrap`, `#[allow]` suppression                      |
| `/typescript-review` | Local-Fix Debt | `as any`, non-null assertions, floating promises, untyped JSON at boundaries                    |
| `/shell-review`      | Silent Failure | `2>/dev/null`, missing `set -euo pipefail`, unquoted expansions, GNU-vs-BSD assumptions         |
| `/test-review`       | Falsifiability | Assertions that cannot fail, mocked units under test, sleep-based timing, regenerated snapshots |

`/test-review` is language-agnostic. It asks one question of every test: name a
change to the production code that would turn this red. A test with no answer is
a finding regardless of coverage.

## Install

### Claude Code

```
/plugin marketplace add tslateman/claude-plugins
/plugin install skills@tslateman
```

Or install directly from this repo:

```
/plugin marketplace add tslateman/skills
```

### Any other agent

The skills are plain Markdown with YAML frontmatter. They work anywhere skills,
rules, or instruction files are supported.

```bash
npx skills@latest add tslateman/skills
```

Cursor: copy `skills/` into `.cursor/skills/`.
Gemini CLI: `gemini skills install https://github.com/tslateman/skills.git --path skills`

### Manual

```bash
git clone https://github.com/tslateman/skills.git ~/dev/skills
ln -s ~/dev/skills/skills/* ~/.claude/skills/
```

## Usage

```
/python-review                    # working-tree changes
/python-review src/ingest         # a path
/go-review ./internal/queue       # a package
/test-review tests/integration    # a suite
```

With no argument each skill reviews the changed files of its language. Ask it to
apply fixes and it applies bucket 2 directly, re-runs the linter and the tests,
and brings you a plan for bucket 3.

## Scope

These skills hunt one thing well. They are not general code review.

- **Generic bug hunt** → `/code-review`
- **Test strategy and design** → [`/duet:testing`](https://github.com/tslateman/duet)
- **Broad judgment on vibe-coded output** → [`/duet:vibe-check`](https://github.com/tslateman/duet)
- **Maintainability and module boundaries** → `/duet:maintainability`

They compose: run `/code-review` for correctness, then the language review for
the debt the linter was told to ignore.

## Contributing

New languages are welcome if they follow the shared spine — see
[CONTRIBUTING.md](CONTRIBUTING.md) and
[docs/skill-anatomy.md](docs/skill-anatomy.md). A language earns a skill when it
has a _characteristic_ silencer, not merely a linter.

## Prior art

Shaped by [mattpocock/skills](https://github.com/mattpocock/skills) and
[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills), which
demonstrated that agent skills work best as a coherent set with one thesis
rather than a personal grab bag.

## License

MIT
