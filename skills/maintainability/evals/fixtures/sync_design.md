# Program Design: Device Config Sync Worker

Syncs device configuration bundles from the platform to partner systems on a
schedule. First vendor is VendorA. VendorB follows next quarter.

## Module layout

```
src/sync
├── scheduler.py        # SyncScheduler
├── orchestrator.py     # SyncOrchestrator
├── payload_builder.py  # PayloadBuilder
├── vendor_client.py    # VendorClient
└── state_store.py      # SyncStateStore
```

## Modules and interfaces

### SyncScheduler

```
next_batch(now: datetime) -> list[BundleRef]
mark_done(ref: BundleRef) -> None
```

Reads due bundles from the queue table. Raises `ScheduleEmptyError` when
nothing is due; the caller decides how long to sleep.

### SyncOrchestrator

```
run_batch(refs: list[BundleRef]) -> BatchResult
```

For each ref: calls `PayloadBuilder.build`, passes the result to
`VendorClient.push`, then calls `SyncStateStore.record`. Raises
`OrchestrationError` wrapping whatever the inner module raised.

### PayloadBuilder

```
build(bundle: ConfigBundle, frame_version: int) -> bytes
```

Produces the VendorA binary frame: 12-byte header (magic, version, body length),
TLV body, trailing CRC16. `frame_version` comes from `WorkerConfig`.

### VendorClient

```
push(payload: bytes) -> PushReceipt
```

Before sending, re-parses the frame header to validate body length and
recomputes the CRC16 as a defense against builder bugs. Sends over mTLS.
Raises `VendorTimeoutError`, `VendorRejectionError`, or `FramingError`.

### SyncStateStore

```
record(ref: BundleRef, receipt: PushReceipt) -> None
get_state(ref: BundleRef) -> SyncState
get_vendor_b_state(ref: BundleRef) -> VendorBSyncState   # ready for next quarter
```

DynamoDB-backed. Raises `StateConflictError` on concurrent writes.

## Configuration

`WorkerConfig` is loaded at startup and passed into every module:

```
WorkerConfig:
  retry_count: int
  backoff_base_ms: int
  backoff_max_ms: int
  frame_version: int
  vendor_timeout_ms: int
```

Callers tune retry and backoff per environment.

## Call stack

```
worker_main
  SyncScheduler.next_batch
  SyncOrchestrator.run_batch
    PayloadBuilder.build
    VendorClient.push
    SyncStateStore.record
```

`worker_main` catches `ScheduleEmptyError`, `OrchestrationError`,
`VendorTimeoutError`, `VendorRejectionError`, `FramingError`, and
`StateConflictError`, and decides retry vs. dead-letter per type.
