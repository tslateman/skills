# Levels

Per-level inclusion rules, where to find the boxes, and how to know a level is done. Simon Brown's C4 model, with the estate level above it.

Rule holding across all of them: **a box appears at exactly one level.** If it belongs at two, the levels are wrong.

---

## Level 0 · System Landscape

Several systems in an estate, with the people who use them. No internals.

**Draw when** the question is "what do we even have", during a re-org, or when scoping ownership across teams.

**Boxes**: whole systems, owned and third-party. **Not**: containers, queues, anything deployable.

**Evidence**: the service catalog, the on-call rotation, the AWS account list, the SSO app list. Where a system has no owner listed, that absence is a finding — record it, do not paper over it.

**Done when** every system a reader could name appears exactly once, and each has an owning team.

---

## Level 1 · System Context

One system in the middle. Around it, every person who uses it and every external system it exchanges data with.

**Boxes**: your system (one box, no internals), people (roles, never named individuals), external systems.

**Not**: containers, databases, internal queues, technology choices. If a reader can tell what language it is written in, the level slipped.

**Evidence**: auth configuration for the human roles, outbound integrations and webhooks, third-party API credentials, the vendor list, inbound callers in gateway or ingress config.

**Sizing**: roughly ten boxes. More means the boundary is drawn too wide — either the system is really several systems, or a landscape diagram is the right level instead.

**Done when** a non-technical stakeholder can read it without asking what a box is.

**Actors people forget**: operations and support staff, other teams' batch jobs and schedulers, the data warehouse pulling extracts, the compliance export, the on-call engineer.

---

## Level 2 · Containers

Inside the system boundary: every separately deployable or runnable thing, plus every datastore. This is the level that earns its keep — for most systems it is the one diagram worth keeping current.

**Boxes**: services and applications, single-page apps, mobile apps, serverless functions grouped by purpose, databases, caches, object stores, message brokers, scheduled jobs.

**Not**: classes, libraries, internal modules, layers. A shared library is not a container — it has no independent runtime. Frameworks are technology annotations, not boxes.

**The test**: could this be deployed, scaled, or restarted on its own? Yes means container. No means it belongs at level 3.

**Evidence**, in descending order of trustworthiness:

1. Deploy manifests — k8s, Terraform, `docker-compose`, serverless configs, Helm charts
2. CI/CD pipeline targets — what actually gets built and shipped
3. Runtime configuration — connection strings, broker topics, service discovery entries
4. Repository layout — weakest, since it reflects intent rather than deployment

**Every box carries its technology**: "Booking API · Python/FastAPI", "Session Store · Redis 7". A container without technology is a wish.

**Done when** you can trace one real request through the diagram and account for every hop, and every datastore in production appears.

---

## Level 3 · Components

Inside **one** container: the major structural groupings and their responsibilities.

**Draw only** for containers your reader owns or is about to change. Drawing it for every container is how map-making becomes the project.

**Boxes**: significant modules, packages, or groupings of related behavior — the units a developer would name when explaining the container.

**Not**: individual classes, functions, or files. If box count passes fifteen, group harder — you are drifting toward level 4.

**Evidence**: package and module structure, import graphs, route and handler registration, dependency injection wiring.

**Done when** a new team member can locate where a given change belongs.

---

## Level 4 · Code

Class or entity diagrams for one component.

**Draw** almost never, and never by hand. The code is already the map at this resolution, and a hand-drawn version is stale at the next commit. Generate on demand from the source when a specific structure genuinely needs discussion, then discard it.

The exceptions worth the effort: a domain model under active design debate, and a state machine whose transitions are the actual subject — and the second one wants a state diagram, not a class diagram.

---

## Marking uncertainty

Any box or relationship inferred rather than verified gets marked as such, visibly, in the diagram itself — not in a footnote. A map that hides its own soft spots is worse than one with gaps, because a reader cannot tell which parts to trust.
