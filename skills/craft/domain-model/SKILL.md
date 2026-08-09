---
name: domain-model
description: Judge whether the domain holds its own invariants, applying Evans' Domain-Driven Design and the functional-core/imperative-shell split. Use when business rules sit in controllers or services, when data classes are passive property bags mutated from outside, when callers must sequence init/validate/save to stay consistent, or when testing a business rule needs a database mock. Names the aggregate that should own each invariant. Do NOT use to judge how a diff will age (that is maintainability) or to sweep a codebase for deepening candidates (that is improve-codebase-architecture).
---

# Domain Model

Answers one question: does the code that owns the state also own the rules about that state? Where it does not, business logic has been transliterated into procedural scripts and the data left passive. This skill locates the invariants and names the aggregate that should hold them; it never executes the restructure.

## Use this vs. its neighbors

- Judge how a design or diff will age, ranked by future edit cost -> `maintainability`.
- Sweep a whole codebase for shallow modules worth deepening -> `improve-codebase-architecture`.
- Look up the depth and information-hiding principles themselves -> `ousterhout-software-design`.
- Execute a named restructure with behavior held constant -> `refactor`.
- Judge whether the domain enforces its own rules, with DDD names -> here.

## The four tests

Run these against the target files. Each one fails loudly or not at all; there is no partial credit.

1. **The mocking test**: does verifying a business rule require stubbing a database, an HTTP client, or a queue? A rule that cannot be tested without I/O is a rule living outside the domain.
2. **The surface-area test**: does the module expose fine-grained setters instead of one or two entry points per business event? `order.status = "shipped"` is a setter; `order.ship(carrier)` is a business event.
3. **The invariant leak test**: is a domain constraint checked outside the boundary that owns the state? A `if balance > 0` in a route handler is the rule leaking to whoever remembered to write it.
4. **The UI shift test**: would changing an API payload or a wizard's step order force edits to core business rules? The domain must not know the shape of its callers.

## What to hunt

**Anemic models.** Data classes, ORM models, and DTOs that serve as property bags while external services mutate them field by field. The tell is a class with no methods beyond accessors, paired with a `-Manager`, `-Processor`, `-Handler`, or bare `-Service` that does all the deciding. Those name suffixes are the search index, not the finding; a `Service` that owns its invariants is fine.

**Orchestration scripts.** A method that fetches data, branches on that data's behalf, mutates its fields, and calls I/O inline. Five or more sequential steps in one method is the threshold worth reading closely.

**Temporal coupling.** An interface where callers must invoke methods in a precise order to avoid an inconsistent state: `init()`, then `validate()`, then `process()`, then `save()`. Every caller now carries the sequence, and no caller can be checked against it.

**Representable invalid states.** An object that can exist in a state the business forbids: a reservation marked checked-in before it is confirmed. Prefer a type that cannot express the invalid state over a validator that rejects it.

**I/O braided through decisions.** Pure decision logic interleaved with reads and writes. This is the root cause the mocking test detects.

## The target shape

Split each finding's fix into two named halves:

- **Domain aggregate**: pure, zero I/O, owns every invariant over the state it holds. It accepts business events, not field assignments, and rejects transitions the business forbids. Name it after the concept, never after a mechanism.
- **Imperative shell**: loads state, delegates the decision to the aggregate, persists the result, dispatches events. It holds no business rules and makes no branches on domain state.

The split is the deliverable. A finding that names the smell but not the aggregate that should own the invariant is unfinished.

## Output

Open with the architectural risk in two or three sentences: which invariants are unowned, and what that costs.

Then one finding per problem:

- **Name**: the DDD term (anemic model, leaked invariant, temporal coupling, representable invalid state, orchestration script)
- **Site**: `file:line`
- **Failing test**: which of the four tests it fails, and why
- **Owner**: the aggregate that should hold the invariant, and the business event that should be its entry point
- **Cure handoff**: `refactor` with the named restructure, or "accept and note"

Rank by blast radius: an invariant checked in three call sites outranks one checked in a single handler. Where a fix is worth showing, give the before and after as code, not prose.

If the domain already owns its rules, say so plainly and stop. No filler findings.

## Gotchas

- **Framework gravity**: an active-record ORM invites putting persistence on the aggregate. The aggregate stays pure; the shell owns the session.
- **Aggregate sprawl**: one aggregate per invariant set, not one per table. If two objects must change together to stay valid, they are one aggregate.
- **CRUD is fine**: a resource with no invariants beyond field types needs no domain model. Applying this skill to genuine CRUD manufactures ceremony.
