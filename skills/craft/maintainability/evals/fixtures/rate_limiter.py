"""Sliding-window rate limiter with idle-refill burst credit."""

import time
from collections.abc import Callable
from dataclasses import dataclass, field


@dataclass
class _KeyState:
    events: list[float] = field(default_factory=list)
    credit: float | None = None
    last_seen: float = 0.0


class SlidingWindowRateLimiter:
    """Allows up to `limit` calls per `window_seconds` for each key. When the
    window is full, a burst credit of up to `burst` extra calls is available;
    credit refills at one call per `burst_refill_seconds` of idle time."""

    def __init__(
        self,
        limit: int,
        window_seconds: float,
        burst: int = 0,
        burst_refill_seconds: float = 30.0,
        clock: Callable[[], float] = time.monotonic,
    ) -> None:
        if limit < 1:
            raise ValueError("limit must be at least 1")
        self._limit = limit
        self._window = window_seconds
        self._burst = burst
        self._burst_refill = burst_refill_seconds
        self._clock = clock
        self._state: dict[str, _KeyState] = {}
        # A key idle this long has refilled to full credit and holds no events,
        # so dropping it is indistinguishable from keeping it.
        self._inert_after = max(window_seconds, burst * burst_refill_seconds)
        self._last_sweep = 0.0

    def allow(self, key: str) -> bool:
        now = self._clock()
        self._evict_inert(now)
        state = self._state.setdefault(key, _KeyState(last_seen=now))
        events = state.events

        drop = 0
        while drop < len(events) and events[drop] <= now - self._window:
            drop += 1
        if drop:
            del events[:drop]

        if len(events) < self._limit:
            events.append(now)
            state.last_seen = now
            return True

        if self._burst:
            credit = self._burst if state.credit is None else state.credit
            credit = min(
                float(self._burst),
                credit + (now - state.last_seen) / self._burst_refill,
            )
            if credit >= 1.0:
                state.credit = credit - 1.0
                events.append(now)
                state.last_seen = now
                return True
            state.credit = credit

        state.last_seen = now
        return False

    def reset(self, key: str) -> None:
        self._state.pop(key, None)

    def _evict_inert(self, now: float) -> None:
        if now - self._last_sweep < self._window:
            return
        self._last_sweep = now
        cutoff = now - self._window
        for key, state in list(self._state.items()):
            idle = now - state.last_seen
            if idle >= self._inert_after and not any(e > cutoff for e in state.events):
                del self._state[key]
