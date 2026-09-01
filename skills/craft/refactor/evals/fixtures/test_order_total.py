from order_total import Line, OrderTotal


def test_single_line_no_tax_region():
    t = OrderTotal([Line("WIDGET", 1000, 2)], "US-OR", member=False).compute()
    assert t["subtotal"] == 2000
    assert t["tax"] == 0
    assert t["total"] == 2000


def test_tax_applied_to_non_exempt_only():
    lines = [Line("WIDGET", 1000, 1), Line("GIFTCARD", 5000, 1)]
    t = OrderTotal(lines, "US-CA", member=False).compute()
    assert t["subtotal"] == 6000
    assert t["tax"] == 92


def test_member_discount_reduces_subtotal_and_taxable():
    t = OrderTotal([Line("WIDGET", 2000, 1)], "US-CA", member=True).compute()
    assert t["subtotal"] == 1900
    assert t["tax"] == 175


def test_discount_reduces_line_before_tax():
    t = OrderTotal([Line("WIDGET", 1000, 2, discount_cents=500)], "US-NY", member=False).compute()
    assert t["subtotal"] == 1500
    assert t["tax"] == 133


def test_rounds_to_nearest_nickel_up_from_three():
    t = OrderTotal([Line("WIDGET", 1003, 1)], "US-OR", member=False).compute()
    assert t["total"] == 1005


def test_rounds_down_below_three():
    t = OrderTotal([Line("WIDGET", 1002, 1)], "US-OR", member=False).compute()
    assert t["total"] == 1000
