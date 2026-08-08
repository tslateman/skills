---
name: system-map
description: Decompose a system into a shared map at consistent levels of abstraction, using the C4 model. Use when you ask to "map the system", "diagram the architecture", "how does this fit together", "explain our architecture to stakeholders", when onboarding someone to an unfamiliar estate, or when a discussion keeps stalling because two people hold different pictures of the same system. Produces a communication artifact for a named audience, not a quality verdict. Do NOT use to judge a design (that is `ousterhout-software-design` or `maintainability`) or to orient one reader in one module (that is `zoom-out`).
---

# System Map

Break a system into pieces small enough to reason about, at one level of abstraction at a time, for one audience at a time. The map is the deliverable — something a team, a stakeholder, and an adjacent team can all point at and mean the same thing.

This skill describes what exists. It never grades it.

## Use this vs. its neighbors

- Orient one reader in one unfamiliar module -> `zoom-out`.
- Judge whether a design will age -> `maintainability`.
- Judge module depth and interface quality -> `ousterhout-software-design`.
- Render a diagram you have already scoped -> `mermaid` or `excalidraw`.
- Record why the architecture is this way -> `adr`.
- Produce the shared map itself, at C4 levels, for a named audience -> here.

## Preconditions

Name both before drawing anything. Skipping either produces the diagram nobody uses.

1. **The boundary.** What is inside the system under description and what is outside it. "Everything" is not a boundary.
2. **The audience.** Who reads this and what decision it serves. The audience picks the level; the level is not a stylistic choice.

## The levels

| Level | Diagram       | Boxes are                                | Audience                        | Answers                                                |
| ----- | ------------- | ---------------------------------------- | ------------------------------- | ------------------------------------------------------ |
| 1     | **Context**   | People and systems                       | Anyone, including non-technical | Who uses this and what does it talk to?                |
| 2     | **Container** | Deployable/runnable units and datastores | Engineers, ops, architects      | What are the moving parts and how do they communicate? |
| 3     | **Component** | Major groupings inside one container     | The team owning that container  | How is this one part organized inside?                 |
| 4     | **Code**      | Classes, functions                       | Almost nobody                   | Generate on demand; usually skip                       |

**The rule that makes C4 work: one level per diagram.** A frame containing a load balancer, a Kafka topic, and a Python class describes nothing, because no reader knows which questions it answers. When a box does not belong at the current level, it goes in a different diagram, not in a corner of this one.

Most systems need levels 1 and 2. Level 3 is worth drawing for containers your team actually owns. Level 4 is nearly always waste — the code is the map at that resolution, and the diagram is stale on commit.

Above level 1, a **system landscape** diagram maps several systems in an estate. Use it when the question is "what do we even have", and keep it free of internals.

Details and per-level inclusion rules: `references/levels.md`.

## Workflow

1. **Fix scope and audience.** State them in one line each, at the top of the artifact. They stay visible in the output.
2. **Inventory from evidence, not memory.** Containers come from deploy manifests, process definitions, `docker-compose`, k8s manifests, CI configs, and connection strings — not from what the architecture "is supposed to" be. Where evidence is missing, mark the box unverified rather than guessing.
3. **Draw level 1.** Every person who uses the system and every external system it exchanges data with. If the box count exceeds roughly ten, the boundary is too wide.
4. **Draw level 2.** One box per separately deployable or runnable thing, plus each datastore. Every box carries its technology.
5. **Draw level 3 only where it earns its place** — the containers your reader owns or must change.
6. **Label every relationship** with a verb and a protocol: "reads booking events from, via SQS", not "uses". An unlabeled arrow is a claim that two things are related without saying how, which is the least useful thing a diagram can assert.
7. **Validate against something executable.** Trace one real request end to end through the map. Any hop the map cannot explain is a missing box.
8. **Date it and say how it was derived.** A map without a date is trusted forever and correct for a month.

## Notation

Every element: **name**, **type or technology**, **one-line responsibility**. All three, every box, every level.

Every relationship: **direction**, **verb**, **protocol or mechanism**. Draw the direction of the dependency, not the direction the data happens to move.

Keep external systems visually distinct from ones you own — the ownership boundary is the single most decision-relevant line on any of these diagrams.

## Beyond C4

C4 maps **static structure**. When the question is a different shape, the map is a different diagram — say which question you are answering and pick accordingly.

| Question                                    | Map                                 |
| ------------------------------------------- | ----------------------------------- |
| What are the parts and how do they connect? | C4 context/container/component      |
| How does this request actually flow?        | Sequence diagram                    |
| What states can this entity be in?          | State diagram                       |
| What does the data look like?               | ER diagram                          |
| Where does it all run?                      | Deployment diagram                  |
| Who owns what, and where are the seams?     | Landscape plus an ownership overlay |

Rendering syntax, including Mermaid's C4 support and when to fall back to a plain flowchart: `references/rendering.md`.

## Gotchas

- **Mixed levels** is the dominant failure. The tell is a box whose neighbors operate at a different granularity — a class beside a database cluster.
- **The hairball.** If everything connects to everything, the diagram has stopped carrying information. Split by level, or scope to one flow, or accept that the coupling is the finding and hand it to `maintainability`.
- **Drawing the org chart and calling it the architecture.** Conway's Law guarantees the two resemble each other, which is exactly why the map must be built from deploy and call evidence. Where they diverge, that divergence is worth stating explicitly.
- **Aspirational boxes.** The service that is "basically done" is not a container. Draw what runs; annotate what is planned, separately and visibly.
- **Missing actors.** Ops, support, batch jobs, and other teams' schedulers are users of the system. Level 1 that shows only the end customer is incomplete.
- **Silent staleness.** Diagrams decay invisibly, unlike code. Prefer generating what you can from source, keep the rest small enough to be cheap to redraw, and put the derivation method in the artifact.
- **Judgment leaking in.** "This coupling is bad" does not belong on the map. Produce the map, then hand it to a judgment skill. Mixing description and verdict makes stakeholders argue with the picture instead of reading it.
