# Craft

**Judge whether code will survive contact with the next change, then change it.**

The largest group, and deliberately so — this repo's center of gravity is code
judgment. Nine skills across four jobs: judge it, learn it, change it, prove it.

## Judge

| Skill                           | Question                                               |
| ------------------------------- | ------------------------------------------------------ |
| `maintainability`               | Will this diff stay cheap to change?                   |
| `improve-codebase-architecture` | Which modules across the codebase are worth deepening? |
| `domain-model`                  | Does the domain own its own invariants?                |
| `ousterhout-software-design`    | Reference: what makes a module deep?                   |

**The three judges differ by scope, not by taste.** `maintainability` takes a
diff or a module and ranks findings by the future edits each one taxes.
`improve-codebase-architecture` takes a whole tree and returns the deepening
candidates worth the effort. `domain-model` takes the business rules and asks
whether the code holding the state also holds the rules about it — the only one
carrying a DDD lens rather than an Ousterhout one.

`ousterhout-software-design` is **not a fourth judge.** It is the principles the
other three cite, for writing code or looking up a term.

## Change

| Skill       | Question                                                  |
| ----------- | --------------------------------------------------------- |
| `tidy`      | Is this cleanup worth it, and does it go before or after? |
| `refactor`  | Execute a named restructure, behavior held constant       |
| `deprecate` | Should this code exist at all, and how does it come out?  |

**Split by size and justification.** A tidying is minutes, needs no mechanics
and no test changes, and is priced by whether you will be back here soon. A
refactoring is named, follows published mechanics, and is verified step by step
against a green suite. Needing the catalog means you left `tidy`.

Both obey Beck's two hats: structure and behavior are separate commits, always.

**`deprecate` is the third verb: removal.** `tidy` and `refactor` both assume
the code stays. `deprecate` asks whether it should, then retires it against
Hyrum's Law — with enough callers, every observable behavior is depended on,
including the ones you never promised. Schemas and shared symbols come out by
expand, migrate, contract, never by changing a form in place.

## Prove

| Skill        | Question                                                  |
| ------------ | --------------------------------------------------------- |
| `testing`    | Which test properties matter here, and what do they cost? |
| `test-first` | Did the test fail first, and for the right reason?        |
| `legacy`     | How do I get this under test without changing it first?   |
| `observe`    | Can you tell what it did in production?                   |

`testing` chooses what to cover. `test-first` fixes the order — a test written
after the code it checks encodes that code's bugs as the specification, so the
run order is the whole discipline. `legacy` is the entry point when there are no
tests at all: characterization first, improvement never on the way in.

**The suite proves it before it ships; `observe` proves it after.** Its first
move is the same one `testing` makes: name the questions worth answering before
choosing what to capture. Two to four questions an on-call engineer will ask,
written down, or you log everything and learn nothing. Done when an induced
failure in staging can be located through telemetry alone, without opening the
source.

`test-review` in [review](../review/README.md) is the audit half — it asks
whether an existing suite can fail at all.

## The through-line

**The judges find, `refactor` and `tidy` execute, and the prove skills supply
the baseline that makes execution safe.** `refactor` refuses to start without a
green suite; when there is none, `legacy` is where it sends you.

Judging a design is not the same as executing a restructure, and neither is a
bug hunt — that lives in [review](../review/README.md). Deciding what to build
at all lives in [shape](../shape/README.md).
