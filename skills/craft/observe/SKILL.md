---
name: observe
description: Decide what telemetry a feature needs before writing any of it, by naming the questions an on-call engineer will ask. Covers signal selection (metric, trace, log), structured events, RED and USE metrics, cardinality limits, and symptom-based alerting. Use when shipping anything that runs in production, when an incident took too long to diagnose, when reviewing a PR that adds retries, queues, or external calls, or on "add logging", "what should we alert on". Do not use to diagnose a failure happening now, or to optimize measured slowness.
argument-hint: "[the feature or service to instrument]"
---

# Observe — Evidence After It Ships

A test proves the code worked under inputs you thought of. In production it
meets the ones you did not, and the only thing that answers "what is it doing
and why" is the telemetry it emits.

Instrumentation is written alongside the feature, the way tests are. Deferred,
it becomes "after the first incident" — the most expensive moment to discover
you are blind.

## Use this vs. its neighbors

- Diagnosing a failure happening now → debug it; `observe` makes that fast the
  _next_ time.
- Proving a feature works before it ships → `testing`, the verification pair.
- Proving a change is safe outside the diff → `blast-radius`.
- Knowing what the system did once real users touched it → here.

## 1. Name the questions first

Telemetry without a question is noise. Before adding a single line, write down
the two to four questions an on-call engineer will ask about this feature:

```text
FEATURE: checkout payment retry
ON-CALL WILL ASK:
  1. What fraction of payments succeed first try vs after retry?
  2. When one fails permanently, why? Provider error, timeout, validation?
  3. Is the provider slower than usual?
→ Every signal below must answer one of these.
```

If you cannot name the questions, you are not ready to instrument. You will log
everything and learn nothing.

## 2. Pick the signal that answers each one

| Signal             | Answers                                | Cost                          |
| ------------------ | -------------------------------------- | ----------------------------- |
| **Metric**         | How often, how slow, in aggregate      | Fixed per series, cheap       |
| **Trace**          | Where the time went across services    | Per request, usually sampled  |
| **Structured log** | Why this specific case did what it did | Per event, grows with traffic |

Metrics tell you **that** something is wrong, traces tell you **where**, logs
tell you **why**. Reaching for the wrong one is how a team ends up
with logs by the terabyte and no idea which endpoint regressed.

## 3. Log events, not prose

Every line is a machine-readable object with a stable event name and fields.
String interpolation produces output nobody can filter, correlate, or alert on.

**A correlation ID is mandatory.** Generate or accept a request ID at the system
boundary, attach it to every log line, span, and outbound call. Without it you
cannot reconstruct one request from interleaved output, the only thing you will
want at 3am.

**Never log secrets, tokens, or unredacted personal data.** Telemetry pipelines
are a classic leak path. Allowlist the fields you emit; never log whole request
bodies.

## 4. Metrics: bounded labels, percentiles

Instrument **RED** on every request path — Rate, Errors, Duration. Instrument
**USE** on every resource such as a queue or pool — Utilization, Saturation,
Errors.

**Cardinality is the failure mode.** Every distinct label combination is its own
time series, so labels come from small fixed sets: a route template, a status
class, a provider name. User IDs, raw URLs, request IDs, and error message text
belong in logs and traces. As labels they take the metrics backend down.

Track percentiles, never averages. An average hides the one percent of users
having a terrible time, and they are the ones who file the ticket.

## 5. Alert on symptoms, not causes

| Page-worthy symptom    | Dashboard-worthy cause |
| ---------------------- | ---------------------- |
| Error rate above 1%    | CPU at 85%             |
| p99 latency above 2s   | A pod restarted        |
| Queue age above 10 min | Disk at 70%            |

Cause alerts fire when nothing is wrong and stay silent for failures nobody
predicted. Symptom alerts fire exactly when users are hurt, whatever the cause.

Every alert must be actionable, must link to a runbook even a three-line one,
and must have a threshold justified by an SLO or by history rather than a guess.
Use two severities: page and ticket. A third becomes noise, and noise trains
people to ignore the pager.

## 6. Verify the telemetry

Instrumentation is code, so it can be wrong. Before calling the work done,
trigger the paths and read the real output rather than assuming.

The completion criterion is one exercise: **induce a failure in staging and
locate it through telemetry alone, without opening the source.** If you cannot,
the instrumentation does not answer the questions from step 1 yet.

Confirm alongside it:

- [ ] Each signal maps to a written on-call question
- [ ] Output is structured, with a correlation ID on every line
- [ ] No secrets or unredacted personal data, checked against real output
- [ ] RED metrics on new endpoints and dependencies, label sets bounded
- [ ] Latency queryable as p95 and p99
- [ ] One request followed end to end with no broken spans
- [ ] Every new alert symptom-based, runbook-linked, and test-fired once

## Rules

1. **No question, no signal.** Instrumentation without one builds dashboards
   that show everything except the answer.
2. **Unstructured output is not observability.** Three queryable events beat
   three hundred lines of prose.
3. **A feature PR that adds retries, queues, or external calls and no telemetry
   is incomplete**, however green the suite is.

---

Adapted from `observability-and-instrumentation` in
[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) (MIT).
Compressed to the judgment and made language-agnostic; the TypeScript and
OpenTelemetry specifics are upstream.
