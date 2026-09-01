"""Compatibility shim: maps retired three-letter codes to current ISO codes.

Added when the payment provider migrated in 2023. Still on the hot path for
every historical invoice reprint, because rows written before the migration
carry the retired codes and are never backfilled.
"""

RETIRED = {
    "DEM": "EUR",
    "FRF": "EUR",
    "ITL": "EUR",
    "ESP": "EUR",
}


def normalize(code: str) -> str:
    return RETIRED.get(code, code)


def is_retired(code: str) -> bool:
    return code in RETIRED
