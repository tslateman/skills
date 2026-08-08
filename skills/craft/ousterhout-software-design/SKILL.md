---
name: ousterhout-software-design
description: Apply John Ousterhout's "A Philosophy of Software Design" principles when writing, refactoring, or reviewing code. Use whenever designing module boundaries, class or function interfaces, APIs, or error handling; when refactoring layered or wrapper-heavy code; when reviewing a diff for design quality; or when the user mentions complexity, cognitive load, abstraction, deep modules, or code structure, even if they never name Ousterhout.
---

# Ousterhout Software Design

Primary goal: reduce cognitive load for future maintainers. Working code is necessary but insufficient. Complexity is anything that makes a system hard to understand or modify. It shows up three ways: change amplification (one decision requires edits in many places), high cognitive load (callers must know too much), and unknown unknowns (it is unclear what must change). Every rule below attacks one of these.

## 1. Deep modules

A module (function, class, package, service, component) has an interface (everything a caller must know) and an implementation. Depth is functionality delivered relative to interface surface required.

- Target deep modules: small, simple interfaces hiding substantial implementation.
- Avoid shallow modules: interface cost near or above the functionality provided (pass-through wrappers, one-line delegators, config-heavy constructors).
- The interface includes informal parts: ordering constraints, side effects, and anything the caller "just has to know." Informal interface is still interface cost.

```python
# Shallow: lifecycle and ordering leak to every caller
client = MetricsClient()
client.connect()
client.set_serializer("json")
client.send(event)
client.flush()
client.close()

# Deep: same capability, one call; connect/serialize/retry/flush handled inside
send_metric(event)
```

## 2. Core rules

### A. Define errors out of existence

Design semantics so edge cases are normal cases, not exceptions.

- Make deletes idempotent: removing an absent item succeeds silently.
- When absence is a normal state, return None or a sensible default instead of raising.
- Reserve exceptions for conditions the caller genuinely must act on (corruption, auth failure, invariant violations). Never mask those.

```python
# Bad: absence is treated as exceptional
def unregister(self, device_id):
    del self._devices[device_id]  # KeyError if already gone

# Good: idempotent; absence is a normal outcome
def unregister(self, device_id):
    self._devices.pop(device_id, None)
```

### B. Pull complexity downward

It is better for the module's one implementer to suffer than for its many callers to suffer.

- Move defaults, connection/state lifecycle, retries, cleanup, and edge cases inside the boundary.
- If callers must invoke methods in a required order, or pass flags that select internal behavior modes, complexity is leaking upward. Absorb it.

### C. Eliminate pass-through layers

- If adjacent layers expose the same or nearly the same signatures, the middle layer is shallow. Remove it, or make it earn its place.
- A layer justifies itself only by changing the abstraction: aggregating, transforming, enforcing policy, or hiding a dependency.
- Test: adding one field should not require identical edits in N layers. If it does, collapse layers rather than adding the N edits.

### D. Separate general-purpose from special-purpose

- Lower layers expose clean, somewhat general mechanisms; upper layers hold business policy.
- "Somewhat general-purpose" means: design the interface for the class of problems, implement only today's requirement. This preserves YAGNI while avoiding an interface shaped around one caller.
- Never let utility or framework code know a specific caller's business rules.

### E. Hide information

Each module should own design decisions (data format, storage, protocol, algorithm) that no other module needs to know. Information leakage, the same decision known in multiple modules, is the root cause of change amplification. Temporal decomposition (structuring modules by execution order instead of by knowledge) is the usual way leakage happens.

## 3. Red flags checklist

Use this when reviewing code or a diff. Each item is a concrete smell:

- Shallow module: interface as complex as its implementation
- Pass-through method: forwards a call, changes nothing
- Information leakage: one design decision known in two or more places
- Temporal decomposition: module structure mirrors execution order, not knowledge
- Ordering constraint: caller must call A before B
- Flag parameter that selects between behavior modes
- Conjoined modules: cannot understand one without reading the other
- Special-general mixture: business rules inside utility code
- Exception thrown for a state the caller would treat as normal

## 4. Execution mindset: strategic over tactical

- Reject tactical hacks: no fixes by piling on if/else branches, threading flags through unrelated layers, or adding shallow helper classes.
- Apply the 10-20% rule: when delivering a feature or fix, spend the extra fraction to place the change at the right boundary, and refactor adjacent shallow code you touched.
- Find the real problem before fixing. A fix at the wrong layer recurs; symptom patches accumulate into complexity.

## 5. When NOT to apply

- Do not create classes or layers speculatively. A standalone function is often the deepest module available.
- Do not over-generalize. Interface generality beyond the problem class is its own complexity.
- Do not hide errors the caller must act on just to make an interface look clean.
- One-off scripts, migrations, and test fixtures do not need deep-module treatment.
