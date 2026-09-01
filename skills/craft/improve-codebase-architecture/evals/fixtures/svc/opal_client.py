from . import http_client
from .config import OPAL_KEY, OPAL_URL


def fetch_reservations(hotel_id):
    r = http_client.get(
        f"{OPAL_URL}/v3/{hotel_id}/stays",
        headers={"Authorization": f"Token {OPAL_KEY}"},
    )
    if r.status_code == 401:
        raise PermissionError("opal auth failed")
    if r.status_code >= 500:
        raise ConnectionError("opal unavailable")
    body = r.json()
    out = []
    for item in body["stays"]:
        out.append(
            {
                "id": item["stayId"],
                "room": item["roomNumber"],
                "in": item["startDate"],
                "out": item["endDate"],
                "status": item["stayState"].lower(),
            }
        )
    return out
