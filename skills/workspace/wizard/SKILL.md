---
name: wizard
description: Generate an interactive bash wizard that walks a human through steps only a human can take — provisioning infrastructure, pasting credentials shown once, clicking through an unfamiliar third-party dashboard, running a one-off migration or cutover. Ships a tested library so only the stages need authoring. Use when an agent hits a wall only the user can pass, or on "write me a setup script", "walk me through this setup", "wizard for X". Do not use for steps the agent can perform itself, or for a repeatable build task — that is a project script.
argument-hint: "[the procedure to wizard, defaults to asking]"
---

# Wizard — Procedures Only a Human Can Run

Some steps cannot be delegated. A dashboard needs someone logged into it, a
secret is displayed once and must be pasted, a cutover needs a person willing to
accept the consequences. The agent stalls there, and the human pays twice: once
doing the procedure, and again re-explaining it to the next agent that stalls in
the same place.

A wizard moves the procedure out of conversation and into a script. It opens
each URL, says exactly what to click, captures the value, writes it where it
belongs, and confirms before anything irreversible. Written once, run by anyone,
and the next agent reads the script instead of asking.

## Use this vs. its neighbors

- The agent can run the step itself → let it. This skill is for the human in the
  loop, not for work the agent is avoiding.
- A repeatable build or task → a project script or Makefile target.
- Deciding what the setup should be before scripting it → `/spec-out`.
- Proving a UI change works → `/demo`.

## The library is already written

[template.sh](template.sh) solves the interaction: a stage counter, screen
clearing so only the current step is visible, cross-platform URL opening
(including WSL), hidden entry for secrets, idempotent `.env` upserts,
`gh secret` and `gh variable` writes, an abort path, and a closing summary
naming what was written and what still needs doing by hand.

Everything above the `STAGES` marker is identical in every wizard. **Never
hand-edit it.** That sameness is why the second wizard feels like the first.

| Helper                   | Does                                                                 |
| ------------------------ | -------------------------------------------------------------------- |
| `banner "Title"`         | Opening frame; call once before the first stage                      |
| `stage "Name"`           | Clears the screen, announces the step, advances the counter          |
| `say` / `step` / `note`  | Instruction line, browser action, aside                              |
| `warn` / `fail`          | Flag a problem; `fail` aborts on a blocker no later stage survives   |
| `open_url URL`           | Opens it in the human's browser                                      |
| `ask KEY "Prompt"`       | Reads a visible value into `$KEY`, offering the current `.env` value |
| `ask_secret KEY "..."`   | Same, with input hidden                                              |
| `write_env KEY VALUE`    | Upserts into `.env`; safe to re-run                                  |
| `set_secret` / `set_var` | Writes a GitHub Actions secret or variable via `gh`                  |
| `pause` / `confirm`      | Wait for acknowledgement; `confirm` is a y/N gate                    |
| `finish`                 | Closing summary                                                      |

## Process

### 1. Scope the procedure

Read the repo before asking anything. Every manual step and every captured value
is usually already written down somewhere:

- **Setup**: `.env`, `.env.example`, `.env.*`, `README`, `docker-compose*`,
  framework config, and `.github/workflows/*` — each `secrets.*` and `vars.*`
  reference is a value the wizard must produce.
- **Migration or cutover**: the current state, the target state, and every
  irreversible action between them.

Then show the ordered stage list and the values each produces, and confirm. The
user may add, drop, or reorder.

**Done when** every stage is named in order, and each value has (a) where the
human gets it, (b) where it is written — `.env`, a GitHub secret, both, or
nowhere, since some stages are pure actions — and (c) whether it is secret.

### 2. Map each stage's journey

Write the precise path a human follows: which URL, what to do there, where the
value appears. "Dashboard → Developers → API keys → Reveal test key → copy."

Where the current UI or exact command is unknown, **say so and check the docs or
ask**. An invented click path is worse than no wizard: it strands the human
mid-procedure with no way to tell whether they or the script is wrong.

**Done when** every stage traces to instructions a stranger could follow.

### 3. Author the stages

Copy `template.sh` to the target path, replace the example stage with one
`stage` per step in dependency order, and set `TOTAL_STAGES` to match.

Hold the bar the library sets:

- `open_url` **before** asking for the value that page shows.
- `ask_secret`, never `ask`, for anything secret.
- `write_env` every persisted value.
- `set_secret` only what CI actually reads.
- `confirm` before every irreversible action.
- One focused task per `stage` — each one clears the screen, so anything the
  human still needs must not have scrolled away.

### 4. Verify and hand off

- `bash -n <script>`, then `shellcheck` if available.
- `chmod +x <script>`.
- **Do not run it end to end**: it opens browsers and blocks on human input.
  Trace it statically instead — every value from step 1 is captured and lands
  where step 1 said, and every `set_secret` name matches a `secrets.*` reference
  in CI exactly.
- Tell the user how to run it.

## Lifespan

A wizard is ephemeral by default: built for one run, written to a scratch or
`scripts/` path, deleted when the job is done.

Commit it only when the setup path is one the next person will also walk. Then
link it from the README, so they run the script instead of asking an agent to
reconstruct it.

---

Adapted from [mattpocock/skills](https://github.com/mattpocock/skills) (MIT).
The library gains a `fail` abort path; the rest of `template.sh` is upstream.
