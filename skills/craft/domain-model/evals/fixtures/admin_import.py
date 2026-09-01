"""Admin bulk import. Second home of the overlap rule."""

import csv
from datetime import date

from .reservation import Reservation


def import_reservations(path: str, db) -> tuple[int, list[str]]:
    created, errors = 0, []
    with open(path) as fh:
        for line in csv.DictReader(fh):
            room_id = int(line["room_id"])
            check_in = date.fromisoformat(line["check_in"])
            check_out = date.fromisoformat(line["check_out"])

            clash = False
            for row in db.query("select * from reservation where room_id = ?", room_id):
                if check_in <= row["check_out"] and row["check_in"] <= check_out:
                    clash = True
            if clash:
                errors.append(f"row for room {room_id} overlaps an existing stay")
                continue

            res = Reservation(
                id=None,
                room_id=room_id,
                guest_id=int(line["guest_id"]),
                check_in=check_in,
                check_out=check_out,
                status="confirmed",
            )
            res.save(db)
            created += 1
    return created, errors
