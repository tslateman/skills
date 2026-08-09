---
name: tidy
description: Decide whether a small structural cleanup is worth doing and when it lands, applying Beck's Tidy First? Use when code is awkward to read right before you change it, when a diff mixes cleanup with behavior, or when asking "should I clean this up now or later". Ships the tidyings catalog and the four-way timing decision (never, later, after, first), priced by whether you will be back. Do NOT use for a named restructure needing test-verified steps (that is refactor) or to find what is wrong (that is maintainability).
---

# Tidy

Answers one question: is this worth tidying, and does it go before the change, after it, or not at all? A tidying is a structural change small enough to need no plan and no test changes — the kind that takes a minute and makes the next hour cheaper. This skill prices them; it never mixes one with a behavior change.

## Use this vs. its neighbors

- Execute a named restructure in test-verified steps -> `refactor`.
- Find and rank what is wrong with a design -> `maintainability`.
- Reuse and simplification pass on a just-written diff -> `simplify`.
- Get untested code under a harness before touching it -> `legacy`.
- Decide whether a small cleanup pays, and when it lands -> here.

**Against `refactor`**: size and justification. A refactoring is named, follows published mechanics, and is verified step by step against a green suite. A tidying is smaller than that machinery — no mechanics to follow, no intermediate states worth committing separately. If you need the catalog and the step-by-step verification, you left tidying and entered `refactor`.

## The separation

Beck's rule, and the whole point: **structure and behavior are different changes.** They go in different commits, always, no exceptions for size. A diff that reshapes and re-specifies at once is unreviewable — a reader cannot tell which lines were supposed to change what the code does.

The reviewer's test: reading only the structural commit, could anything a caller observes have changed? If yes, it was not a tidying.

## When

Four options. Pick one deliberately; the default is not "first".

| Timing    | When it applies                                                                         |
| --------- | --------------------------------------------------------------------------------------- |
| **Never** | Code you will not read again. Ugly and untouched costs nothing.                         |
| **Later** | It bothers you but nothing depends on it. Add it to a list and do it when depleted.     |
| **After** | You just changed here and understand it now. Cheapest moment; you already paid to read. |
| **First** | The change you are about to make is genuinely hard to make in the current shape.        |

**Tidy first only when it makes the coming change easier** — that is the sole justification, and it is testable before you start: name the change, then say what the tidying removes from it. If you cannot name the change, the answer is later or never.

**Tidy after is the usual right answer.** Discounted cash flow: a dollar today outweighs a dollar tomorrow, so shipping the behavior first and cleaning second beats deferring the ship. You are also at peak understanding right after the change, and that understanding decays.

## The tidyings

Beck's catalog. Each is minutes, not hours.

| Tidying                                      | Do                                                                            |
| -------------------------------------------- | ----------------------------------------------------------------------------- |
| Guard clauses                                | Lift precondition checks to the top and return early; unnest the body         |
| Dead code                                    | Delete it. Unreferenced code is not documentation                             |
| Normalize symmetries                         | Make things that do the same thing look the same way                          |
| New interface, old implementation            | Write the interface you wish existed; have it call the one that exists        |
| Reading order                                | Reorder within a file so a reader meets things in the order they need         |
| Cohesion order                               | Move things that change together nearer each other                            |
| Move declaration and initialization together | Close the gap between where a variable appears and where it gets value        |
| Explaining variables                         | Name a subexpression; the name carries what a comment would have              |
| Explaining constants                         | Replace the literal with a named constant                                     |
| Explicit parameters                          | Pass what the function uses instead of a bag it reaches into                  |
| Chunk statements                             | Insert a blank line between the parts that do different work                  |
| Extract helper                               | Pull out a coherent block with a name, called from one place                  |
| One pile                                     | Inline several fragments back into one readable block when the split obscures |

**Beck's fourteenth tidying is explaining comments; this repo does not use it.** The `code-comments` rule overrides Beck here, the same way it overrides Ousterhout in `maintainability`. Where Beck would add a comment to explain a fragment, use explaining variables, explaining constants, or extract helper — the name is the explanation. Deleting a comment made redundant by a good name is still a tidying.

## Why it pays

Coupling and cohesion are the measures, and both are about change cost. **Constantine's equivalence**: the cost of software tracks the cost of changing it, and the cost of changing it tracks its coupling — the chance that changing one element forces changing another.

Two elements are coupled with respect to a change if changing one requires changing the other. Coupling is never absolute; it is always relative to a specific kind of change. So the question is never "is this coupled" but "is this coupled to the change I keep making".

Tidying buys **optionality**: structure that lets you make a change later without knowing today which change it will be. That option is worth more when the future is uncertain, and worth less when exercising it is slow. Untidy code is not merely unpleasant; it prices out the options you have not chosen yet.

## Workflow

1. **Name the coming change**, or accept that this is a tidy-after or a tidy-later.
2. **Pick the timing** from the table. Say which and why.
3. **Apply one tidying.** Not all of them, and not everything you can see.
4. **Commit it alone**, structure only, message naming the tidying.
5. **Then the behavior change**, in its own commit.

Batch tidyings only when they are the same tidying applied to sibling sites. Different tidyings go in different commits.

## Gotchas

- **Tidying everything in reach** is the dominant agent failure. Given a file, an agent will tidy the whole file because it can, unpriced. Most of that code will never be read again. Tidy the part the change touches.
- **Mixing the hats.** A cleanup commit that also renames a public method, changes an error type, or reorders a side effect is a behavior change. Split it.
- **Tidying instead of changing.** The tidying is preparation, not the work. If the coming change has not started after several cleanup commits, the tidying became procrastination — Beck's own warning.
- **No test changes.** A tidying that requires editing a test is either not a tidying or not structural. Stop and reconsider which one.
- **Reading order is subjective and cheap to fight over.** If it is contested, it was not worth doing.
