from . import http_client
from .config import NORTHWIND_KEY, NORTHWIND_URL


def fetch_reservations(hotel_id):
    r = http_client.get(
        f"{NORTHWIND_URL}/property/{hotel_id}/bookings",
        headers={"X-Api-Key": NORTHWIND_KEY},
    )
    if r.status_code == 401:
        raise PermissionError("northwind auth failed")
    if r.status_code >= 500:
        raise ConnectionError("northwind unavailable")
    body = r.json()
    out = []
    for item in body["bookings"]:
        out.append(
            {
                "id": item["bookingRef"],
                "room": item["unit"],
                "in": item["checkIn"],
                "out": item["checkOut"],
                "status": item["bookingStatus"].lower(),
            }
        )
    return out
