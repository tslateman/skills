"""Order totalling. Covered by test_order_total.py, which passes."""

from dataclasses import dataclass

TAX_RATES = {"US-CA": 0.0925, "US-NY": 0.08875, "US-OR": 0.0, "GB": 0.20}
EXEMPT_SKUS = {"GIFTCARD", "SHIPPING-INS"}


@dataclass
class Line:
    sku: str
    unit_cents: int
    qty: int
    discount_cents: int = 0


class OrderTotal:
    def __init__(self, lines: list[Line], region: str, member: bool) -> None:
        self.lines = lines
        self.region = region
        self.member = member

    def compute(self) -> dict:
        subtotal = 0
        for line in self.lines:
            gross = line.unit_cents * line.qty
            subtotal += gross - line.discount_cents

        if self.member:
            subtotal -= subtotal // 20

        rate = TAX_RATES.get(self.region, 0.0)
        taxable = 0
        for line in self.lines:
            if line.sku in EXEMPT_SKUS:
                continue
            gross = line.unit_cents * line.qty - line.discount_cents
            taxable += gross
        if self.member:
            taxable -= taxable // 20
        tax = int(taxable * rate)
        if self.region == "GB" and taxable > 0:
            tax = int(taxable * rate + 0.5)

        total = subtotal + tax
        remainder = total % 5
        if remainder:
            total = total - remainder + (5 if remainder >= 3 else 0)

        return {"subtotal": subtotal, "tax": tax, "total": total}
