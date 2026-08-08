# Skill Anatomy

Every skill in this repo follows one spine. A new language skill that departs
from it will read as a different product.

## Frontmatter

```yaml
---
name: <language>-review
description: >
  Review <Language> code for agent-typical anti-patterns: <the three or four
  characteristic silencers, named concretely>. Runs <linter> with a targeted
  rule set, then judges each trigger with a <lens> lens. Use when: reviewing
  agent-written <Language>, before committing <Language> changes, or on
  "<language> review", "review this <language>", "<linter> pass". For generic
  bug hunts use /code-review.
argument-hint: "[path or package to review, defaults to working-tree changes]"
---
```

The description carries three jobs: it names the silencers (so the model matches
on the symptom, not the language alone), it names the trigger phrases, and it
names what this skill is _not_ for. Skip the third and the skill fires on every
review request.

## Title and thesis

```markdown
# <Language> Review — <Audit Name>

<Two to four sentences: the pressure this language applies, the specific
silencer it offers in response, and what the debt costs when it surfaces.
End with: "This review hunts that debt class specifically.">
```

The audit name is the language's own lens, not a generic label — Local-Fix Debt
for compiled and typed languages, Silent Failure for shell, Falsifiability for
tests. The name tells the reader what is being measured.

Do not open with what the skill does. Open with why the debt exists.

## Context

```markdown
## Context

Changed files:
!`git diff --name-only HEAD 2>/dev/null | grep '\.<ext>$' || echo "(not a git repo or no changed .<ext> files — review the given path instead)"`
```

The fallback message matters. Without it, a non-git directory produces an empty
block and the model invents a scope.

## Process

Four steps, always in this order.

### Step 1: Scope

Resolve `$ARGUMENTS`, then changed files, then ask. One line stating what
context each finding needs — error contract, ownership, type flow, control
flow — so the model reads whole files rather than grepped lines.

### Step 2: Mechanical Pass

The linter invocation with a rule set targeted at _this debt class_, not the
project's default set. Annotate why each rule earns its place.

Then the escape clause: **if the project pins its own config, run that instead
and say so.** A review that overrides a team's deliberate configuration is
noise.

Then the trigger table — the greps the linter cannot judge:

```markdown
| Trigger    | Suspicion                                         |
| ---------- | ------------------------------------------------- |
| `<syntax>` | <The question this raises, phrased as a question> |
```

Suspicions are questions, never verdicts. The verdict is Step 3's job.

### Step 3: Judgment Pass

Three buckets, always in this order and always with this framing:

1. **Fine** — with two concrete examples of hits that are _not_ findings
2. **Mechanical fix** — with three or four concrete rewrites
3. **`<Lens>` restructure** — named for the language's own axis (error-contract,
   ownership, type, failure-handling, coverage), with concrete restructures and
   their blast radius. Closes with: _"Do not apply it without asking — this
   bucket is why the review exists."_

Then the aggregation rule, restated in the language's own terms:

> A repeated trigger is one finding, not many: `<concrete example>` point at
> `<the one underlying design gap>`.

Bucket 1 needs real examples or the review reports everything. Bucket 3 needs
real examples or the review reports nothing but style.

### Step 4: Report

Findings with `file:line`, bucket, one-sentence why, suggested fix. Then a
one-paragraph verdict phrased as a **question this language makes sharp**:

- Go — does the error arrive with a cause chain or as an orphaned string?
- Python — does this fail loudly at the boundary, or quietly downstream?
- Rust — is this code compile-shaped or design-shaped?
- TypeScript — do the types describe the data, or what tsc was told to accept?
- Shell — when this script fails, does anyone find out?
- Tests — if someone broke this code tomorrow, would this suite notice?

End with counts: `N fine / N mechanical / N restructure`.

Then the apply clause: bucket 2 applied directly and verified with the linter
plus the test suite; bucket 3 gets a plan first.

## Rules

Three or four, each one line. The first three are fixed in shape:

1. **Never suggest `<the silencers>` as a fix.** Non-negotiable — a review that
   recommends the anti-pattern it hunts is worse than no review.
2. **`<Tool>` passing is the floor, not the verdict** — with one clause on why
   the tool is blind here.
3. **Judge `<the ambiguous trigger>` by `<the real criterion>`, not by `<the
easy proxy>`.**

Add a fourth only for a genuine platform or ecosystem constraint, the way
`shell-review` adds macOS BSD-vs-GNU testing.

## Placement

Review skills live in `skills/audit/`. The group is declared in the `skills`
array of `.claude-plugin/plugin.json`; a skill in an undeclared directory is
never discovered.

## Checklist for a new language

- [ ] The language has a _characteristic_ silencer, not merely a linter
- [ ] The silencer is what an agent reaches for under failure pressure
- [ ] A standard linter exists and can be given a targeted rule set
- [ ] The restructure bucket has a real name on the language's own axis
- [ ] The verdict question is one this language makes sharp
- [ ] Bucket 1 examples are drawn from idiomatic code, not straw men
- [ ] Under 130 lines
- [ ] Filed under `skills/audit/`, and that group is declared in `plugin.json`
