# Research Patterns

Detailed patterns for common technical research scenarios.

## Pattern: "Should we use X?"

**Goal:** Evaluate whether a specific library/framework/service fits the use case.

**Process:**

1. Identify what problem X solves
2. Check if the codebase already has a solution
3. Research X's fitness for the specific use case
4. Identify alternatives worth comparing
5. Make a recommendation

**Example: "Should we use Zod for validation?"**

```markdown
## Summary

Zod is a strong fit for TypeScript validation with good DX and bundle size.

## Investigation

### Current State

- Codebase uses manual validation in `/src/validators/`
- No existing schema validation library
- TypeScript throughout

### Zod Evaluation

- **Maintenance:** Active, v3.23 released Jan 2026
- **Size:** 13KB gzipped (acceptable)
- **TypeScript:** Native, excellent inference
- **API:** Fluent, composable, well-documented

### Alternatives Considered

- **Yup:** Larger, worse TS inference
- **io-ts:** FP style, steeper learning curve
- **Valibot:** Smaller but less mature ecosystem

## Recommendation

Adopt Zod. It aligns with TypeScript-first approach and has the ecosystem maturity needed.

Sources:

- [Zod Documentation](https://zod.dev)
- [Bundlephobia](https://bundlephobia.com/package/zod)
```

## Pattern: "X vs Y"

**Goal:** Compare two or more options head-to-head.

**Process:**

1. Establish comparison criteria based on actual needs
2. Research each option against the criteria
3. Build comparison table
4. Recommend based on priorities

**Example: "Prisma vs Drizzle for our API"**

```markdown
## Summary

Drizzle offers better performance and SQL control; Prisma offers better DX and ecosystem.

## Comparison

| Criterion         | Prisma                     | Drizzle                 |
| ----------------- | -------------------------- | ----------------------- |
| Query performance | Good, some overhead        | Excellent, near-raw SQL |
| Type safety       | Excellent                  | Excellent               |
| Migration DX      | Excellent (prisma migrate) | Good (drizzle-kit)      |
| Raw SQL escape    | Awkward                    | Native                  |
| Bundle size       | Large (~2MB)               | Small (~50KB)           |
| Ecosystem         | Mature, many tools         | Growing rapidly         |
| Learning curve    | Low                        | Medium                  |

## Context

- API handles 10K req/min, performance matters
- Team comfortable with SQL
- Existing Prisma usage in other services

## Recommendation

For new services: Drizzle, given performance requirements and SQL comfort.
For existing Prisma services: Keep Prisma, migration cost not justified.

Sources:

- [Prisma docs](https://prisma.io/docs)
- [Drizzle docs](https://orm.drizzle.team)
- [Benchmark comparison](https://orm-benchmark.io)
```

## Pattern: "How does X work?"

**Goal:** Deep technical understanding of a system, library, or concept.

**Process:**

1. Start with official documentation
2. Find architecture diagrams or explanations
3. Look for source code if needed
4. Summarize the key mechanisms

**Example: "How does React Server Components work?"**

```markdown
## Summary

RSC separates components into Server (no client JS) and Client (interactive) components, streaming HTML with embedded data.

## Key Mechanisms

### Component Types

- **Server Components:** Run only on server, can async/await, access DB directly
- **Client Components:** Run on both (SSR + hydration), handle interactivity
- Marked with `'use client'` directive at file top

### Rendering Flow

1. Server renders Server Components to RSC Payload (serialized React tree)
2. Client Components in payload are placeholders with props
3. Payload streamed to client
4. Client reconstructs tree, hydrates Client Components

### Data Serialization

- Props between Server→Client must be serializable
- Functions, classes, symbols cannot cross boundary
- Promises can be serialized (Suspense integration)

### Bundle Impact

- Server Component code never ships to client
- Reduces JS bundle significantly for content-heavy pages

## Practical Implications

- Default to Server Components
- Add 'use client' only for: useState, useEffect, event handlers, browser APIs
- Data fetching moves to Server Components (no useEffect waterfalls)

Sources:

- [React RFC](https://github.com/reactjs/rfcs/blob/main/text/0188-server-components.md)
- [Next.js RSC docs](https://nextjs.org/docs/app/building-your-application/rendering/server-components)
```

