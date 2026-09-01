"""Booking flow. Owns the overlap rule and the status transitions."""

from datetime import date

from .reservation import Reservation


class ReservationService:
    def __init__(self, db):
        self.db = db

    def create(self, room_id: int, guest_id: int, check_in: date, check_out: date) -> Reservation:
        if check_out <= check_in:
            raise ValueError("check_out must be after check_in")

        existing = self.db.query(
            "select * from reservation where room_id = ? and status != 'cancelled'",
            room_id,
        )
        for row in existing:
            if check_in < row["check_out"] and row["check_in"] < check_out:
                raise ValueError(f"room {room_id} is already booked for those dates")

        res = Reservation(
            id=None,
            room_id=room_id,
            guest_id=guest_id,
            check_in=check_in,
            check_out=check_out,
        )
        res.rate_cents = self._rate_for(room_id, check_in, check_out)
        res.status = "confirmed"
        res.save(self.db)
        return res

    def cancel(self, res: Reservation) -> None:
        if res.status == "checked_out":
            raise ValueError("cannot cancel a completed stay")
        res.status = "cancelled"
        res.save(self.db)

    def _rate_for(self, room_id: int, check_in: date, check_out: date) -> int:
        room = self.db.get("room", room_id)
        return room["base_rate"] * (check_out - check_in).days
