"""Existing suite for the folio calculator. Every collaborator is mocked."""

from unittest.mock import MagicMock, call, patch

from folio import Folio


@patch("folio.TaxTable")
@patch("folio.RateCard")
@patch("folio.Ledger")
def test_total_calls_ledger_once(ledger, rate_card, tax_table):
    rate_card.return_value.lookup.return_value = 1000
    tax_table.return_value.rate_for.return_value = 0.1
    ledger.return_value.post.return_value = None

    f = Folio(stay_id=7)
    f.total()

    assert ledger.return_value.post.call_count == 1


@patch("folio.TaxTable")
@patch("folio.RateCard")
@patch("folio.Ledger")
def test_total_calls_rate_card_with_stay_id(ledger, rate_card, tax_table):
    rate_card.return_value.lookup.return_value = 1000
    tax_table.return_value.rate_for.return_value = 0.1

    Folio(stay_id=7).total()

    assert rate_card.return_value.lookup.call_args == call(7)


@patch("folio.TaxTable")
@patch("folio.RateCard")
@patch("folio.Ledger")
def test_total_invokes_in_order(ledger, rate_card, tax_table):
    manager = MagicMock()
    manager.attach_mock(rate_card, "rate_card")
    manager.attach_mock(tax_table, "tax_table")
    rate_card.return_value.lookup.return_value = 1000
    tax_table.return_value.rate_for.return_value = 0.1

    Folio(stay_id=7).total()

    assert manager.mock_calls[0][0].startswith("rate_card")


@patch("folio.TaxTable")
@patch("folio.RateCard")
@patch("folio.Ledger")
def test_total_uses_private_helper(ledger, rate_card, tax_table):
    rate_card.return_value.lookup.return_value = 1000
    tax_table.return_value.rate_for.return_value = 0.1

    f = Folio(stay_id=7)
    with patch.object(f, "_apply_rounding", wraps=f._apply_rounding) as spy:
        f.total()

    assert spy.called
