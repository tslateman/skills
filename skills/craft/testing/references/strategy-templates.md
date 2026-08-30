# Strategy Templates

Fill-in shapes for the three most common test-design jobs. Reach for the one
that matches what you are testing; the workflow in `SKILL.md` decides what goes
in the blanks.

## For a pure function

```markdown
## Contract

[function name]: [input types] → [output type]

- Promises: [what it guarantees]
- Requires: [what inputs must satisfy]

## Test Cases

- [ ] Empty/zero input
- [ ] Single valid input
- [ ] Multiple valid inputs
- [ ] Boundary values
- [ ] Invalid inputs (error cases)
- [ ] Properties that hold for all inputs
```

## For an API endpoint

```markdown
## Contract

[METHOD /path]: [request] → [response]

- Auth: [required/optional/none]
- Idempotent: [yes/no]

## Test Cases

- [ ] Happy path (valid request → expected response)
- [ ] Validation failures (400)
- [ ] Auth failures (401/403)
- [ ] Not found (404)
- [ ] Concurrent requests
- [ ] Rate limiting
```

## For a UI component

```markdown
## Contract

[Component]: [props] → [rendered output + interactions]

## Test Cases

- [ ] Renders with required props
- [ ] Renders with all optional props
- [ ] User interactions trigger callbacks
- [ ] Loading/error/empty states
- [ ] Accessibility (keyboard nav, screen reader)
```
