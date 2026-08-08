---
name: naming
description: Evaluate and improve names in code using naming as a design diagnostic. Use when the user asks to "name this", "rename", "review naming", "what should I call", struggles to name something, or when a code review surfaces vague or misleading names.
---

# Naming as Design

## Overview

Naming difficulty is a design smell. When you struggle to name something, the abstraction is wrong. Use naming as a lens to surface confused boundaries, mixed responsibilities, and domain misunderstanding.

## Benner's Four Principles

Every name balances four properties. When they conflict, make the tradeoff deliberate.

1. **Understandability**, Describe the context it represents. A reader should know what it does without reading the implementation
2. **Conciseness**, Use only the words necessary. Longer is not clearer if the extra words add no meaning
3. **Consistency**, Same word means the same thing everywhere. Different things get different names
4. **Distinguishability**, A name must be distinct from its neighbors. Similar names for different things cause bugs

See `references/principles.md` for detailed rules and naming smells.

## Two Modes

### Review Mode

Examine names in recently changed code:

1. Read the changed code
2. For each name, ask:
   - Does it pass all four principles?
   - Could a reader understand this without context?
   - Is the verb specific? ("process", "handle", "manage" almost never are)
   - Does it match the domain language?
3. Surface violations with specific alternatives

### Design Mode

When naming is hard, use the struggle as a diagnostic:

1. What does this thing _actually do_? List its responsibilities
2. If the list has more than one item, the naming problem is a design problem, split it
3. Who calls it? What do they expect?
4. If it disappeared, what would break? That's what it is
5. What would the domain expert call it?

## Naming Smells

Names that signal design confusion:

| Smell                                  | Example                        | What it reveals                       |
| -------------------------------------- | ------------------------------ | ------------------------------------- |
| Generic verb                           | `handleData`, `processRequest` | Unclear responsibility                |
| Suffix `-Manager`, `-Helper`, `-Utils` | `UserManager`, `StringHelper`  | God object or junk drawer             |
| And/Or in name                         | `validateAndSave`              | Two responsibilities                  |
| Type in name                           | `userList`, `nameString`       | Redundant or wrong abstraction level  |
| Negated boolean                        | `isNotReady`, `disableFeature` | Double negatives in conditions        |
| Abbreviated beyond recognition         | `usrSvcRsp`                    | Conciseness without understandability |

## Bloch's API Design Maxims

For public interfaces, APIs, library boundaries, module exports:

- **Names should be self-documenting.** If you need a comment to explain what a function does, rename it
- **Same word, same meaning.** Don't use "remove" in one place and "delete" in another for the same operation
- **Principle of Least Astonishment.** A method named `check` should not modify state
- **If it's hard to name, the design is wrong.** Rename the design, not just the symbol

## Evans' Ubiquitous Language

Code names should match how domain experts talk:

- If the business says "order" and code says "purchase", one of them is wrong
- Naming mismatches between code and conversation reveal domain misunderstanding
- When renaming, update tests, docs, and conversations, not just code

## Naming Checklist

For any name under review:

```
[ ] Specific verb (not handle/process/manage/do)
[ ] No unnecessary words
[ ] Consistent with similar names nearby
[ ] Distinguishable from neighbors
[ ] Matches domain language
[ ] Readable without implementation context
[ ] No embedded type information
[ ] Boolean reads as a question (isReady, hasPermission, canEdit)
```

## Output Format

When reviewing names:

```markdown
## Naming Review

### Must Rename

- `processData` → `validateInvoiceLineItems` — "process" hides
  the actual responsibility; this only validates
- `handleClick` → `submitPayment` — name the action, not
  the event

### Consider Renaming

- `userInfo` → `billingProfile` — more specific to its
  actual contents

### Design Concern

- `OrderManager` has 12 methods spanning validation,
  persistence, and notification. The naming struggle
  reflects three responsibilities that should be separate
  types.
```

## Before/After Examples

Strunk's Rule 12 applied to code: use definite, specific, concrete names. (`/prose` carries the same rule for English prose.)

### Functions

| Before               | After                               | Why                                                               |
| -------------------- | ----------------------------------- | ----------------------------------------------------------------- |
| `processData(input)` | `validateInvoiceLineItems(invoice)` | "Process" hides responsibility; name the action and the domain    |
| `handleClick()`      | `submitPayment()`                   | Name the business action, not the DOM event                       |
| `doStuff(items)`     | `deduplicateContacts(contacts)`     | Eliminate weasel verbs; name what it actually does                |
| `run()`              | `pollForStatusUpdates()`            | Ambiguous in any class with more than one operation               |
| `getData()`          | `fetchUserProfile()`                | "Get" hides the source and subject; name the fetch and the domain |

### Variables

| Before   | After                 | Why                                                 |
| -------- | --------------------- | --------------------------------------------------- |
| `data`   | `unpaidInvoices`      | Generic noun → specific domain concept              |
| `temp`   | `unsavedDraft`        | Reveals intent; "temp" says nothing about lifecycle |
| `flag`   | `requiresApproval`    | Reads as a question; boolean purpose is clear       |
| `result` | `validationErrors`    | Names the content, not the role in the function     |
| `list`   | `activeSubscriptions` | Type-in-name smell; name the contents instead       |

### Types and Modules

| Before          | After                             | Why                                                      |
| --------------- | --------------------------------- | -------------------------------------------------------- |
| `UserManager`   | `UserRepository` + `UserNotifier` | `-Manager` reveals multiple responsibilities; split them |
| `StringHelper`  | `SlugFormatter`                   | `-Helper` is a junk drawer; name the actual capability   |
| `DataService`   | `InventoryClient`                 | Two generic words; name the domain and the role          |
| `utils/misc.ts` | `pricing/discount-rules.ts`       | File path is a name too; make it navigable               |

### Booleans

| Before           | After                           | Why                                              |
| ---------------- | ------------------------------- | ------------------------------------------------ |
| `isNotReady`     | `isReady` (invert usage)        | Avoid double negatives in conditionals           |
| `disableFeature` | `featureEnabled` (invert usage) | Positive form reads naturally in `if` statements |
| `check`          | `hasPermission`                 | "Check" doesn't say what the answer means        |

## See Also

- `/design`: Hard-to-name things signal design problems
- `/code-review`: Code review surfaces naming issues; naming review deepens code review
- `/prose`: Strunk's rules apply to code names identically to English prose
- `skills/FRAMEWORKS.md`: Full framework index
