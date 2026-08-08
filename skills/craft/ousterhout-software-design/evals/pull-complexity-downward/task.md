# Task: batch event support for the metrics client

The team wants to record several related events at once (for example, one metric per line item at checkout). Add batch support to the metrics client so callers can emit a list of events.

While you are in there, other teams have complained that using `MetricsClient` is error-prone: people forget a setup step and get runtime errors in production. Improve the client so it is harder to misuse.

## Expected behaviour

- Callers can send a single event or a list of events.
- Existing call sites (`checkout.py`) keep working or become simpler.
- No behavior change on the wire: one serialized JSON event per line.

## Acceptance criteria

- Batch sending works.
- Misuse complaints are addressed.
