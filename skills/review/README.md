# Review

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
| `review-decisions`  | Knowledge-transfer review for a PR or diff                   |
| `vibe-check`        | Whether the whole change holds up, not one debt class        |
| `visual-recap`      | The shape of a large diff, before reading lines              |

**Reach for the language skill** when an agent just made a build go green.
**Reach for `review-decisions`** when the change needs a reader, not a linter — it
captures concerns raised, alternatives rejected, and risks accepted, because
review's real product is knowledge transfer.
**Reach for `visual-recap`** first when the diff is too large to start reading.

## `review-decisions` is not `/code-review`

`/code-review` is Claude Code's built-in: it hunts correctness bugs and
cleanups in a diff, posts inline PR comments with `--comment`, and applies
findings with `--fix`. Nothing here replaces it.

`review-decisions` produces a different artifact. It assumes the bugs are
findable by other means and asks what a future maintainer will need: which
concerns were raised, which alternatives were rejected and why, which risks
were accepted deliberately. Run `/code-review` for defects, `review-decisions`
for the record.

The six language skills each run a mechanical pass with a targeted rule set,
then sort every trigger into **fine**, **mechanical fix**, or **restructure**.
The third is named with its blast radius and never applied without asking.

New language? See [CONTRIBUTING.md](../../CONTRIBUTING.md) — the six share a
fixed spine documented in
[docs/skill-anatomy.md](../../docs/skill-anatomy.md).
