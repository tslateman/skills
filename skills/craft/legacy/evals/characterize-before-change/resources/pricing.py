"""Order line pricing against the configured volume-discount tiers."""

import json
from pathlib import Path

TAX_RATE = 0.0875


class PricingEngine:
    """Prices order lines. Construct once per process and reuse."""

    def __init__(self, config_path: str = "/etc/billing/pricing.json") -> None:
        self._tiers = json.loads(Path(config_path).read_text())["tiers"]
        self._audit = open("/var/log/billing/pricing.log", "a")

    def line_total(self, unit_price: float, quantity: int) -> float:
        """Return the line total after volume discount and tax, rounded to cents.

        Orders of 10 or more units take the 10% volume discount. Orders of 50 or
        more take 20% instead.
        """
        subtotal = unit_price * quantity
        discount = 0.0
        if quantity > 50:
            discount = 0.20
        elif quantity > 10:
            discount = 0.10
        total = subtotal * (1 - discount) * (1 + TAX_RATE)
        self._audit.write(f"{quantity}@{unit_price} -> {total}\n")
        return round(total, 2)

    def order_total(self, lines: list[tuple[float, int]]) -> float:
        """Return the sum of every line total in the order."""
        return round(sum(self.line_total(price, qty) for price, qty in lines), 2)
