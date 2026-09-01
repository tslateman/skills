---
name: verify
description: Drive the invoicing app end to end to prove a change works. Use before merging any change to the invoice or payment flows.
---

# verify

Proves the invoicing app works by driving it the way a user does.

## Setup

    just up          # postgres + api + web, waits for /healthz
    just seed        # loads the demo tenant

## Features and how to prove each one

| Feature          | Command                          | Proof                                    |
| ---------------- | -------------------------------- | ---------------------------------------- |
| Create invoice   | `just drive create-invoice`      | Invoice appears in the list with status `draft` |
| Send invoice     | `just drive send-invoice`        | Status flips to `sent`, mailhog holds one message |
| Record payment   | `just drive record-payment`      | Balance falls to zero, status is `paid`  |
| Void invoice     | `just drive void-invoice`        | Status is `void`, balance unchanged      |

Each `just drive` target runs a Playwright script under `verify/` and exits
non-zero on failure. Read the script before changing the feature it covers.

## Teardown

    just down
