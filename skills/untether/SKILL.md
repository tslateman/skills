---
name: untether
description: >
  Remove a cross-project tether from the current session. Triggers: "untether",
  "remove tether", "disconnect project".
argument-hint: "<project | all>"
---

# Process

## 1. Determine scope

- If argument is "all" or no argument given: run `rm -f ~/.claude/.tether`. Confirm "All tethers removed."
- If a specific project name is given: proceed to step 2.

## 2. Remove specific tether

- Remove the exact line matching the project name from `~/.claude/.tether` using `grep -v '^{name}$'`.
- If `.tether` is now empty, remove the file.
- If the project name was not found in `.tether`, say "No tether found for {name}."

## 3. Confirm

Say what was untethered.
