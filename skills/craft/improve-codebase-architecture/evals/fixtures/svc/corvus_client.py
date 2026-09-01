from . import http_client
from .config import CORVUS_KEY, CORVUS_URL


def fetch_reservations(hotel_id):
    r = http_client.get(
        f"{CORVUS_URL}/hotels/{hotel_id}/reservations",
        headers={"Authorization": f"Bearer {CORVUS_KEY}"},
    )
    if r.status_code == 401:
        raise PermissionError("corvus auth failed")
    if r.status_code >= 500:
        raise ConnectionError("corvus unavailable")
    body = r.json()
    out = []
    for item in body["data"]:
        out.append(
            {
                "id": item["reservationId"],
                "room": item["roomCode"],
                "in": item["arrival"],
                "out": item["departure"],
                "status": item["state"].lower(),
            }
        )
    return out
