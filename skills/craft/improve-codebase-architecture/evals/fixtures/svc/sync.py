from . import corvus_client, northwind_client, opal_client
from .reservation_manager import ReservationManager

VENDORS = {
    "corvus": corvus_client,
    "northwind": northwind_client,
    "opal": opal_client,
}


def sync_all(hotel_ids):
    manager = ReservationManager()
    total = 0
    for name, client in VENDORS.items():
        for hotel_id in hotel_ids:
            try:
                for res in client.fetch_reservations(hotel_id):
                    manager.save(res)
                    total += 1
            except (PermissionError, ConnectionError):
                continue
    return total
