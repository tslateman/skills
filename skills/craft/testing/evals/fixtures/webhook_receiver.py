"""Receives reservation events from PMS vendors. No tests yet."""

import hmac
import json
from hashlib import sha256

from .db import session
from .models import InboundEvent, Reservation

VENDOR_SECRETS = {"corvus": b"...", "northwind": b"...", "opal": b"..."}


def receive(vendor: str, raw_body: bytes, signature: str) -> tuple[int, str]:
    secret = VENDOR_SECRETS.get(vendor)
    if secret is None:
        return 404, "unknown vendor"

    expected = hmac.new(secret, raw_body, sha256).hexdigest()
    if not hmac.compare_digest(expected, signature):
        return 401, "bad signature"

    body = json.loads(raw_body)
    event_id = body.get("event_id")
    if not event_id:
        return 400, "missing event_id"

    with session() as s:
        seen = s.get(InboundEvent, (vendor, event_id))
        if seen is not None:
            return 200, "duplicate"
        s.add(InboundEvent(vendor=vendor, event_id=event_id))

        res = s.get(Reservation, body["reservation_id"])
        if res is None:
            res = Reservation(id=body["reservation_id"])
            s.add(res)
        res.status = body["status"]
        res.check_in = body["check_in"]
        res.check_out = body["check_out"]
        s.commit()

    return 202, "accepted"
