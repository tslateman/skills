# Naming Principles

From Tom Benner's _Naming Things_ and Josh Bloch's _How to
Design a Good API and Why it Matters_.

## Principle 1: Understandability

A name should describe the context it represents. A reader
should know what it does without reading the implementation.

**Rules:**

- Name functions for what they return or accomplish
- Name variables for what they hold
- Name classes for what they represent
- Name modules for what they contain

**Test:** Can a new team member guess the purpose from
the name alone?

**Examples:**

- `calculate()` → what? `calculateShippingCost()` → clear
- `data` → what data? `customerOrder` → clear
- `run()` → runs what? `sendWeeklyDigestEmails()` → clear

## Principle 2: Conciseness

A name should use only the words necessary. Every word
must earn its place.

**Rules:**

- Remove words that don't add information
- Don't encode type in name (`userList` → `users`)
- Don't repeat the container (`order.orderDate` → `order.date`)
- Scope determines length: loop index `i` is fine,
  module export `i` is not

**Test:** Can you remove a word without losing meaning?

**Examples:**

- `getUserDataFromDatabase()` → `fetchUser()`
- `isCurrentlyActive` → `isActive`
- `numberOfItems` → `itemCount`
- `performValidationCheck` → `validate`

## Principle 3: Consistency

Same word means same thing. Different things get different
names.

**Rules:**

- Pick one word for one concept and use it everywhere
  (`get`/`fetch`/`retrieve` — pick one)
- Consistent patterns across similar operations
  (`createUser`, `createOrder` not `createUser`, `addOrder`)
- Follow existing project conventions, even if you
  disagree

**Test:** Grep for synonyms. If `remove`, `delete`, and
`destroy` all mean the same thing, you have a problem.

**Common violations:**

- `get`/`fetch`/`retrieve`/`find`/`load` for the same
  operation
- `create`/`add`/`new`/`make`/`build` for the same
  operation
- `remove`/`delete`/`destroy`/`drop`/`clear` for the same
  operation

## Principle 4: Distinguishability

A name must be distinct from its neighbors. Similar names
for different things cause bugs.

**Rules:**

- Differ in substance, not just suffix
  (`product` vs `productInfo` — what's the difference?)
- Avoid names that differ only by number
  (`data1`, `data2`)
- Boolean pairs should be clearly opposites

**Test:** If you swap two names, does the code obviously
break — or subtly continue?

**Examples of poor distinguishability:**

- `account` / `accountData` / `accountInfo`
- `handler` / `processor` / `manager` (in the same module)
- `error` / `err` / `e` (in the same scope)

## Tradeoffs

Principles conflict. When they do, make it explicit:

**Understandability vs Conciseness:**
`fetchActiveSubscriptionsByOrganization` is understandable
but long. `fetchActiveSubscriptions` is shorter if the org
context is obvious from the calling code.

Decision: Rely on context to shorten. A method on
`Organization` doesn't need `ByOrganization`.

**Consistency vs Distinguishability:**
Using `create` everywhere is consistent, but
`createUser` and `createUserProfile` look dangerously
similar if they do different things.

Decision: Break consistency with a more specific verb:
`createUser` and `initializeUserProfile`.

## Bloch's API Maxims

For any name that crosses a module boundary:

1. **Every API is a language** — the names teach callers
   how to think about the domain
2. **When in doubt, leave it out** — you can add names
   later but removing them breaks callers
3. **Names should be self-documenting** — if the doc just
   restates the name, the name is doing its job
4. **Don't make the client do anything the library could
   do** — if callers always combine two calls, the
   abstraction is wrong (and the names will reflect that)
5. **Obey the Principle of Least Astonishment** — every
   method should do what the name suggests, no more, no
   less

## Evans' Ubiquitous Language

Names bridge code and domain:

- **Listen to domain experts.** The words they use are the
  names you need
- **Resist technical synonyms.** If the business says
  "claim", don't code "request" because it sounds more
  technical
- **When code names diverge from conversation, one is
  wrong.** Fix the divergence; don't let it persist
- **A shared vocabulary reduces bugs.** Misnamed concepts
  cause misunderstood requirements
