# Writing

**Decide whether prose is ready to go out under your name.**

| Skill               | Question                               |
| ------------------- | -------------------------------------- |
| `technical-writing` | What kind of document is this?         |
| `prose`             | Is it clear and as short as it can be? |
| `slop-check`        | Could anyone have written this?        |
| `cite-or-cut`       | Can every claim name its evidence?     |
| `voice`             | Did **you** write this?                |
| `ste`               | Can the reader execute it?             |
| `narrate`           | Can you explain what you just built?   |
| `bro`               | Can the reader understand it?          |

**`technical-writing` runs first, and only for documents.** It picks the
Diátaxis mode — tutorial, how-to, reference, explanation — before anyone argues
about sentences, because a how-to that keeps teaching is broken at a level no
line edit reaches. It summarises the STE instruction rules; `ste` is the deeper
authority when the text is a procedure.

**Order matters after that.** `slop-check` scores and deliberately refuses to rewrite;
`prose` is the fixing half. Run slop-check first — a draft failing on
genericness fails `voice` too, and its findings are cheaper to fix.

`cite-or-cut` runs on the claims, not the sentences. `slop-check` catches the
vocabulary of overclaiming; this one catches a clean sentence that asserts
something the writer never checked. Run it on anything that argues a position.

`voice` judges against a corpus you supply at `$VOICE_TRAITS`, or
`~/.config/voice-traits.md` when that is unset. It
ships the taxonomy, never anyone's traits. Derive your own before first use.

`ste` is the odd one: ASD-STE100 controlled English for text a reader
_executes_ rather than considers. It strips nuance by design, so keep it away
from anything that argues a position.

`slop-check` refuses to score `ste` and `bro` output, because both mandate
patterns it penalizes.
