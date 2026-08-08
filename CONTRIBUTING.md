# Contributing

## What belongs here

One thesis: **local-fix debt** — the minimal edit that clears a failure signal
without fixing its cause. See [docs/local-fix-debt.md](docs/local-fix-debt.md).

A skill belongs here when it hunts that debt class in one language or one
artifact type. A skill that reviews code generally, designs a test strategy, or
judges architecture belongs somewhere else.

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
