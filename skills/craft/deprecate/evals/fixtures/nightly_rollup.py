"""Internal cron. Runs 02:00 UTC, writes the occupancy rollup table."""

from .availability_api import get_availability_v1
from .warehouse import write_rollup


def run(hotel_ids: list[str], start: str, end: str) -> int:
    written = 0
    for hotel_id in hotel_ids:
        payload = get_availability_v1(hotel_id, start, end)
        for room in payload["rooms"]:
            write_rollup(
                hotel_id=hotel_id,
                room=room["room"],
                open_nights=len(room["nights"]),
                rate=room["rate"],
                currency=payload["currency"],
            )
            written += 1
    return written
