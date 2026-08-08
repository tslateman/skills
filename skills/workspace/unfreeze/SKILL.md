---
name: unfreeze
description: >
  Remove the edit scope restriction set by /freeze. Triggers: "unfreeze",
  "unlock edits", "remove freeze", "thaw".
---

# Unfreeze: Remove Edit Scope Restriction

Remove the directory restriction set by `/freeze`.

## Process

### 1. Check current state

Check if `~/.claude/.freeze` exists. If it doesn't, tell the user there's no
active freeze.

### 2. Remove the freeze file

```bash
rm -f ~/.claude/.freeze
```

### 3. Confirm

Tell the user edits are unrestricted again.
