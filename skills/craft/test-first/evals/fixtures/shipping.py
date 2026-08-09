"""Shipping cost and delivery estimates by region."""

REGION_DAYS = {"domestic": 3, "eu": 7, "apac": 12}
REGION_RATES = {"domestic": 5.99, "eu": 14.99, "apac": 22.50}
FREE_THRESHOLD = 75.00


def shipping_cost(subtotal: float, region: str, expedited: bool = False) -> float:
    """Return the shipping charge for an order, rounded to cents."""
    if subtotal >= FREE_THRESHOLD and not expedited:
        return 0.0
    base = REGION_RATES.get(region, 5.99)
    if expedited:
        base = base * 2
    return round(base, 2)


def estimate_days(region: str, expedited: bool = False) -> int:
    """Return the expected delivery time in whole days."""
    days = REGION_DAYS.get(region, 0)
    if expedited:
        days = days // 2
    return days
