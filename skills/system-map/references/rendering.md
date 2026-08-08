# Rendering

Every snippet below was validated against the Mermaid Chart renderer on 2026-08-02 and returned `valid: true`. That is the current Mermaid engine — **not** GitHub's, which lags by versions. Target the renderer the reader will actually use, and check there before shipping.

## Choosing the syntax

| Situation                                                              | Use                                         |
| ---------------------------------------------------------------------- | ------------------------------------------- |
| Renderer is current Mermaid and C4 semantics matter                    | `C4Context` / `C4Container` / `C4Component` |
| Must render in a GitHub README or an unknown viewer                    | `flowchart` fallback                        |
| Stakeholder-facing, will be edited by hand, needs to survive a meeting | `duet:excalidraw`                           |

Mermaid's C4 support is **experimental** by Mermaid's own documentation, and layout control is limited — you get `UpdateLayoutConfig` and per-relationship offsets, not real positioning. When a diagram has to look a specific way, the flowchart fallback gives more control and the Excalidraw path gives full control.

## C4 element vocabulary

| Element                                              | Use for                                          |
| ---------------------------------------------------- | ------------------------------------------------ |
| `Person(id, "Name", "Description")`                  | A human role inside your organization            |
| `Person_Ext(...)`                                    | A human role outside it                          |
| `System(id, "Name", "Description")`                  | The system under description, or one you own     |
| `System_Ext(...)`                                    | A system someone else owns                       |
| `Container(id, "Name", "Technology", "Description")` | A deployable or runnable unit                    |
| `ContainerDb(...)`                                   | A datastore                                      |
| `ContainerQueue(...)`                                | A broker or queue                                |
| `Component(id, "Name", "Technology", "Description")` | A grouping inside one container                  |
| `Enterprise_Boundary(id, "Name") { }`                | Organizational ownership boundary                |
| `System_Boundary(id, "Name") { }`                    | The system boundary at container level           |
| `Container_Boundary(id, "Name") { }`                 | The container boundary at component level        |
| `Rel(from, to, "Verb phrase", "Protocol")`           | A relationship; fourth argument is the mechanism |

`Rel_U` / `Rel_D` / `Rel_L` / `Rel_R` nudge direction. `UpdateRelStyle(from, to, $offsetX="10", $offsetY="-20")` moves a label off a collision.

## Level 1 · Context

```mermaid
C4Context
    title System Context diagram for Booking Platform

    Person(guest, "Guest", "Books and manages stays")
    Person(agent, "Support Agent", "Resolves booking issues")
    Person_Ext(partner, "Hotel Partner", "Manages inventory and rates")

    Enterprise_Boundary(org, "Acme Travel") {
        System(booking, "Booking Platform", "Reservations, pricing, and guest self-service")
        System_Ext(warehouse, "Data Warehouse", "Nightly reservation extracts")
    }

    System_Ext(payments, "Stripe", "Card capture and payouts")

    Rel(guest, booking, "Books stays using")
    Rel(agent, booking, "Resolves bookings in")
    Rel(partner, booking, "Loads inventory into")
    Rel(booking, payments, "Captures payment via", "JSON/HTTPS")
    Rel(booking, warehouse, "Exports reservations to", "Nightly batch")
```

Note the support agent and the warehouse. Those are the actors level 1 diagrams usually omit.

## Level 2 · Containers

```mermaid
C4Container
    title Container diagram for Booking Platform

    Person(guest, "Guest", "Books and manages stays")
    System_Ext(payments, "Stripe", "Card capture and payouts")

    System_Boundary(booking, "Booking Platform") {
        Container(web, "Booking Web App", "TypeScript, React", "Search, book, and manage reservations")
        Container(api, "Booking API", "Python, FastAPI", "Reservation lifecycle and pricing")
        ContainerDb(db, "Reservations DB", "PostgreSQL 16", "Reservations, guests, rate plans")
        ContainerQueue(events, "Booking Events", "Amazon SQS", "Reservation state changes")
    }

    Rel(guest, web, "Books stays using", "HTTPS")
    Rel(web, api, "Calls", "JSON/HTTPS")
    Rel(api, db, "Reads from and writes to", "SQL/TCP")
    Rel(api, events, "Publishes reservation events to", "HTTPS")
    Rel(api, payments, "Captures payment via", "JSON/HTTPS")

    UpdateRelStyle(api, payments, $offsetY="-20")
```

Every container carries its technology; every relationship carries a verb and a protocol.

## Fallback · Flowchart

Renders anywhere Mermaid renders at all, including older GitHub. Boundaries become `subgraph`, datastores use the cylinder shape, queues use the subroutine shape, and external things get a dashed stroke.

```mermaid
flowchart TB
    guest["Guest<br/><i>Person</i>"]
    partner["Hotel Partner<br/><i>Person, external</i>"]

    subgraph platform["Booking Platform"]
        web["Booking Web App<br/><i>TypeScript, React</i>"]
        api["Booking API<br/><i>Python, FastAPI</i>"]
        db[("Reservations DB<br/><i>PostgreSQL 16</i>")]
        events[["Booking Events<br/><i>Amazon SQS</i>"]]
    end

    payments["Stripe<br/><i>External system</i>"]

    guest -->|"Books stays using<br/>HTTPS"| web
    partner -->|"Loads inventory into<br/>HTTPS"| api
    web -->|"Calls<br/>JSON/HTTPS"| api
    api -->|"Reads from and writes to<br/>SQL/TCP"| db
    api -->|"Publishes events to<br/>HTTPS"| events
    api -->|"Captures payment via<br/>JSON/HTTPS"| payments

    classDef external stroke-dasharray: 5 5
    class partner,payments external
```

The fallback loses C4's semantics — nothing enforces that a box is a container rather than a class — so the level discipline moves from the syntax into your head. Keep the title stating the level.

## Layout

- `flowchart TB` stacks vertically and stays readable in a narrow column; `LR` runs wide fast. Prefer `TB` for anything embedded in a document.
- Trim labels hard. One line of identity, one line of technology. A paragraph inside a box is a paragraph that belongs in the prose beside it.
- If the diagram needs manual layout surgery to be legible, it has too many boxes. Split it by level instead.
