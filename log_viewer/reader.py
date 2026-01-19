import datetime
import re


ISO_DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}")


def read_lines(path):
    """Yield (line_number, text) for each non-empty line in the file."""
    with open(path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            yield i, line.rstrip("\n")


def parse_timestamp(text):
    """Attempt to find an ISO timestamp (basic) in the text and parse it.
    Returns a datetime.datetime or None.
    """
    m = ISO_DATE_RE.search(text)
    if not m:
        return None
    ts_str = m.group(0)
    try:
        return datetime.datetime.fromisoformat(ts_str)
    except Exception:
        return None
