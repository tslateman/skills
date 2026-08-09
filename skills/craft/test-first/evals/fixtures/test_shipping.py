from unittest.mock import Mock

from shipping import REGION_RATES, estimate_days, shipping_cost


def test_free_shipping_over_threshold():
    assert shipping_cost(80.00, "domestic") == 0.0


def test_under_threshold_charges_domestic_rate():
    assert shipping_cost(20.00, "domestic") == 5.99


def test_shipping_cost_returns_a_value():
    assert shipping_cost(10.00, "eu")


def test_expedited_doubles_the_base_rate():
    expected = round(REGION_RATES.get("eu", 5.99) * 2, 2)
    assert shipping_cost(10.00, "eu", expedited=True) == expected


def test_unknown_region_estimates_zero_days():
    assert estimate_days("antarctica") == 0


def test_unknown_region_charges_domestic_rate():
    assert shipping_cost(10.00, "antarctica") == 5.99


def test_quote_calls_the_rate_service():
    service = Mock()
    service.lookup.return_value = 5.99
    service.quote("domestic", 10.00)
    assert service.quote.called
