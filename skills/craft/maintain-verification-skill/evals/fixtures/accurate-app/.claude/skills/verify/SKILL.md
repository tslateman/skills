---
name: verify
description: Drive the timesheet app end to end to prove a change works. Use before merging any change to entry or approval.
---

# verify

## Setup

    just up && just seed

## Feature map

| Feature        | Target                      | Proof                                                |
| -------------- | --------------------------- | ----------------------------------------------------- |
| Log hours      | `just drive log-hours`      | Click `[data-testid="hours-submit"]`, row shows the total |
| Approve week   | `just drive approve-week`   | Click `[data-testid="week-approve"]`, status `approved`   |

## Not covered

- Payroll export. It runs on a nightly cron with no UI entry point, so nothing
  here drives it.
