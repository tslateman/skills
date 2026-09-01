"""Rate plan resolution. One module, one job, no wrappers."""

from datetime import date

from .calendar import season_for


class RatePlan:
    """Resolves the nightly rate for a room on a date.

    Callers pass a room and a date and get cents back. Seasonality, weekend
    uplift, length-of-stay discounting and the corporate override are all
    resolved inside; none of them appear in the signature.
    """

    def __init__(self, base_cents: int, weekend_uplift: float = 0.15) -> None:
        self._base = base_cents
        self._weekend_uplift = weekend_uplift
        self._overrides: dict[str, int] = {}

    def set_corporate_rate(self, account: str, cents: int) -> None:
        self._overrides[account] = cents

    def nightly_cents(self, night: date, nights_booked: int, account: str | None = None) -> int:
        if account in self._overrides:
            return self._overrides[account]
        rate = int(self._base * season_for(night).multiplier)
        if night.weekday() >= 4:
            rate = int(rate * (1 + self._weekend_uplift))
        if nights_booked >= 7:
            rate = int(rate * 0.9)
        elif nights_booked >= 4:
            rate = int(rate * 0.95)
        return rate
