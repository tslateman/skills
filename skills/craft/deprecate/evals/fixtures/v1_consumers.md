# Who still calls /api/v1/rooms/availability

Pulled from the gateway access log, trailing 30 days.

| Consumer            | Type     | Daily calls | Contact                  |
| ------------------- | -------- | ----------- | ------------------------ |
| Northwind Travel    | partner  | ~430        | api@northwind.example    |
| Corvus Booking      | partner  | ~350        | dev@corvusbooking.example |
| `nightly_rollup`    | internal | 24          | us                       |

Notes:

- Both partners signed integration agreements in 2024. Neither has a stated
  deprecation window in the contract.
- Northwind reads `available` (the boolean). Corvus reads `nights` and `rate`.
- v2 returns no `available` field. It returns `nights`, and the caller decides.
- v2 requires an explicit `currency`. v1 always answered in USD.
