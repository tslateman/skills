"""No tests exist for this module."""

import requests

from .db import connect


class PmsSyncJob:
    def __init__(self, hotel_id: str, vendor_url: str, api_key: str) -> None:
        self.hotel_id = hotel_id
        self.conn = connect()
        self.session = requests.Session()
        self.session.headers["Authorization"] = f"Bearer {api_key}"
        self.vendor_url = vendor_url
        self.cursor = self.conn.execute(
            "select last_sync from sync_state where hotel_id = ?", (hotel_id,)
        ).fetchone()

    def run(self) -> int:
        page, written = 0, 0
        while True:
            resp = self.session.get(
                f"{self.vendor_url}/reservations",
                params={"since": self.cursor, "page": page},
                timeout=30,
            )
            if resp.status_code == 429:
                continue
            body = resp.json()
            for row in body["items"]:
                self.conn.execute("insert or replace into reservation values (?)", (row,))
                written += 1
            if not body.get("next"):
                break
            page += 1
        self.conn.commit()
        return written
