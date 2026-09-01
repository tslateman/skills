# Contributing

## What belongs here

Judgment skills — each asks a question that a passing build, a clean diff, or a
readable draft does not answer.

A skill belongs here when it applies a named framework to a decision someone
actually faces, and when it says what it is _not_ for. A skill that only wraps a
tool invocation, or that duplicates a question an existing skill already asks
better, belongs somewhere else.

The `review/` group carries a stricter thesis of its own: **local-fix debt**, the
minimal edit that clears a failure signal without fixing its cause. See
[docs/local-fix-debt.md](docs/local-fix-debt.md).

## Where a skill goes

`skills/` holds seven groups. Place a new skill in the one whose question it
answers, and read that group's `README.md` first — if the skill does not fit
the sentence at the top of it, it belongs in a different group.

| Group        | Owns                                                 |
| ------------ | ---------------------------------------------------- |
| `review/`    | Inspecting work that exists, reporting what is wrong |
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

## Evals

Skills that carry a published eval set hold it in an `evals/` directory beside
`SKILL.md`. **Two formats, chosen by what the skill produces**, not two
conventions competing for the same job.

**Judgment evals** grade a report. Use when the skill's output is prose: a
verdict, a ranked finding list, a recommendation.

```text
evals/
├── evals.json      # skill_name + cases: prompt, expected_output, files, expectations[]
└── fixtures/       # the code the prompt points at
```

Each expectation is one binary, checkable claim about the report. Write them so
a grader never has to weigh partial credit.

**Task evals** grade changed code. Use when the skill's output is a diff.

```text
evals/<case-name>/
├── task.md         # the request, as a user would phrase it
├── criteria.json   # context + weighted_checklist[] scored by category
├── scenario.json   # {"include": ["resources/"]}
└── resources/      # the starting code
```

Categories are `INTENT`, `DESIGN`, `EDGE_CASE`, `INTEGRATION`. Weight `DESIGN`
highest when the skill exists to change how an agent decides, not what it types.

Which format a skill uses is readable from its tree: a judgment set has
`evals/evals.json`, a task set has `evals/<case-name>/task.md`.

Point prompts at fixtures with the `{fixtures}` token rather than a checked-in
path. A runner stages `fixtures/` to a scratch directory and expands the token to
point there, so runs stay hermetic and the set carries no machine-specific paths.

`slop-check` has a set that stays unpublished. Its clean-draft fixture is
real unedited writing about internal systems, so `.gitignore` excludes
`**/slop-check/evals/`. Keep any fixture drawn from private prose out of the
repo the same way.

**Every set needs a negative control** — a case where the right answer is "nothing
to report". Skills that always find something are the failure mode evals exist to
catch, and a suite without one cannot see it.

Seed fixtures with flaws that are unambiguous and verifiable. Run them: a
negative-control fixture whose tests fail, or a seeded bug that is not actually
reachable, silently inverts what the eval measures.

## Style

- ATX headers, fenced code blocks with a language identifier
- Tables formatted with `prettier --write`
- Active voice, no needless words, concrete over abstract
- No commentary inside the skill about the skill

## Licensing

MIT. By contributing you agree your work ships under it.
