"""Rate lookup gateway. Already instrumented; treat as the reference."""

import logging
import time

from .metrics import counter, histogram
from .tracing import span

log = logging.getLogger(__name__)

requests = counter("rate_gateway_requests_total", labels=("vendor", "outcome"))
latency = histogram(
    "rate_gateway_request_seconds",
    labels=("vendor",),
    buckets=(0.05, 0.1, 0.25, 0.5, 1, 2.5, 5),
)
inflight = counter("rate_gateway_inflight", labels=("vendor",))


def fetch_rate(vendor: str, room_code: str, night: str) -> int | None:
    started = time.monotonic()
    inflight.inc(vendor=vendor)
    with span("rate_gateway.fetch", vendor=vendor, room_code=room_code):
        try:
            rate = _call(vendor, room_code, night)
        except TimeoutError:
            requests.inc(vendor=vendor, outcome="timeout")
            log.warning(
                "rate lookup timed out",
                extra={"vendor": vendor, "room_code": room_code, "night": night},
            )
            return None
        except ValueError:
            requests.inc(vendor=vendor, outcome="rejected")
            log.warning(
                "rate lookup rejected",
                extra={"vendor": vendor, "room_code": room_code, "night": night},
            )
            return None
        else:
            requests.inc(vendor=vendor, outcome="ok")
            return rate
        finally:
            latency.observe(time.monotonic() - started, vendor=vendor)
            inflight.dec(vendor=vendor)


def _call(vendor: str, room_code: str, night: str) -> int:
    raise NotImplementedError
