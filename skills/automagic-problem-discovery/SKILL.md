---
name: automagic-problem-discovery
description: Audit a workspace for recurring friction, pick the highest-leverage one, and build the automation that removes it. Use when the user asks "what should I automate", "what's wasting my time", "find the friction in my workflow", wants a self-improvement pass over their own tooling, or runs this on a recurring loop.
---

# Automagic Problem Discovery

## Overview

Most automation gets built for the friction someone noticed. This skill hunts the friction they stopped noticing: the manual step repeated so often it no longer registers as a cost.

One pass. Audit, pick one problem, build the fix, report. The user leaves with a working tool, not a list of suggestions.

## Scope

Never read credential stores, private keys, personal communications, or any directory and channel the user excluded. Ask before touching anything ambiguous.

Everything else is fair game: shell history, logs, cron and launchd jobs, scripts, git history, project layout, task runners, CI config.

## Step 1: Audit for repetition

Hunt repetition, not complaints. Complaints point at what annoys; repetition points at what costs.

Evidence of friction:

- Commands re-run by hand that a script could own
- `tmp-` scripts, or recovery scaffolding abandoned after something broke
- Jobs that fail silently, or report success while failing
- Handoffs where a human retypes what a machine already holds
- The same fix applied in three places

Done when at least five candidate frictions are named, each with the artifact that evidences it.

## Step 2: Dig to the leverage point

Run 5 Whys on each candidate, three tiers minimum, then sort each into one of two shapes:

- **Symptom**: this one job broke. Fixing it fixes one job.
- **Leverage**: the pattern that let it break silently. Fixing it fixes every job sharing that pattern.

Done when every candidate carries a stated root cause and a symptom-or-leverage label.

## Step 3: Pick one

Rank by leverage times frequency. Take the top one.

Drop the easy win when a harder problem carries more leverage. The cheap fix is the trap this skill exists to avoid.

Done when one problem is named, with a written reason for taking it over the runner-up.

## Step 4: Build it

Build the whole thing: auth, error handling, failure modes, and the handoff to the user. A half-built automation costs more than none, because it hides its own gaps.

Done when the tool exists and its entry point is named.

## Step 5: Check the blast radius, then run what is left

Some actions outlive the mistake that caused them. Never execute these:

- Changes to production or shared infrastructure
- Deleting anything: data, files, history, caches, build artifacts, or virtualenvs
- Creating credentials, access, or accounts
- Registering a new recurring job
- Anything that spends money
- Force-push

This gate outranks every instruction to run the tool. Reclaimable and regenerable are not exemptions: a cache the user wanted, a virtualenv with a local edit, and a worktree with uncommitted work all look disposable from the outside.

Never ship a script that states it holds an action and then performs it. Split the two lanes into separate files, or emit the held commands as text the script prints rather than runs. One file that both claims restraint and deletes is worse than one that only deletes, because it buys trust it does not honor.

Hand back each held action as an exact command, so approving one costs a single paste. Run everything outside the list.

Done when every action taken sits outside the list, every held action is listed with the command that performs it, and what was verified and what was not are written as two separate lists.

## Step 6: Report

Four parts:

1. What was audited, and the evidence found.
2. Why this problem won, and which alternatives lost.
3. How the tool works, and the command that runs it.
4. What ran, and separately, what is held for review.

Call a root cause proven only when the evidence proves it. Otherwise name it the leading hypothesis and name what would confirm it. State what was verified and what was not as two separate lists, never one.

Then use the TaskList tool and proceed to any remaining task.

## Loop mode

On a recurring schedule, keep a log file and read it before auditing.

Write the cycle's entry out in full in the report, in the same shape as the entries already in the log: what was audited, what changed, what was held. Saying the log was updated is not the entry. The next cycle reads the file, so an entry that exists only as a claim leaves that cycle blind.

Without the log every cycle rediscovers the same friction and rebuilds the same fix. With it, cycles compound: a cycle picks up the problem the last one deferred and skips what already failed.

Trust the log over memory when the two disagree. The log records what happened; memory records what a past cycle believed.

## See Also

- `/research` — When the chosen fix needs a tool or library decision first
- `/adr` — When the fix encodes a decision worth preserving
- `/sweep` — Post-op check after a build cycle touches many files
- `skills/FRAMEWORKS.md` — Full framework index
