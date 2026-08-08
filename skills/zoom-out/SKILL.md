---
name: zoom-out
description: Step up a layer of abstraction to map how unfamiliar code fits into the larger system. Use when the user says "zoom out", "bigger picture", "I don't know this area", "give me a map", "where does this fit", is reading code and feels lost, or is about to change unfamiliar code.
---

# Zoom Out

## Overview

When you don't know a section of code well, the failure mode is to read line-by-line and never see the shape. Zoom out forces a higher layer of abstraction first: callers, neighbors, role in the system. Read the map before walking the streets.

## The Map First

Before explaining what a piece of code does, produce a map of its surroundings:

1. **Identify the unit**: file, module, package, or service. Name it precisely.
2. **Find callers**: who uses this? Grep for imports, invocations, or routes.
3. **Find neighbors**: what siblings live in the same directory or namespace, and what do they do?
4. **Find the abstraction above**: what does this module belong to? A pipeline, a layer, a bounded context.
5. **Find the abstraction below**: what does it depend on?

Render the result as a short list or small diagram. Use the **project's own vocabulary**: the words the codebase uses, not generic CS terms.

## Output Shape

Aim for something like:

```
Module:    src/billing/invoicing/
Role:      Generates invoices from billing periods (one of three writers under /billing)
Above:     /billing — orchestrates subscriptions, invoicing, dunning
Below:     /billing/pricing (rates), /billing/tax (tax calc)
Callers:   src/jobs/monthly_invoice_job.py, src/api/admin/invoices.py
Siblings:  subscriptions/, dunning/
```

Then, and only then, go deeper.

## Anti-Patterns

- **Reading line-by-line first.** A bottom-up model rarely survives contact with the actual architecture.
- **Generic vocabulary.** "Service layer, repository pattern" tells the reader nothing about _this_ codebase. Use its own terms.
- **Skipping callers.** Behavior at the callsite often constrains the module more than the module's own code does.
- **Zooming in too soon.** If the map isn't done, every implementation detail you read is uncalibrated.

## Pairs With

- `/naming`: domain vocabulary lives in names; zoom-out is naming applied to architecture
- `/design`: zoom-out surfaces the structure, design evaluates it
- `/ia`: IA is zoom-out for documentation; same instinct, different medium
- `/research`: zoom-out maps the inside, research maps the outside

---

_Adapted from [mattpocock/skills](https://github.com/mattpocock/skills)._
