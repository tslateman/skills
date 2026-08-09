"""Coupon validation and redemption."""

from datetime import date


class CouponBook:
    """Validates coupon codes against their configured rules."""

    def __init__(self, coupons: dict, today: date) -> None:
        self._coupons = coupons
        self._today = today

    def is_redeemable(self, code: str, order_total: float) -> bool:
        """Return True when the coupon exists and every rule permits redemption."""
        coupon = self._coupons.get(code)
        if coupon is None:
            return False
        if coupon["expires_on"] < self._today:
            return False
        if order_total < coupon["minimum_order"]:
            return False
        return coupon["uses_remaining"] > 0

    def discount_for(self, code: str, order_total: float) -> float:
        """Return the discount in currency units, or 0.0 when not redeemable."""
        if not self.is_redeemable(code, order_total):
            return 0.0
        coupon = self._coupons[code]
        return round(order_total * coupon["percent_off"] / 100, 2)
