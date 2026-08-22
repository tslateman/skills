---
name: deprecate
description: Decide whether code should still exist, then remove it without breaking the callers who depend on it — including the behaviors you never promised. Covers the deprecation decision, advisory vs compulsory, and the expand-migrate-contract sequence for schemas and shared symbols. Use when sunsetting a feature, consolidating duplicate implementations, removing code nobody owns, or on "deprecate this", "can we delete this", "migrate off X". Do not use to restructure code you are keeping — that is refactor.
argument-hint: "[the system, API, or feature to sunset]"
---

# Deprecate — Removing Code That Stopped Earning Its Keep

Code is a liability. Every line carries tests to maintain, dependencies to bump,
security patches to apply, and load on everyone who reads nearby. The value is
the behavior, never the lines. Most teams are good at adding and bad at
removing, so the liability compounds quietly.

Removal is harder than it looks because of **Hyrum's Law**: with enough users,
every observable behavior of your system gets depended on by somebody, including
the bugs, the timing quirks, and the things you never documented. That is why
deprecation is a migration you perform, not an announcement you publish.

## Use this vs. its neighbors

- Restructure code you are keeping → `refactor`.
- Small cleanup before an edit → `tidy`.
- Get untested code safe to touch → `legacy`.
- Decide which modules deserve deepening → `improve-codebase-architecture`.
- Decide whether code should exist at all, and retire it → here.

## The decision

Answer these before touching anything. A no at step 3 ends the exercise.

1. **Does it still provide unique value?** If yes, maintain it.
2. **Who depends on it?** Quantify the scope before promising a date.
3. **Does a replacement exist?** If not, build it first. Never deprecate
   without an alternative.
4. **What does migration cost each consumer?** Trivially automated means do it
   for them. Manual and expensive gets weighed against step 5.
5. **What does _not_ deprecating cost?** Security exposure, engineer time, and
   the drag the extra complexity puts on everything near it.

## Advisory or compulsory

| Type           | When                                                                    | Mechanism                                           |
| -------------- | ----------------------------------------------------------------------- | --------------------------------------------------- |
| **Advisory**   | The old system is stable and migration can happen on the caller's clock | Warnings, docs, nudges. No deadline.                |
| **Compulsory** | Security exposure, blocked progress, or unsustainable maintenance       | A dated removal, with migration tooling you provide |

**Default to advisory.** Compulsory is a cost you impose on other people, so it
has to be earned by the maintenance burden, and it obliges you to ship the
tooling and the guide. A deadline without tooling is not a plan.

**The churn rule:** if you own the thing being deprecated, you own the
migration. Either migrate the callers yourself or ship a change that requires no
migration. Announcing a removal and leaving callers to work it out is how a
deprecation becomes everyone else's outage.

## The sequence

1. **Build the replacement.** It covers the critical cases, has a migration
   guide, and is proven in production rather than in theory.
2. **Announce.** State status, replacement, reason, and whether a removal date
   exists. Say which behaviors are deliberately not carried over.
3. **Migrate consumers one at a time.** For each: find every touchpoint, switch
   it, verify behavior matches, drop the old references, confirm no regression.
4. **Remove.** Only once usage is provably zero — from metrics and dependency
   analysis, not from belief. Delete the code, its tests, its config, and its
   deprecation notices together.

## Patterns

**Strangler.** Run both, route traffic across in stages (canary, half, all),
remove the old one when it serves nothing. Best when you can measure traffic.

**Adapter.** Keep the old interface, back it with the new implementation.
Callers migrate on their own schedule because nothing they see changed.

**Expand, migrate, contract.** For a schema or a shared symbol, where the data
is the one thing a rollback cannot undo. The failure is coupling the shape
change to the code change: rename a column in the release that starts using the
new name, and during rollout old and new code run together, one of them querying
something that no longer exists.

```text
EXPAND ─────────────→ MIGRATE ─────────────→ CONTRACT
add the new form,     backfill, and          drop the old form once
nullable, beside      dual-write both        nothing reads it, in a
the old one           from the app           separate later deploy
```

Never change a form in place. Each phase ships on its own, and old and new code
are both valid at every point in between. That property is what makes the
sequence safe, and it is the reason contract is a separate deploy rather than a
tidy-up at the end of the migrate one.

## Rules

1. **No replacement, no deprecation.** Removing the only way to do something is
   a feature deletion; call it that and decide it on those terms.
2. **Zero usage is measured, not assumed.** "Nobody calls this" is a hypothesis
   until metrics or dependency analysis agree.
3. **Undocumented behavior still counts as a contract.** Hyrum's Law does not
   care what you promised.

---

Adapted from `deprecation-and-migration` in
[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) (MIT).
