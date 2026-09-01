"""Reservation record. Rules live elsewhere; see reservation_service."""

from dataclasses import dataclass, field
from datetime import date


@dataclass
class Reservation:
    id: int | None
    room_id: int
    guest_id: int
    check_in: date
    check_out: date
    status: str = "pending"
    rate_cents: int = 0
    notes: list[str] = field(default_factory=list)

    def save(self, db) -> None:
        if self.id is None:
            self.id = db.insert("reservation", self.__dict__)
        else:
            db.update("reservation", self.id, self.__dict__)

    def nights(self) -> int:
        return (self.check_out - self.check_in).days
