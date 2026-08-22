# Phase Boundaries

When to continue, clear, hand off, delegate, or compact — and why the answer is
only decidable at one moment.

A **phase** is a chunk of work inside a session: the grilling, the
implementation, the QA. The definition is loose on purpose. A phase ends when
you think _"right, that's done"_.

The **phase boundary** is the gap between two of them, and it is the only place
this decision belongs. Mid-phase there is nothing to decide: continue, or split
what remains into subagents. Compacting mid-phase makes the agent lose the
thread it was holding.

## The five moves

| Move         | Does                                                             | Here                               |
| ------------ | ---------------------------------------------------------------- | ---------------------------------- |
| **Continue** | Stay put. No context switch at all.                              | —                                  |
| **Clear**    | Empty the window and start from nothing.                         | `/clear`                           |
| **Hand off** | Write a portable record and seed a session anywhere with it.     | `/lore:handoff`, or a handoff file |
| **Delegate** | Send one task to its own window and get a report back.           | Task tool, agent teams             |
| **Compact**  | Compress this context and seed a fresh session with the summary. | `/compact <instruction>`           |

## The tree

Work top to bottom at the boundary. The first **yes** wins.

**1. Can you continue in this session?**

Two things make the answer yes: the next phase needs this one as a **primary
source**, or enough smart zone remains for the next phase to fit. Design →
implementation is the standard yes — the implementation wants the reasoning
verbatim, not a summary of it.

Continue costs nothing and loses nothing, so rule it out before anything else.

**2. Is the context irrelevant to what comes next?**

If everything here — the exploration, the decisions, the dead ends — is
disposable, `/clear`. It is the cheapest move on the board: instant, and it
hands back the whole window. It is not terminal either, since the old session
stays resumable.

The cost of getting this one wrong is one-way. Clear a _relevant_ context and
you lose the **why** behind what you built. Reading the diff back does not
return it.

**3. Does something need to travel?**

Handing off is narrow. It earns its cost only when you are:

- swapping harness (Claude → Codex),
- moving to a different directory or repo,
- sending the work to a person,
- or forking a side task you found mid-phase without derailing what you are on.

That list is the whole clause. What a handoff buys is **portability**. If
nothing is travelling, you do not need it.

**4. Can the task run unattended?**

Scoped tightly enough to run with you away from the keyboard, no steering? Send
it to a subagent and leave this session untouched. Automated review is the
standard case: the agent reads the diff and reports, and you are not needed
while it does.

**5. Otherwise, compact.**

Relevant context, same harness, same directory, and you need to stay in the
loop. The tree lands here often. Pass an instruction — `/compact we're about to
QA the migration path` — so the summary keeps what the next phase needs.

Compact is the **default, not the first reach**. It sits at the bottom because
the four questions above it are each cheaper or more precise. The failure mode
of starting here is a fresh session that is confidently wrong about a decision
the summary flattened.

## Why the order is the order

Every move except **Continue** converts a **primary source** into a **secondary
source**: the session as it happened, replaced by an account of it.

```text
primary    the reasoning, the dead ends, the exact words     full, noisy, no room
   │
   └─▶ compact / handoff ─▶ secondary   the account of it    lossy, clean, room to move
```

| Source                        | Information | Noise | Room to move |
| ----------------------------- | ----------- | ----- | ------------ |
| Primary (continue)            | Full        | Lots  | Little       |
| Secondary (compact, hand off) | Lossy       | Less  | Lots         |

That trade is why question 1 comes first. You only pay the lossiness once
staying costs more than it saves.

## The smart zone

The **smart zone** is the window within which a model still reasons sharply,
roughly 150k tokens on frontier models. It is a property of attention, not of
the context limit: a million-token window does not move it, it only delays the
moment you are forced to act.

So question 1 has a second half. Not _will the next phase fit_, but _will it fit
inside the zone where the answers are still good_. A session pushed past it does
not fail loudly; it gets subtly worse, which is harder to notice than a wall.

## Rituals are not moves

Three skills fire at exactly these moments and none of them is a context move.
Run them before you decide, not instead of deciding:

| Skill    | Asks                                        |
| -------- | ------------------------------------------- |
| `/sweep` | What did the agents leave behind?           |
| `/retro` | What did this phase teach that outlives it? |
| `/vamp`  | What is worth playing next?                 |

`/retro` in particular pays for itself right before a lossy move: whatever it
extracts survives the compaction that flattens everything else.

## These are judgement calls

None of the five questions is objective. Each carries taste, and the same
boundary can go two ways on two days. The value is in asking them **in order**,
**at** the boundary rather than in the middle of the work.

---

Adapted from `ask-matt/PHASE-BOUNDARIES.md` in
[mattpocock/skills](https://github.com/mattpocock/skills) (MIT). The smart-zone
and rituals sections are additions.
