# Writing

**Decide whether prose is ready to go out under your name.**

| Skill        | Question                               |
| ------------ | -------------------------------------- |
| `prose`      | Is it clear and as short as it can be? |
| `slop-check` | Could anyone have written this?        |
| `voice`      | Did **you** write this?                |
| `ste`        | Can the reader execute it?             |
| `narrate`    | Can you explain what you just built?   |
| `bro`        | Can the reader understand it?          |

**Order matters.** `slop-check` scores and deliberately refuses to rewrite;
`prose` is the fixing half. Run slop-check first — a draft failing on
genericness fails `voice` too, and its findings are cheaper to fix.

`voice` judges against a corpus you supply at `~/.claude/voice-traits.md`. It
ships the taxonomy, never anyone's traits. Derive your own before first use.

`ste` is the odd one: ASD-STE100 controlled English for text a reader
_executes_ rather than considers. It strips nuance by design, so keep it away
from anything that argues a position.

`slop-check` refuses to score `ste` and `bro` output, because both mandate
patterns it penalizes.
