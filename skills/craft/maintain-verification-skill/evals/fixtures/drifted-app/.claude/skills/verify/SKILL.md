---
name: verify
description: Drive the invoicing app end to end to prove a change works. Use before merging any change to invoicing.
---

# verify

Last reviewed: March.

## Setup

    just up && just seed

## Feature map

| Feature        | Target                      | Proof                                              |
| -------------- | --------------------------- | -------------------------------------------------- |
| Create invoice | `just drive create-invoice` | Row appears in the list with status `draft`        |
| Send invoice   | `just drive send-invoice`   | Click `[data-testid="send-invoice"]`, status `sent` |
| Record payment | `just drive record-payment` | Balance falls to zero, status `paid`               |
| Export CSV     | `just drive export-csv`     | A file lands in `tmp/export.csv`                   |

## Not covered

Nothing. The map above is complete.
