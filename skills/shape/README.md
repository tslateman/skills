# Shape

**Decide what to build before building it.**

| Skill                         | Question                                     |
| ----------------------------- | -------------------------------------------- |
| `spec-out`                    | You have a vague idea — what is it actually? |
| `brainstorm`                  | You know the goal — what are the options?    |
| `research`                    | What should we use, and what does it cost?   |
| `design`                      | What shape and tone should this take?        |
| `adr`                         | Why did we choose this, for the next reader? |
| `automagic-problem-discovery` | What friction have you stopped noticing?     |

**Start with `spec-out` when you do not know what you want. Start with
`brainstorm` when you know what but not how.**

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
