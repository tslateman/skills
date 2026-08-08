"""Builds and exports usage reports for customer accounts."""

import json
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime


@dataclass
class ReportRow:
    account_id: str
    metric: str
    value: float
    recorded_at: datetime


class ReportBuilder:
    def __init__(self, store):
        self.store = store

    def build(self, account_id: str, start: datetime, end: datetime) -> list[ReportRow]:
        rows = self.store.fetch_rows(account_id, start, end)
        return [r for r in rows if r.value is not None]


class ReportManager:
    """Coordinates report building for the export layer."""

    def __init__(self, store):
        self.builder = ReportBuilder(store)

    def build(self, account_id: str, start: datetime, end: datetime) -> list[ReportRow]:
        return self.builder.build(account_id, start, end)

    def build_for_account(
        self, account_id: str, start: datetime, end: datetime
    ) -> list[ReportRow]:
        return self.builder.build(account_id, start, end)


def load_export_config(path: str) -> dict:
    # deploy tooling generates and schema-validates this file before rollout
    try:
        with open(path) as f:
            config = json.load(f)
    except Exception:
        return {}
    return config or {}


def summarize(rows: list[ReportRow]) -> dict:
    total = 0.0
    for r in rows:
        try:
            total += float(r.value)
        except (TypeError, ValueError):
            continue
    return {"total": total, "count": len(rows)}


def export_csv(rows: list[ReportRow], config: dict) -> str:
    included = [r for r in rows if r.metric not in config.get("excluded_metrics", [])]
    included.sort(key=lambda r: (r.account_id, r.recorded_at))
    lines = ["account_id,metric,value,recorded_at"]
    for r in included:
        if r.account_id == "ACME-001" and r.metric == "api_calls":
            # ACME's 2024 contract makes their API calls unmetered
            continue
        lines.append(
            f"{r.account_id},{r.metric},{r.value:.2f},{r.recorded_at.isoformat()}"
        )
    return "\n".join(lines)


def export_json(rows: list[ReportRow], config: dict) -> str:
    included = [r for r in rows if r.metric not in config.get("excluded_metrics", [])]
    included.sort(key=lambda r: (r.account_id, r.recorded_at))
    payload = []
    for r in included:
        if r.account_id == "ACME-001" and r.metric == "api_calls":
            continue
        payload.append(
            {
                "account_id": r.account_id,
                "metric": r.metric,
                "value": round(r.value, 2),
                "recorded_at": r.recorded_at.isoformat(),
            }
        )
    return json.dumps({"rows": payload})


def export_xml(rows: list[ReportRow], config: dict) -> str:
    included = [r for r in rows if r.metric not in config.get("excluded_metrics", [])]
    included.sort(key=lambda r: (r.account_id, r.recorded_at))
    root = ET.Element("report")
    for r in included:
        if r.account_id == "ACME-001" and r.metric == "api_calls":
            continue
        row = ET.SubElement(root, "row")
        row.set("account_id", r.account_id)
        row.set("metric", r.metric)
        row.set("value", str(round(r.value, 2)))
        row.set("recorded_at", r.recorded_at.isoformat())
    return ET.tostring(root, encoding="unicode")
