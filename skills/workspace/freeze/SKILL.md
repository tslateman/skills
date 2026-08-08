---
name: freeze
description: >
  Restrict file edits to a specific directory for this session. Use when
  debugging or doing focused work. Triggers: "freeze edits to", "only edit in",
  "scope edits to", "lock edits to".
argument-hint: "<directory>"
---

# Freeze: Dynamic Edit Scoping

Restrict all file edits (Write, Edit, Bash writes) to a single directory for
the remainder of this session. Agent teams inherit the restriction
automatically — the state lives on disk.

## Process

### 1. Resolve the target directory

Take the argument and resolve it to an absolute path:

```
target=$(realpath "<argument>")
```

If no argument is provided, ask the user which directory to freeze to.

Verify the directory exists. If it doesn't, tell the user and stop.

### 2. Write the freeze file

Write the resolved absolute path to `~/.claude/.freeze`:

```bash
echo "$target" > ~/.claude/.freeze
```

### 3. Confirm

Tell the user:

- Edits are now restricted to `<target>`
- The freeze applies to Write, Edit, and Bash write operations
- Agent teams inherit the restriction
- Use `/unfreeze` to remove the restriction
- The freeze clears automatically when the session ends
