"""Money value object. Constructing an invalid one is not possible."""

from __future__ import annotations

from dataclasses import dataclass

_MINOR_UNITS = {"USD": 2, "EUR": 2, "JPY": 0, "KWD": 3}


@dataclass(frozen=True)
class Money:
    amount_minor: int
    currency: str

    def __post_init__(self) -> None:
        if self.currency not in _MINOR_UNITS:
            raise ValueError(f"unsupported currency {self.currency!r}")
        if not isinstance(self.amount_minor, int):
            raise TypeError("amount_minor must be a whole number of minor units")

    @classmethod
    def parse(cls, text: str, currency: str) -> Money:
        if currency not in _MINOR_UNITS:
            raise ValueError(f"unsupported currency {currency!r}")
        exponent = _MINOR_UNITS[currency]
        whole, _, frac = text.partition(".")
        frac = (frac + "0" * exponent)[:exponent]
        return cls(int(whole) * 10**exponent + int(frac or 0), currency)

    def __add__(self, other: Money) -> Money:
        if self.currency != other.currency:
            raise ValueError(f"cannot add {self.currency} to {other.currency}")
        return Money(self.amount_minor + other.amount_minor, self.currency)

    def times(self, n: int) -> Money:
        return Money(self.amount_minor * n, self.currency)
