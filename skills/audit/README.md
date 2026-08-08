# Audit

**Inspect work that already exists and report what is wrong with it.**

Six of these hunt one debt class: **local-fix debt**, the minimal edit that
clears a failure signal without fixing its cause. Each language offers a
different silencer, so each gets its own skill. The argument is in
[docs/local-fix-debt.md](../../docs/local-fix-debt.md).

| Skill               | Scope                                                        |
| ------------------- | ------------------------------------------------------------ |
| `go-review`         | Discarded errors, string-matched handling, leaked goroutines |
| `python-review`     | Blind except, `type: ignore`, `Any`, `.get()` defaults       |
| `rust-review`       | Clone-to-appease-borrowck, bare `unwrap`, `#[allow]`         |
| `typescript-review` | `as any`, non-null assertions, floating promises             |
| `shell-review`      | `2>/dev/null`, missing strict mode, GNU-vs-BSD assumptions   |
| `test-review`       | Tests that cannot fail; language-agnostic                    |
| `review`            | Knowledge-transfer code review for a PR or diff              |
| `vibe-check`        | Whether the whole change holds up, not one debt class        |
| `visual-recap`      | The shape of a large diff, before reading lines              |

**Reach for the language skill** when an agent just made a build go green.
**Reach for `review`** when the change needs a reader, not a linter.
**Reach for `visual-recap`** first when the diff is too large to start reading.

New language? See [CONTRIBUTING.md](../../CONTRIBUTING.md) — the six review
skills share a fixed spine documented in
[docs/skill-anatomy.md](../../docs/skill-anatomy.md).
