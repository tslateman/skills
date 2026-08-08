# Contributing

## What belongs here

Judgment skills — each asks a question that a passing build, a clean diff, or a
readable draft does not answer.

A skill belongs here when it applies a named framework to a decision someone
actually faces, and when it says what it is _not_ for. A skill that only wraps a
tool invocation, or that duplicates a question an existing skill already asks
better, belongs somewhere else.

The `audit/` group carries a stricter thesis of its own: **local-fix debt**, the
minimal edit that clears a failure signal without fixing its cause. See
[docs/local-fix-debt.md](docs/local-fix-debt.md).

## Where a skill goes

`skills/` holds seven groups. Place a new skill in the one whose question it
answers, and read that group's `README.md` first — if the skill does not fit
the sentence at the top of it, it belongs in a different group.

| Group        | Owns                                                 |
| ------------ | ---------------------------------------------------- |
| `audit/`     | Inspecting work that exists, reporting what is wrong |
| `craft/`     | Whether code survives the next change                |
| `navigate/`  | Finding your way around unfamiliar code              |
| `writing/`   | Whether prose is ready to publish                    |
| `shape/`     | Deciding what to build                               |
| `draw/`      | Making the picture                                   |
| `workspace/` | Controlling the session and its artifacts            |

Adding a group means editing the `skills` array in
`.claude-plugin/plugin.json` — Claude Code scans only the declared directories,
so an undeclared group is invisible. Add the group `README.md` in the same
commit.

## Adding a language

A language earns a skill when it has a **characteristic silencer** — the one
edit an agent reaches for when that language pushes back. Not merely a linter;
every language has a linter.

Before writing, answer these:

1. What does this language enforce that others do not?
2. What is the escape hatch it provides for that constraint?
3. What does the escape hatch cost when the code fails in production?
4. What is the restructure axis — the design property the silencer is hiding?
5. What verdict question does this language make sharp?

If any answer is generic, the language does not need its own skill yet.

Then follow [docs/skill-anatomy.md](docs/skill-anatomy.md) exactly. The spine is
the product; a skill that departs from it reads as a different tool bolted on.

## Standards

Borrowed from the repos that shaped this one — skills must be:

- **Specific** — actionable steps, never vague guidance
- **Verifiable** — every finding carries `file:line` and a named fix
- **Battle-tested** — drawn from real reviews, not imagined failure modes
- **Minimal** — under 130 lines; the spine is not padding

Two rules are absolute:

- **Never suggest a silencer as a fix.** A review that recommends `as any`,
  `# type: ignore`, `2>/dev/null`, or a loosened assertion has inverted its own
  purpose.
- **Suspicions are questions; verdicts belong to the judgment pass.** Trigger
  tables must not decide.

## Testing a skill

Run it against real code before opening a PR — ideally agent-written code with
known debt.

Check three failure modes:

- **False floods** — every hit reported as a finding means bucket 1 lacks real
  examples
- **Silence** — nothing reported on code you know is bad means the trigger table
  is too narrow
- **Style drift** — findings that are all formatting means bucket 3 lacks
  concrete restructures

State in the PR what you ran it against and what it found.

## Style

- ATX headers, fenced code blocks with a language identifier
- Tables formatted with `prettier --write`
- Active voice, no needless words, concrete over abstract
- No commentary inside the skill about the skill

## Licensing

MIT. By contributing you agree your work ships under it.
