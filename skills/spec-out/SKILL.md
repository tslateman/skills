---
name: spec-out
description: This skill should be used when the user asks to "spec out", "spec this out", "help me spec", "help me clarify", "I have a vague idea", "help me think through this initiative", "what should I be considering", or wants to turn an ambiguous topic into a clear specification. Also triggers on "I'm not sure what I want yet", "let's figure this out", or "ask me questions about".
argument-hint: "<topic, initiative, or plan to clarify>"
---

# Spec Out

Turn ambiguous topics into clear specifications through structured questioning. The interviewer asks; the user answers. The output is a concise spec the user can act on.

## Process

### 1. Establish Scope

Read any context the user provides (files, links, prior notes). Then ask one opening question with multiple-choice options:

> "In one sentence, what are you trying to accomplish?"

Provide 3-5 concise options plus an open-text option. Make the top option your recommended default. Keep labels short.

This anchors the interview. Do not proceed until the scope is stated.

### 2. Interview Rounds

Run 3-4 rounds of questions. Each round has a focus area and 2-3 questions. Each question should offer multiple-choice options with an open-text option. Wait for the user to answer before moving to the next round.

**Round structure:**

| Round | Focus              | Goal                                       |
| ----- | ------------------ | ------------------------------------------ |
| 1     | Why                | Motivation, success criteria, who benefits |
| 2     | What               | Scope boundaries, deliverables, non-goals  |
| 3     | How                | Constraints, dependencies, known risks     |
| 4     | When (if relevant) | Sequencing, milestones, deadlines          |

**Question style:**

- Ask open questions first, then tighten with closed ones.
- Reflect back what you heard before asking the next question ("So the core problem is X. Given that...")
- Surface contradictions gently ("Earlier you said A, but this implies B. Which takes priority?")
- Ask "What are you explicitly not doing?" in every interview. Non-goals prevent scope creep.
- Provide 3-5 options per question plus an open-text option. Make the first option your recommended default.

### 3. Synthesize

After the final round, produce a structured spec:

```
## Spec: [Title]

### Problem
[1-2 sentences: what's broken or missing]

### Goal
[1 sentence: the desired outcome]

### Success Criteria
- [Measurable condition 1]
- [Measurable condition 2]

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

### 4. Confirm

Present the spec and ask: "Does this capture what you mean? Anything to add, cut, or correct?"

Iterate once if needed, then finalize.

## Guidelines

- Stay in interviewer mode. Ask questions; do not propose solutions unless asked.
- Keep rounds short. Two good questions beat five mediocre ones.
- If the user's answers reveal the scope is larger than expected, name it: "This sounds like it might be two separate initiatives. Want to split it?"
- Adapt the round structure to the topic. A technical plan needs more "How"; a strategic initiative needs more "Why."
- If the user already has a doc or plan file, read it first and skip questions it already answers. Focus on gaps.

## See Also

- `/brainstorm` — Generative counterpart; use before spec-out to explore the solution space, or after to brainstorm approaches within scoped constraints
- `/research` — Evidence-gathering companion; use to validate assumptions surfaced during the interview
- `/design` — Implementation companion; use when the spec is done and needs structural shape
- `skills/FRAMEWORKS.md` — Full framework index
