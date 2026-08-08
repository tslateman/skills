---
name: shell-review
description: >
  Review shell scripts for agent-typical anti-patterns: 2>/dev/null and
  || true silencing real breakage, missing set -euo pipefail, unquoted
  expansions, unchecked cd before destructive operations, hardcoded /tmp
  paths, GNU-vs-BSD tool assumptions that break on macOS, shellcheck
  disable comments. Runs shellcheck, then judges each trigger with a
  failure-visibility lens. Use when: reviewing agent-written bash or zsh,
  before committing hooks or install scripts, or on "shell review",
  "review this script", "shellcheck pass", "check for silent failures".
  For generic bug hunts use /code-review.
argument-hint: "[script or directory to review, defaults to working-tree changes]"
---

# Shell Review — Silent Failure Audit

Shell scripts fail quietly by default: a command that dies mid-pipeline
still returns success, an unset variable expands to nothing, a failed
`cd` leaves the next `rm` pointed at the wrong directory. The
agent-typical minimal edit makes the noise stop rather than the failure:
append `2>/dev/null`, add `|| true`, silence shellcheck. The script gets
quieter while getting more dangerous. This review hunts that debt class
specifically.

Hooks and install scripts deserve the strictest reading — they run
unattended, so a swallowed error surfaces days later as unexplained
missing behavior.

## Context

Changed shell files:
!`git diff --name-only HEAD 2>/dev/null | grep -E '\.(sh|bash|zsh)$' || echo "(not a git repo or no changed shell files — review the given path instead)"`

## Process

### Step 1: Scope

Review `$ARGUMENTS` if given; otherwise the changed shell files above;
otherwise ask which script. Include extensionless files with a shell
shebang — hooks and CLI entry points often have no extension. Read each
scoped script fully before judging; control flow in shell is textual and
a finding usually depends on what runs three lines later.

### Step 2: Mechanical Pass

```bash
shellcheck --severity=style --enable=all --format=gcc <files>
```

`--enable=all` turns on the optional checks (`require-variable-braces`,
`add-default-case`, `quote-safe-variables`) that catch this debt class.
If the project pins a `.shellcheckrc`, run that instead and say so.

Confirm each script declares its strictness. The absence of
`set -euo pipefail` (or a documented reason for its absence) is the
first thing to report — every other finding is amplified by it.

Then grep the scoped files for triggers shellcheck cannot judge:

| Trigger                                              | Suspicion                                                                         |
| ---------------------------------------------------- | --------------------------------------------------------------------------------- |
| `2>/dev/null`                                        | Which error is expected here? Discarding all stderr hides the unexpected ones too |
| `\|\| true` / `\|\| :`                               | Failure declared acceptable — is it, and is that written down?                    |
| missing `set -euo pipefail`                          | Script continues past errors by default                                           |
| unquoted `$var` in test, path, or argument position  | Word splitting and glob expansion on any value with spaces                        |
| `cd $dir` without `\|\| exit`                        | Later commands run in the wrong directory                                         |
| `rm -rf "$var"`                                      | What if the variable is empty or unset?                                           |
| hardcoded `/tmp/name`                                | Collision and symlink races — wants `mktemp`                                      |
| `# shellcheck disable=`                              | Who silenced the check, and is the reason written down?                           |
| `tac`, `sed -i`, `date -d`, `readlink -f`, `grep -P` | GNU-only; breaks on macOS BSD tools                                               |
| `yq`, `jq`, `realpath`                               | Which implementation? Python yq and Go yq take different syntax                   |
| `local` inside a non-function                        | zsh and bash disagree                                                             |
| `[ ]` vs `[[ ]]` mixed                               | Usually accidental, changes quoting semantics                                     |

The platform row matters here specifically: this workstation is macOS,
so a script that only ran under GNU coreutils in CI is untested where it
actually runs.

### Step 3: Judgment Pass

For each trigger hit, decide which of three buckets it belongs in — this
is the review's actual work:

1. **Fine** — the suppression is narrow and documented.
   `command -v foo >/dev/null 2>&1` as a presence check is not a finding;
   `rm -f` on a known-optional file is not a finding.
2. **Mechanical fix** — safe local rewrite: quote the expansion, add
   `|| exit 1` after `cd`, swap the hardcoded temp path for `mktemp`,
   narrow `2>/dev/null` to the one command that legitimately warns,
   replace the GNU-only invocation with a portable form.
3. **Failure-handling restructure** — the silencing exists because the
   script has no error strategy: no `trap` for cleanup, no distinction
   between expected and unexpected failure, no way for a caller to learn
   something went wrong. Name the restructure (strict mode plus targeted
   allowances, a `trap ... ERR` handler, a loud-mode flag for
   development, exit codes that mean something) and its blast radius. Do
   not apply it without asking — this bucket is why the review exists.

A repeated trigger is one finding, not many: six `2>/dev/null || true`
across one hook point at a single missing error strategy.

### Step 4: Report

Findings ordered by severity, each with `file:line`, the bucket, why it
matters in one sentence, and the suggested fix. Then a one-paragraph
verdict: when this script fails, does anyone find out? End with the
counts: N fine / N mechanical / N restructure.

If the user asks you to apply fixes, apply bucket 2 directly and re-run
shellcheck plus the script's own smoke path after; bucket 3 gets a plan
first.

## Rules

- Never suggest `2>/dev/null`, `|| true`, or a shellcheck disable as a
  fix.
- A clean run is the floor, not the verdict — a silent script and a
  working script look identical from outside.
- Judge suppression by which specific error it was meant to catch. If
  that error cannot be named, the suppression is a finding.
- Test platform assumptions on macOS before calling a script portable.
