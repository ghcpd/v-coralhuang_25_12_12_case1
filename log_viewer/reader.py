import re
from dataclasses import dataclass
from typing import List, Optional

TS_RE = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}")

@dataclass
class Line:
    number: int
    text: str
    ts: Optional[str] = None


def read_lines(path: str) -> List[Line]:
    """Read a file and return list of Line objects with optional timestamp parsed.
    Timestamp is the first ISO-like token found in the line.
    """
    lines = []
    with open(path, "r", encoding="utf-8") as f:
        for i, raw in enumerate(f, start=1):
            txt = raw.rstrip("\n")
            m = TS_RE.search(txt)
            ts = m.group(0) if m else None
            lines.append(Line(number=i, text=txt, ts=ts))
    return lines
