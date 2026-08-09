"""URL slug generation for article titles."""

import re
import unicodedata

MAX_LENGTH = 60


def slugify(title: str) -> str:
    """Return a URL-safe slug of at most MAX_LENGTH characters.

    Accents are transliterated, runs of non-alphanumerics collapse to a single
    hyphen, and the result never begins or ends with a hyphen.
    """
    normalized = unicodedata.normalize("NFKD", title)
    ascii_only = normalized.encode("ascii", "ignore").decode("ascii")
    hyphenated = re.sub(r"[^a-z0-9]+", "-", ascii_only.lower())
    trimmed = hyphenated.strip("-")
    if len(trimmed) <= MAX_LENGTH:
        return trimmed
    return trimmed[:MAX_LENGTH].rstrip("-")
