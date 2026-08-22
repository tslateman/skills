---
name: spec-out
description: This skill should be used when the user asks to "spec out", "spec this out", "help me spec", "help me clarify", "I have a vague idea", "help me think through this initiative", "what should I be considering", or wants to turn an ambiguous topic into a clear specification. Also triggers on "I'm not sure what I want yet", "let's figure this out", or "ask me questions about".
argument-hint: "<topic, initiative, or plan to clarify>"
---

# Spec Out

What people ask for and what they want are different things. They ask for a
dashboard because that is what one asks for, not because a dashboard solves the
problem. They say "make it faster" without a number to hit.

The cheapest moment to find that gap is before anything exists. Afterward the
switching cost is real, and the user will rationalize the wrong thing into a
good-enough thing. This skill closes the gap while closing it is free, and hands
back a spec that can be acted on.

## Use this vs. its neighbors

- You know the goal and want options → `brainstorm`.
- You need evidence about a tool or approach → `research`.
- The spec exists and needs structural shape → `design`.
- The decision is made and needs recording → `adr`.
- You do not yet know what you want → here.

## 1. State your hypothesis, with a number

Before asking anything, write your current read in one sentence with an honest
confidence number:

```
HYPOTHESIS: You want to answer "how are we doing?" in standup, and "dashboard"
            was the convention that came to mind.
CONFIDENCE: ~30% — missing who it is for, what "metrics" means here, and what
            success looks like.
```

Below ~70%, the reason is not optional. It tells the user exactly what the
interview has to surface, and it turns the number from a vibe into a claim you
can be wrong about in public.

## 2. Establish scope

Read whatever the user provides first — files, links, prior notes — and skip
every question they already answer. Then ask the opening question:

> "In one sentence, what are you trying to accomplish?"

Offer 3-5 short options plus open text, with your recommended default first.
Do not proceed until the scope is stated.

## 3. Work the frontier

Ask in rounds. Each round asks only questions whose prerequisites are already
settled — never one whose answer depends on another question still open in the
same round. Those belong to a later round. Answers push the frontier outward and
unblock what was waiting.

Every question carries 3-5 options plus open text, recommended default first.
**The options are your guesses.** Reacting to a wrong guess is faster than
generating an answer from nothing, and it puts your assumptions where the user
can correct them. Being visibly willing to be wrong is what stops a polite user
agreeing with you.

Cover these before you stop. They are a checklist, not a schedule — a technical
plan needs more How, a strategic one more Why:

| Area     | Must come out                              |
| -------- | ------------------------------------------ |
| **Why**  | Motivation, success criteria, who benefits |
| **What** | Scope boundaries, deliverables, non-goals  |
| **How**  | Constraints, dependencies, known risks     |
| **When** | Sequencing, milestones, deadlines          |

Ask "what are you explicitly not doing?" in every interview. Silent disagreement
about non-goals is half of all misalignment.

Finding facts is your job, never the user's. When a question needs something
from the filesystem or the tools, go get it rather than asking.

### Listen for want vs should-want

The dangerous answers are the ones that sound like what a thoughtful answer
sounds like. Watch for best-practice talk with no specifics ("scalable", "clean
architecture"), deference to convention ("the way most apps do it"), and the
phrase "I should probably". When you hear one, ask:

> "If you didn't have to justify this to anyone, what would you actually want?"

That question routinely does more work than the previous five.

## 4. Stop when you can predict

The interview is over when you can answer yes to this:

> _Can I predict the user's reaction to the next three questions I would ask?_

That is a checkable test, not a feeling. Running out of rounds is not a reason
to stop, and neither is the user sounding agreeable.

It has a floor. If several rounds in you still cannot predict, that is
information about the ask rather than a reason to grind: say so plainly —
"I've asked six questions and still can't predict your answers; something
foundational is missing, want to step back?"

## 5. Synthesize

```
## Spec: [Title]

### Problem
[1-2 sentences: what's broken or missing]

### Goal
[1 sentence: the desired outcome]

### Success Criteria
- [Measurable condition]

### Scope
**In scope:**
- [Item]

**Out of scope:**
- [Item]

### Approach (if discussed)
[Key decisions or constraints that shape the solution]

### Open Questions
- [Anything unresolved]
```

## 6. Confirm — an explicit yes

Ask: "Does this capture what you mean? Anything to add, cut, or correct?"

These are **not** a yes:

| Answer                        | What it means                                                                                |
| ----------------------------- | -------------------------------------------------------------------------------------------- |
| "Whatever you think is best." | Delegation. They are not confident either — re-ask as a choice between two concrete options. |
| "Sounds good."                | Ambiguous. Ask what they would refine. Silence is not confirmation.                          |
| "Sure, let's go."             | Often a polite exit. Same follow-up.                                                         |

Fold in every correction and restate. Loop until the yes is explicit.

## Guidelines

- Stay in interviewer mode. Ask; do not propose solutions unless asked.
- Two good questions beat five mediocre ones.
- Reflect back what you heard before the next round, and surface contradictions
  gently: "Earlier you said A, but this implies B — which takes priority?"
- If the answers reveal a bigger scope than expected, name it: "This sounds like
  two initiatives. Split it?"

## See Also

- `/brainstorm` — generative counterpart, before or after this
- `/research` — validate assumptions the interview surfaces
- `/design` — structural shape once the spec is done
- `skills/FRAMEWORKS.md` — full framework index
