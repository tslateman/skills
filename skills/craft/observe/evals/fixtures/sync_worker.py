"""Pulls reservations from three PMS vendors on a five minute cycle."""

import logging
import time

from .dlq import dead_letter
from .vendors import CorvusClient, NorthwindClient, OpalClient

log = logging.getLogger(__name__)

CLIENTS = {"corvus": CorvusClient, "northwind": NorthwindClient, "opal": OpalClient}
CYCLE_SECONDS = 300


def run_forever(hotel_ids: list[str]) -> None:
    while True:
        started = time.monotonic()
        for vendor, client_cls in CLIENTS.items():
            client = client_cls()
            for hotel_id in hotel_ids:
                try:
                    sync_hotel(client, vendor, hotel_id)
                except Exception:
                    log.exception("sync failed")
        elapsed = time.monotonic() - started
        time.sleep(max(0, CYCLE_SECONDS - elapsed))


def sync_hotel(client, vendor: str, hotel_id: str) -> None:
    reservations = None
    for attempt in range(4):
        try:
            reservations = client.fetch_reservations(hotel_id)
            break
        except TimeoutError:
            time.sleep(2**attempt)
    if reservations is None:
        dead_letter(vendor=vendor, hotel_id=hotel_id, reason="fetch timed out")
        return

    for res in reservations:
        try:
            upsert(res)
        except ValueError:
            dead_letter(vendor=vendor, hotel_id=hotel_id, reason="bad payload")


def upsert(res: dict) -> None:
    from .db import session

    with session() as s:
        s.merge(res)
