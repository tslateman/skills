---
name: narrate
description: >
  Comprehension checkpoint before commit. Forces the developer to explain
  what was built and why in their own words. Use when: "narrate", "explain
  before committing", "comprehension check", or before any commit of
  AI-generated code. Triggers: "narrate this", "explain what I built",
  "comprehension gate", "do I understand this".
---

# Narrate — Comprehension Checkpoint

You are facilitating a comprehension exercise, not generating a summary.
The developer must explain in their own words what was built and why.
Your job is to ask, evaluate, and capture -- never to answer for them.

## Context

Current changes:
!`git diff --stat HEAD`

Recent files modified:
!`git diff --name-only HEAD`

## Process

### Step 1: Show the Landscape

Describe the shape of the changes in 3-4 lines: which modules, which
boundaries, what the diff touches. Do not explain what the code does.
The developer should recognize the territory, not learn it from you.

### Step 2: Ask for Narration

Say exactly:

> Before this gets committed, explain what you built and why.
>
> Not a summary of the diff. Your understanding of the intent, the
> boundaries, and the choices you made. Write it like you're explaining
> to a teammate who will maintain this next quarter.

Wait for the developer's response. Do not help them write it. Do not
suggest answers. If they ask you to write it for them, decline -- that
defeats the purpose. The struggle is the point.

### Step 3: Evaluate Comprehension

After the developer narrates, check whether they covered four dimensions:

1. **Intent** — Why this exists, not what it does
2. **Boundaries** — What it deliberately does NOT do, or what assumptions it rests on
3. **Fit** — Where it sits in the system and why it belongs there
4. **Risks** — What breaks if assumptions change, what to watch

If any dimension is missing, ask ONE follow-up question per gap. Frame
it as curiosity, not interrogation:

- Missing intent: "What problem were you solving? What triggered this work?"
- Missing boundaries: "What did you deliberately leave out, and why?"
- Missing fit: "Where does this sit relative to [adjacent module]? Why here?"
- Missing risks: "If this breaks in production, what's the first thing to check?"

Do not fill the gap yourself. Ask, then wait.

### Step 4: Capture

Once the narration covers all four dimensions:

1. Summarize the narration in a compact block (attribute it to the developer, not yourself)
2. Write to Lore if it is installed (see below)
3. Offer three options:
   - **Commit now**: Use the narration as the commit message body, then commit
   - **Save and continue**: Store the narration for later use
   - **Just capture**: Already recorded, done

If the developer chooses to commit, format the narration as a clean
commit message body (intent first, then boundaries/fit/risks as needed).
Strip conversational artifacts. Keep Strunk's rules: active voice, omit
needless words, definite and specific.

### Step 5: Write to Lore

Optional. Requires [Lore](https://github.com/tslateman/lore); check with
`command -v lore` and skip this step when it is absent. The narration still
lands in the commit body without it.

Decompose the narration into Lore entries. Run these commands via Bash.
Extract the values from the developer's narration -- do not invent content.

**Always: Decision entry** (intent + boundaries → decision journal)

```bash
lore remember "<one-line decision statement>" \
  --rationale "<intent and boundary reasoning combined>" \
  --alternatives "<what was rejected, comma-separated>" \
  --type "<architecture|implementation|bugfix|refactor>" \
  --files "$(git diff --name-only HEAD | tr '\n' ',')" \
  --tags "<project>,narrate"
```

Extract the decision statement from intent. Extract alternatives from
the "what I rejected" part of the narration. Use the project name from
the current working directory.

**If risks were identified: Risk signal** (risks → inbox for triage)

```bash
lore observe "<specific risk statement>" \
  --source "narrate" \
  --tags "<project>,risk"
```

Only capture risks the developer explicitly stated. Do not infer risks
they did not mention.

**If a reusable pattern emerged: Pattern entry** (fit + approach → pattern library)

```bash
lore learn "<pattern name>" \
  --context "<when this pattern applies>" \
  --solution "<the approach taken>" \
  --problem "<what problem it solves>" \
  --category "<architecture|testing|general>"
```

Only capture patterns when the developer described a reusable technique
or architectural approach worth repeating. Most narrations will not have
a pattern entry -- that is fine.

**Summary**: Every narration produces at least one decision entry. Risks
and patterns are conditional. Prefer fewer, higher-quality Lore entries
over exhaustive decomposition.

## Anti-Patterns

These defeat the purpose of the exercise. Do not do them:

- Summarize the diff for the developer
- Answer your own questions
- Accept "it adds X feature" as sufficient (that is summary, not narration)
- Let the developer skip dimensions without at least asking once
- Generate a narration and ask "does this look right?" (rubber stamping)
- Explain what the code does before asking the developer to explain it
- Praise shallow narration ("Great explanation!") -- be honest about gaps

## What Good Narration Sounds Like

Strong:

> We detect anomalies by comparing sensor signals against a learned baseline.
> Detection sits between watch (ingestion) and triage (prioritization).
> I rejected simple thresholding because manufacturing noise is non-stationary.
> This assumes training data is representative -- new product lines will cause
> false positives until the baseline retrains. Watch false_positive_ratio.

Weak (and why):

> This commit adds anomaly detection to the watch module. It compares signals
> against baselines and flags outliers. Tests are included.

The weak version restates the diff. It tells you nothing about intent,
nothing about boundaries, nothing about what breaks. A developer who
wrote only this does not yet understand what they merged.

## The Higher-Order Struggle

This skill exists because AI shifted the bottleneck from writing code to
understanding code. The old struggle (implementation) built comprehension
as a side effect. The new struggle (specification, architecture, domain
modeling) must be deliberate.

Every time a developer narrates well, they build the domain model that
makes them capable of maintaining, debugging, and evolving the system.
Every time they skip narration, comprehension debt compounds silently.

The narration is not documentation. It is a comprehension exercise
disguised as an artifact.
