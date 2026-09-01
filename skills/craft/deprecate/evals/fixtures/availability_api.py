"""Availability endpoints. v2 shipped last spring; v1 is still routed."""

from datetime import date

from .rooms import Room, RoomRepository


def get_availability_v1(hotel_id: str, start: str, end: str) -> dict:
    repo = RoomRepository(hotel_id)
    rooms = repo.all()
    out = []
    for room in rooms:
        nights = _open_nights(room, date.fromisoformat(start), date.fromisoformat(end))
        out.append(
            {
                "room": room.code,
                "nights": nights,
                "rate": room.base_rate,
                "available": len(nights) > 0,
            }
        )
    return {"rooms": out, "currency": "USD"}


def get_availability_v2(hotel_id: str, start: date, end: date, currency: str) -> dict:
    repo = RoomRepository(hotel_id)
    rooms = [
        {
            "room": room.code,
            "nights": _open_nights(room, start, end),
            "rate": room.rate_in(currency),
        }
        for room in repo.all()
    ]
    return {"rooms": rooms, "currency": currency}


def _open_nights(room: Room, start: date, end: date) -> list[date]:
    booked = set(room.booked_nights)
    span = (end - start).days
    return [start + _day(i) for i in range(span) if start + _day(i) not in booked]


def _day(n: int):
    from datetime import timedelta

    return timedelta(days=n)
