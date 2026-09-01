"""Two retry helpers that grew independently. Both are live."""

import time


def with_retries(fn, attempts: int = 3, delay: float = 0.5):
    """Used by pms_client, vendor_sync, and webhook_dispatch."""
    last = None
    for n in range(attempts):
        try:
            return fn()
        except TimeoutError as exc:
            last = exc
            time.sleep(delay * (2**n))
    raise last


def retry(fn, times: int = 3, backoff: float = 0.5):
    """Used by legacy_importer only."""
    err = None
    for n in range(times):
        try:
            return fn()
        except TimeoutError as exc:
            err = exc
            time.sleep(backoff * (2**n))
    raise err
