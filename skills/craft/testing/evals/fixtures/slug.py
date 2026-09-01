"""Slug generation. See test_slug.py."""

import re
import unicodedata

_SEPARATORS = re.compile(r"[\s_]+")
_UNSAFE = re.compile(r"[^a-z0-9-]")
_RUNS = re.compile(r"-{2,}")


def slugify(text: str, max_length: int = 60) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    ascii_only = normalized.encode("ascii", "ignore").decode("ascii")
    lowered = _SEPARATORS.sub("-", ascii_only.strip().lower())
    safe = _UNSAFE.sub("", lowered)
    collapsed = _RUNS.sub("-", safe).strip("-")
    if len(collapsed) <= max_length:
        return collapsed
    cut = collapsed[:max_length].rsplit("-", 1)[0]
    return cut or collapsed[:max_length]
