# Mechanics Catalog

Fowler's ordered procedures for the moves `SKILL.md` routes to. The mechanics exist so every intermediate state compiles and passes. Run the tests where each procedure says to; the step is the unit of verification, not the refactoring.

Convention below: **Test.** marks a mandatory suite run.

---

## Composing functions

### Extract Function

Use when a fragment expresses a concern the reader must currently interleave with the surrounding one. Never to reduce line count.

1. Create a new function; name it for **what it does**, not how.
2. Copy the fragment into it.
3. Resolve references: locals used but not assigned become parameters; a single local assigned and used after becomes the return value.
4. Compile.
5. Replace the original fragment with a call. **Test.**
6. Scan for other fragments doing the same thing; replace each and **test** after each.

If step 3 produces more than three parameters or two return values, the boundary is wrong. Stop and reconsider the seam.

### Inline Function

Use when the body is as clear as the name, or the function is a pass-through.

1. Confirm it is not polymorphic (never inline a method with subclass overrides).
2. Find every caller. **Test** that the list is complete — grep the bare name for dynamic dispatch.
3. Replace one call with the body. **Test.**
4. Repeat one call at a time.
5. Delete the function.

### Extract Variable

1. Confirm the expression has no side effects.
2. Declare an immutable variable, assign the expression.
3. Replace the expression with the variable. **Test.**

### Change Function Declaration

For renames and signature changes. The safe path is the migration path.

1. Extract the body into a new function with the new signature.
2. Make the old function delegate to it. **Test.**
3. Update callers one at a time, **testing** after each.
4. Inline the old function away.

For a simple rename with full static visibility, the direct route (rename, update all callers, test) is fine — but only when tooling did the rename, not text substitution.

---

## Moving features

### Move Function

1. Inspect every element the function uses in its current context; decide which move with it.
2. Confirm it is not polymorphic.
3. Copy it to the target, fitting it to its new home. **Compile.**
4. Reference the target from the source: turn the original into a delegating call. **Test.**
5. Decide whether to inline the delegator away or keep it as the public entry point.

### Split Phase

Use when one block does two sequential things (parse then compute, compute then format).

1. Extract the second phase into its own function. **Test.**
2. Introduce an intermediate data structure as a parameter to it. **Test.**
3. Move each piece of first-phase output into the intermediate structure, **testing** after each.
4. Extract the first phase, returning the intermediate structure. **Test.**

The payoff is that each phase becomes independently testable. If the intermediate structure ends up with one field, the split was not real — revert.

---

## Simplifying conditionals

### Decompose Conditional

Extract the condition, the then-leg, and the else-leg into named functions. **Test** after each extraction. The names carry the intent the comment would have.

### Replace Nested Conditional with Guard Clauses

1. Take the outermost condition that is a precondition, not a branch of the main logic.
2. Invert it into an early return. **Test.**
3. Repeat until only the main path remains at top level. **Test** after each.

Guard clauses are for **preconditions** — cases where the function has nothing to do. Two equally weighted branches stay an if/else; flattening those loses meaning.

### Consolidate Conditional Expression

When several conditions produce the same result, combine them with `&&`/`||`, then Extract Function on the combined condition to name the reason. **Test.**

Only when the conditions are genuinely one reason. Independent checks that coincidentally share a result should stay separate.

### Replace Conditional with Polymorphism

Use when the same type-switch appears at three or more sites.

1. Create a class per branch (or a lookup keyed by type) with a factory returning the right one.
2. Move the switch into a superclass method or interface default.
3. Move one branch's body into its subclass override. **Test.**
4. Repeat per branch, **testing** after each.
5. Delete the now-empty superclass body, or leave it as the default case.

At one or two call sites this is over-machinery. Leave the conditional.

### Remove Flag Argument

1. Create an explicit function per flag value, each calling the original with the literal. **Test.**
2. Migrate callers to the explicit functions one at a time, **testing** after each.
3. Inline the original away.

---

## Data and parameters

### Introduce Parameter Object / Extract Class

For a data clump — the same group of values travelling together.

1. Create the structure (empty is fine to start).
2. Add it as a parameter via Change Function Declaration. **Test.**
3. Move fields into it one at a time, updating callers and **testing** after each.
4. Once all callers pass the object, remove the loose parameters.
5. Move behavior that operates only on those fields onto the new type. This step is where the value is; a parameter object with no methods is a tuple with ceremony.

### Preserve Whole Object

When a caller pulls several values out of one object only to pass them separately, pass the object. Change Function Declaration to accept it, **test**, then delete the extracted locals.

Do not apply when it would create a dependency the callee should not have — passing a whole request object into a pure calculation exports coupling.

### Replace Primitive with Object

1. Encapsulate the field if it is bare.
2. Create the wrapping type with a value accessor.
3. Change the setter to construct it and the getter to unwrap. **Test.**
4. Migrate callers to the type, **testing** as you go.
5. Move validation and formatting behavior onto the type.

### Replace Temp with Query

Where a local caches a computed value, extract the computation into a function and call it at each use. **Test.** Skip when the computation is expensive and the loop is hot — that is a behavior change at the boundary.

---

## Removing structure

### Remove Middle Man

When a class does little but delegate: add direct accessors to the real target, migrate callers one at a time (**test** each), then delete the delegating methods.

### Collapse Hierarchy

When a subclass no longer differs meaningfully: pull up or push down remaining members, **test**, then merge and delete the empty class.

### Remove Dead Code

Confirm unreachability by static reference **and** a grep for the bare name (reflection, string dispatch, serialized names, templates). Delete. **Test.** Version control is the archive; commenting it out is not.

---

## Step-size rule

If any step above cannot be made green on its own, split it. Fowler: if it hurts, the steps are too big. The correct response to a red suite mid-refactor is `git reset --hard` to the last green commit, not a debugging session — the half-applied state carries no information worth recovering.
