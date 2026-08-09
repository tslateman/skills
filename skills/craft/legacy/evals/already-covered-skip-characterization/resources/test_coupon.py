from datetime import date

import pytest

from coupon import CouponBook


@pytest.fixture
def book():
    return CouponBook(
        {
            "SAVE10": {
                "expires_on": date(2030, 1, 1),
                "minimum_order": 50.0,
                "uses_remaining": 5,
                "percent_off": 10,
            },
            "EXPIRED": {
                "expires_on": date(2020, 1, 1),
                "minimum_order": 0.0,
                "uses_remaining": 5,
                "percent_off": 50,
            },
            "USEDUP": {
                "expires_on": date(2030, 1, 1),
                "minimum_order": 0.0,
                "uses_remaining": 0,
                "percent_off": 50,
            },
        },
        today=date(2026, 6, 1),
    )


def test_unknown_code_is_not_redeemable(book):
    assert book.is_redeemable("NOPE", 100.0) is False


def test_expired_coupon_is_not_redeemable(book):
    assert book.is_redeemable("EXPIRED", 100.0) is False


def test_exhausted_coupon_is_not_redeemable(book):
    assert book.is_redeemable("USEDUP", 100.0) is False


def test_order_below_minimum_is_not_redeemable(book):
    assert book.is_redeemable("SAVE10", 49.99) is False


def test_order_at_minimum_is_redeemable(book):
    assert book.is_redeemable("SAVE10", 50.0) is True


def test_discount_is_a_percentage_of_the_order(book):
    assert book.discount_for("SAVE10", 200.0) == 20.0


def test_discount_is_zero_when_not_redeemable(book):
    assert book.discount_for("EXPIRED", 200.0) == 0.0
