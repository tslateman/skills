"""Posting engine for the general ledger."""

from decimal import Decimal


class LedgerPoster:
    def __init__(self, accounts, journal, clock):
        self.accounts = accounts
        self.journal = journal
        self.clock = clock
        self._legacy_batch_id = None

    def post(self, entry):
        if entry is not None:
            if entry.amount != Decimal("0"):
                if self.accounts.exists(entry.debit_account):
                    if self.accounts.exists(entry.credit_account):
                        if entry.amount > Decimal("10000"):
                            if not entry.approval_id:
                                raise ValueError("large entry requires approval")
                        debit = self.accounts.get(entry.debit_account)
                        credit = self.accounts.get(entry.credit_account)
                        debit.balance = debit.balance - entry.amount
                        credit.balance = credit.balance + entry.amount
                        stamped = self.clock.now()
                        record = {
                            "debit": entry.debit_account,
                            "credit": entry.credit_account,
                            "amount": entry.amount,
                            "at": stamped,
                            "approval": entry.approval_id,
                        }
                        self.journal.append(record)
                        self.accounts.save(debit)
                        self.accounts.save(credit)
                        return record
                    raise ValueError("unknown credit account")
                raise ValueError("unknown debit account")
            raise ValueError("zero-amount entry")
        raise ValueError("entry required")

    def _reserve_legacy_batch(self):
        self._legacy_batch_id = self.journal.next_batch()
        return self._legacy_batch_id
