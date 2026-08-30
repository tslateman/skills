# Shape

**Decide what to build before building it.**

| Skill                         | Question                                       |
| ----------------------------- | ---------------------------------------------- |
| `spec-out`                    | You have a vague idea — what is it actually?   |
| `end-state`                   | What is the finished thing, and in what order? |
| `slice`                       | The spec exists — what are the units of work?  |
| `brainstorm`                  | You know the goal — what are the options?      |
| `research`                    | What should we use, and what does it cost?     |
| `design`                      | What shape and tone should this take?          |
| `adr`                         | Why did we choose this, for the next reader?   |
| `automagic-problem-discovery` | What friction have you stopped noticing?       |

**Start with `spec-out` when you do not know what you want. Start with
`brainstorm` when you know what but not how.**

**`end-state` sits between them.** `spec-out` decides what to build; `end-state`
writes the finished thing at the layer where disciplines converge, then peels it
into a release ladder where every rung names what it enables _and_ what it
defers. That deferred column is what separates a slice of a known whole from an
MVP with an unbounded heap behind it.

**`slice` runs last.** `spec-out` decides what to build; `slice` turns one
release into tasks that can be picked up — each cutting through every layer so it is
demonstrable alone, each declaring what blocks it and which command proves it.
The wide mechanical refactor is its exception: no single slice lands green, so
it sequences expand, migrate, contract instead.

The two decompose differently on purpose: `brainstorm` runs independent lenses
in parallel, `spec-out` runs sequentially because each round builds on the last
answers. Diverge before you converge, and never in the same pass.

`design` commits to a direction before implementation — purpose, tone,
constraints, and the one thing worth getting right — for interfaces, components,
and APIs alike. It asks what a thing should be, not whether it will last; that
second question is [craft](../craft/README.md).

`automagic-problem-discovery` inverts the direction — instead of shaping work
you brought, it audits for repetition you stopped noticing, then builds one fix
completely.
