---
name: test-review
description: >
  Audit tests for agent-typical anti-patterns: assertions that cannot
  fail, mocking the unit under test, sleep-based timing, snapshots
  regenerated to match whatever the code did, tests asserting on
  implementation detail, skipped or swallowed failures. Language-agnostic
  — judges whether a suite can actually detect a regression. Use when:
  reviewing agent-written tests, before trusting a green suite, or on
  "test review", "review these tests", "are these tests real", "would
  this catch a bug". For designing a test strategy use /testing;
  for generic bug hunts use /code-review.
argument-hint: "[test path or suite to review, defaults to working-tree changes]"
---

# Test Review — Falsifiability Audit

A test earns its keep by failing when the code breaks. The
agent-typical failure mode is a test written to pass: it runs the code,
observes whatever came out, and asserts that. Green suite, zero
detection power. The tell is that you cannot describe a change to the
production code that would turn the test red.

That question — _what break would this catch?_ — is the whole review.
Everything below is a way of finding tests that have no answer to it.

## Context

Changed test files:
!`git diff --name-only HEAD 2>/dev/null | grep -iE '(test|spec)' || echo "(not a git repo or no changed test files — review the given path instead)"`

## Process

### Step 1: Scope

Review `$ARGUMENTS` if given; otherwise the changed test files above;
otherwise ask which suite. Read both the tests and the code under test —
a test can only be judged against what it claims to protect. Note the
language and framework; the triggers below are universal but their
spelling is not.

### Step 2: Mechanical Pass

Run the suite and record what it reports:

```
<the project's own test command: pytest, go test -race ./..., npm test,
cargo test — check the Makefile first, since targets there mirror CI>
```

Capture three numbers before reading any code: tests passed, tests
skipped, and wall-clock time. Skipped tests are invisible in a green
summary. A suite that runs suspiciously fast may not be exercising what
it claims; one that runs slowly often contains sleeps.

If coverage tooling is already configured, run it — but treat coverage
as a map of what was _executed_, never as evidence of what was
_checked_. A tautological test covers lines perfectly.

Then grep the scoped tests for triggers no tool can judge:

| Trigger                                                                  | Suspicion                                                              |
| ------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| `assert True`, `expect(true).toBe(true)`, `assert.NoError` alone         | Assertion that cannot fail                                             |
| assertion comparing a value to itself, or to a call of the same function | Tautology — the test restates the code                                 |
| mock or patch naming the unit under test                                 | The test exercises the mock, not the code                              |
| `sleep`, `setTimeout`, `time.Sleep` in a test                            | Timing guess standing in for synchronization — flake in waiting        |
| snapshot or golden file with no assertion on its content                 | Records behavior; regenerating on failure erases the signal            |
| `skip`, `xit`, `t.Skip`, `@pytest.mark.skip`                             | Disabled test — permanent or forgotten?                                |
| `try`/`except` or `catch` inside a test body                             | Failure swallowed before the framework sees it                         |
| assertions on private methods, call counts, or internal state            | Implementation-coupled — breaks on refactor, silent on behavior change |
| no assertion at all (smoke-only)                                         | Verifies "does not crash" — say so, do not call it coverage            |
| identical setup copied across many tests                                 | Shared fixture drifting out of sync with reality                       |
| hardcoded dates, ports, paths, or ordering assumptions                   | Passes today, on this machine, in this order                           |

### Step 3: Judgment Pass

For each test, answer the falsifiability question, then bucket it —
this is the review's actual work:

1. **Real** — you can name a production-code change that turns this
   test red, and that change is a bug worth catching. A smoke test
   honestly labeled as such is real; so is a mock of a genuine external
   boundary like a network call or clock.
2. **Mechanical fix** — the intent is sound but the execution leaks:
   replace the sleep with a wait-for-condition, unwrap the swallowed
   exception, assert on returned behavior instead of call counts, delete
   the tautology, give the skip an expiry or a reason.
3. **Coverage restructure** — the test exists to make a number go up,
   not to detect a defect: whole modules mocked into meaninglessness,
   snapshots standing in for expectations, a suite that would stay green
   through a rewrite of the logic it names. Name what is actually
   unprotected and what would protect it. Do not apply it without
   asking — this bucket is why the review exists.

A repeated trigger is one finding, not many: twelve tests mocking the
same collaborator point at one seam that resists testing.

Also report the inverse, which greps cannot find: behavior the code has
and the suite does not touch. Error paths and boundary conditions are
where agent-written suites are thinnest, because the happy path is what
the agent just watched work.

### Step 4: Report

Findings ordered by severity, each with `file:line`, the bucket, the
break it fails to catch, and the suggested fix. Then a one-paragraph
verdict answering the only question that matters: if someone broke this
code tomorrow, would this suite notice? End with the counts: N real /
N mechanical / N restructure, plus the skipped-test count.

If the user asks you to apply fixes, apply bucket 2 directly. Verify
each repair the honest way — break the production code on purpose,
confirm the test goes red, then restore it. A test you have not seen
fail is not a test you have verified. Bucket 3 gets a plan first.

## Rules

- Never suggest deleting a failing test, loosening an assertion, or
  regenerating a snapshot as a fix for a red suite.
- Green is the floor, not the verdict — a suite that cannot fail is
  indistinguishable from one that passes.
- Judge every test by the break it would catch. A test with no answer
  is a finding regardless of how much it covers.
- Coverage percentage is context, never a conclusion.
