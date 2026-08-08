# Craft

**Judge whether code will survive contact with the next change, then change it.**

| Skill                             | Question                                                   |
| --------------------------------- | ---------------------------------------------------------- |
| `maintainability`                 | Will this stay cheap to change?                            |
| `ousterhout-software-design`      | Is the module deep, or is the interface doing the work?    |
| `improve-codebase-architecture`   | Which modules are worth deepening?                         |
| `strategic-architecture-analyzer` | Anemic models, leaked invariants, shallow service wrappers |
| `refactor`                        | Execute a named restructure, behavior held constant        |
| `design`                          | Is the interface right before it ships?                    |
| `testing`                         | Which test properties matter, and what do they cost?       |

The pairing that matters: **`maintainability` finds, `refactor` executes.**
Maintainability names the future edits a design taxes and hands cures over;
refactor applies them in small verified steps against a green suite.

Judging a design is not the same as executing a restructure, and neither is a
bug hunt — that lives in [review](../review/README.md).
