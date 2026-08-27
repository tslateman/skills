# skills

Skills for coding agents, grouped by what they own.
[skills/FRAMEWORKS.md](skills/FRAMEWORKS.md) maps them to the frameworks and
authorities they apply.

## Install

```
/plugin marketplace add tslateman/skills
```

<details>
<summary><strong>Any other agent</strong></summary>

Skills are plain Markdown with YAML frontmatter and work anywhere skills, rules,
or instruction files are supported.

```bash
npx skills@latest add tslateman/skills
```

The groups are real directories, so take one at a time. `skills/review` alone is
a complete thing if the review suite is all you want.

Cursor: copy any group into `.cursor/skills/`.
Gemini CLI: `gemini skills install https://github.com/tslateman/skills.git --path skills/review`

</details>

`/voice` needs a corpus you supply at `$VOICE_TRAITS`, or
`~/.config/voice-traits.md` when that is unset.

`/slop-check` and `/ste` use a deterministic scanner when one is on `PATH`, and
report judgment-only findings when none is. Nothing here needs installing.

## Groups

| Group                                   | Owns                                      |
| --------------------------------------- | ----------------------------------------- |
| [review](skills/review/README.md)       | What is wrong with work that exists       |
| [craft](skills/craft/README.md)         | Whether code survives the next change     |
| [navigate](skills/navigate/README.md)   | Finding your way around unfamiliar code   |
| [writing](skills/writing/README.md)     | Whether prose is ready to publish         |
| [shape](skills/shape/README.md)         | Deciding what to build                    |
| [draw](skills/draw/README.md)           | Making the picture                        |
| [workspace](skills/workspace/README.md) | Controlling the session and its artifacts |

Each group README names what it owns and which skill to reach for.
`.claude-plugin/plugin.json` declares every group, so Claude Code discovers every skill.

The `review` group argues a thesis of its own, **local-fix debt**: the minimal
edit that clears a failure signal without fixing its cause. See
[docs/local-fix-debt.md](docs/local-fix-debt.md).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and
[docs/skill-anatomy.md](docs/skill-anatomy.md). Review skills follow a fixed
spine; a new language earns one when it has a _characteristic_ silencer, not
merely a linter.

## Prior art

Shaped by [mattpocock/skills](https://github.com/mattpocock/skills) and
[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills).
`/technical-writing`, `/blast-radius`, `/arena`, and the verification pair are
adapted from [pstack](https://github.com/cursor/plugins/tree/main/pstack) by
Lauren Tan, MIT.

Supersedes [duet](https://github.com/tslateman/duet), whose skills were migrated
here after a utilization pass over a month of session transcripts.
