# Craft

**Judge whether code will survive contact with the next change, then change it.**

| Skill                           | Question                                                 |
| ------------------------------- | -------------------------------------------------------- |
| `maintainability`               | Will this diff stay cheap to change?                     |
| `improve-codebase-architecture` | Which modules across the codebase are worth deepening?   |
| `domain-model`                  | Does the domain own its own invariants?                  |
| `ousterhout-software-design`    | Reference: what makes a module deep?                     |
| `refactor`                      | Execute a named restructure, behavior held constant      |
| `testing`                       | Which test properties matter here, and what do they cost |

Three judges, one reference, one executor, one precondition.

**The three judges differ by scope, not by taste.** `maintainability` takes a
diff or a module and ranks findings by the future edits each one taxes.
`improve-codebase-architecture` takes a whole tree and returns the deepening
candidates worth the effort. `domain-model` takes the business rules and asks
whether the code holding the state also holds the rules about it — the only one
carrying a DDD lens rather than an Ousterhout one.

`ousterhout-software-design` is **not a fourth judge.** It is the principles the
other three cite, for writing code or looking up a term.

The pairing that matters: **the judges find, `refactor` executes.** Each judge
hands over a named cure; refactor applies it in small verified steps against a
green suite — which `testing` is there to design.

Judging a design is not the same as executing a restructure, and neither is a
bug hunt — that lives in [review](../review/README.md). Deciding what to build
at all lives in [shape](../shape/README.md).
