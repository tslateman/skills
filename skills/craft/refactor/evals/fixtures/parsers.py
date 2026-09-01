"""Two parsers that look like duplicates. They are not."""


def parse_room_code(raw: str) -> str:
    """Guest-facing input. Tolerant: trims, upper-cases, drops inner spaces."""
    cleaned = raw.strip().upper().replace(" ", "")
    if not cleaned:
        raise ValueError("empty room code")
    return cleaned


def parse_vendor_room_code(raw: str) -> str:
    """Vendor feed input. Strict: the feed contract says no surrounding space."""
    cleaned = raw.upper().replace(" ", "")
    if not cleaned:
        raise ValueError("empty room code")
    return cleaned
