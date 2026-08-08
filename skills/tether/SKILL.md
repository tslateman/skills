---
name: tether
description: >
  Bridge cross-project context into the current session. Loads a project's
  CLAUDE.md, recent changes, and registry interface so you can work across
  project boundaries. Triggers: "tether", "tether to", "connect to project".
argument-hint: "<project>"
---

# Process

## 1. Resolve the project

- If no argument: read `~/.claude/.tether` and list currently tethered projects. If the file is empty or missing, say "No active tethers." and stop.
- Take the argument as the project name.
- Check `$DEV_ROOT/forge/registry/{name}.yaml` (with `DEV_ROOT` defaulting to `~/dev`) -- if found, read the `path:` field.
- Else check if `$DEV_ROOT/{name}/` exists as a directory.
- If neither, tell the user the project wasn't found and stop.

## 2. Write the tether

- Check if `~/.claude/.tether` already contains the project name (grep for exact match). If so, say "Already tethered to {name}." and stop.
- Append the project name to `~/.claude/.tether` (one name per line).

## 3. Load context

- Read the tethered project's `CLAUDE.md` (first 30 lines) and display a brief summary.
- Run: `git -C {path} log --oneline -5` to show recent commits.
- Run: `git -C {path} branch --show-current` to show active branch.

## 4. Confirm

Say: "Tethered to **{name}** ({branch}). Context will be injected automatically on each prompt."

Note: Tethers clear when the session ends.
