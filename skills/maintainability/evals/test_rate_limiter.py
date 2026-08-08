"""Pins the rate_limiter fixture's behavior.

The clean-deep-module-no-filler eval asserts that a reviewer finds nothing
significant here. That assertion is only meaningful while the module is
actually correct, so these checks guard the fixture itself. Run them after any
edit to rate_limiter.py.

    python3 test_rate_limiter.py

Lives outside fixtures/ on purpose: the harness copies that whole directory
into the directory under review, and a test file sitting next to the module
would change what the reviewer sees.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "fixtures"))

from rate_limiter import SlidingWindowRateLimiter


class FakeClock:
    def __init__(self) -> None:
        self.now = 0.0

    def __call__(self) -> float:
        return self.now


def test_limits_within_window() -> None:
    clock = FakeClock()
    rl = SlidingWindowRateLimiter(limit=2, window_seconds=10, clock=clock)
    assert [rl.allow("a") for _ in range(3)] == [True, True, False]


def test_window_slides() -> None:
    clock = FakeClock()
    rl = SlidingWindowRateLimiter(limit=2, window_seconds=10, clock=clock)
    for _ in range(3):
        rl.allow("a")
    clock.now = 11.0
    assert rl.allow("a") is True


def test_burst_credit_spends_and_refills() -> None:
    clock = FakeClock()
    rl = SlidingWindowRateLimiter(
        limit=1, window_seconds=10, burst=1, burst_refill_seconds=5, clock=clock
    )
    assert rl.allow("b") is True
    assert rl.allow("b") is True
    assert rl.allow("b") is False
    clock.now = 5.0
    assert rl.allow("b") is True


def test_eviction_bounds_memory() -> None:
    clock = FakeClock()
    rl = SlidingWindowRateLimiter(limit=5, window_seconds=10, clock=clock)
    for i in range(1000):
        rl.allow(f"k{i}")
    assert len(rl._state) == 1000
    clock.now = 100.0
    rl.allow("trigger")
    assert len(rl._state) == 1


def test_eviction_is_behavior_neutral() -> None:
    """An evicted key must behave exactly like one whose state was retained."""
    clock = FakeClock()
    retained = SlidingWindowRateLimiter(
        limit=1, window_seconds=10, burst=2, burst_refill_seconds=5, clock=clock
    )
    retained.allow("x")
    retained.allow("x")
    clock.now = 1000.0
    after_idle = [retained.allow("x") for _ in range(3)]

    fresh_clock = FakeClock()
    fresh_clock.now = 1000.0
    fresh = SlidingWindowRateLimiter(
        limit=1, window_seconds=10, burst=2, burst_refill_seconds=5, clock=fresh_clock
    )
    assert after_idle == [fresh.allow("x") for _ in range(3)]


def test_reset_clears_state() -> None:
    clock = FakeClock()
    rl = SlidingWindowRateLimiter(limit=1, window_seconds=10, clock=clock)
    rl.allow("z")
    assert rl.allow("z") is False
    rl.reset("z")
    assert rl.allow("z") is True


def test_limit_must_be_positive() -> None:
    try:
        SlidingWindowRateLimiter(limit=0, window_seconds=10)
    except ValueError:
        return
    raise AssertionError("limit=0 must raise ValueError")


if __name__ == "__main__":
    checks = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for check in checks:
        check()
    print(f"{len(checks)} checks pass")
