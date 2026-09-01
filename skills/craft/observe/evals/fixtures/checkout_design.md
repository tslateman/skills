# Express checkout: design, pre-implementation

A guest taps "check out" in the mobile app. We settle the folio, release the
room key credential, and email a receipt.

## Flow

1. App calls `POST /v1/stays/{id}/checkout`.
2. We read the folio and compute the final balance.
3. If the balance is non-zero we charge the card on file through Stripe.
4. We call the lock vendor to revoke the mobile key. This is a third-party HTTP
   call, p99 around 2.4s, and it fails roughly 0.5% of the time.
5. We enqueue the receipt email.
6. We mark the stay closed and return 200.

## Decisions already made

- Steps 3 and 4 are not in one transaction. A card can be charged and the key
  revocation can still fail.
- On a step 4 failure we retry twice, then close the stay anyway and file a
  housekeeping task to re-key the door by hand.
- The receipt email is fire and forget through the existing queue.

## Open

Nothing about instrumentation has been decided.