## Pattern: "What are the options for X?"

**Goal:** Survey the landscape of solutions for a problem.

**Process:**

1. Define the problem clearly
2. Identify major categories of solutions
3. Research representative options in each category
4. Present as a decision tree or matrix

**Example: "What are the options for real-time updates?"**

```markdown
## Summary

Four main approaches: polling, SSE, WebSockets, or third-party services. Choice depends on update frequency and complexity needs.

## Options

### 1. Polling

- **How:** Client requests every N seconds
- **Pros:** Simple, works everywhere, no infrastructure
- **Cons:** Latency = poll interval, wasted requests
- **Use when:** Updates infrequent (>30s), simplicity paramount

### 2. Server-Sent Events (SSE)

- **How:** Server pushes over HTTP, one-way
- **Pros:** Simple, auto-reconnect, works with HTTP/2
- **Cons:** One-way only, limited browser connections
- **Use when:** Server→client only, moderate scale

### 3. WebSockets

- **How:** Bidirectional persistent connection
- **Pros:** Low latency, bidirectional, efficient
- **Cons:** Infrastructure complexity, connection management
- **Use when:** Bidirectional needed, high frequency, <10K concurrent

### 4. Third-Party Services

- **Examples:** Pusher, Ably, Firebase Realtime
- **Pros:** Managed scale, presence, history
- **Cons:** Cost, vendor lock-in, latency
- **Use when:** >10K concurrent, global distribution, rapid development

## Decision Tree
```

Need bidirectional?
→ Yes: WebSocket or third-party
→ No: SSE (or polling if very infrequent)

Scale > 10K concurrent?
→ Yes: Third-party or managed WebSocket service
→ No: Self-hosted fine

```

Sources:
- [MDN SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)
- [MDN WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)
```

## Pattern: "Is X still the right choice?"

**Goal:** Re-evaluate a past technology decision.

**Process:**

1. Understand why X was chosen originally
2. Research what's changed since then
3. Identify pain points with current approach
4. Evaluate migration cost vs benefit

**Example: "Is Moment.js still the right choice?"**

```markdown
## Summary

No. Moment.js is deprecated; migrate to date-fns or Temporal API.

## Original Context

- Chosen in 2019 for date handling
- Best option at the time

## What's Changed

- Moment.js officially deprecated Sept 2020
- No new features, maintenance-only security fixes
- 67KB gzipped (massive by 2026 standards)
- Mutable API causes bugs

## Current Pain Points

- Bundle size bloating client
- Occasional mutation bugs
- Contributors unfamiliar with API

## Alternatives

| Option   | Size | Immutable  | Tree-shakeable |
| -------- | ---- | ---------- | -------------- |
| date-fns | 13KB | Yes        | Yes            |
| Day.js   | 2KB  | Via plugin | Partial        |
| Temporal | 0KB  | Yes        | N/A (native)   |

## Recommendation

Migrate to date-fns incrementally. Temporal API still Stage 3, not ready for production.

Migration cost: ~2 days for 47 Moment usages found via grep.

Sources:

- [Moment.js deprecation notice](https://momentjs.com/docs/#/-project-status/)
- [date-fns docs](https://date-fns.org)
- [Temporal proposal](https://tc39.es/proposal-temporal/docs/)
```

## Anti-Patterns

### Research Theater

Gathering information without a decision to inform. Always start with: "What decision does this research support?"

### Analysis Paralysis

Researching indefinitely instead of making a reversible decision. Set a timebox. Good enough beats perfect.

### Source Blindness

Treating all sources equally. A random Medium post is not equal to official documentation.

### Recency Bias

Assuming newest = best. Stable, boring technology often wins.

### Ignoring Context

Recommending the "best" option without considering team expertise, existing code, or constraints.
