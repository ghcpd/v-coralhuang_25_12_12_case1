"""Search functionality for log_viewer

Exposes a search function that returns structured results including
line numbers, context lines, and parsed timestamps (when available).
"""
from typing import List, Dict, Any, Optional
import re
import datetime

from .reader import read_lines


TIMESTAMP_RE = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}")


def _parse_timestamp_from_line(line: str) -> Optional[datetime.datetime]:
    m = TIMESTAMP_RE.search(line)
    if not m:
        return None
    ts_str = m.group(0)
    try:
        return datetime.datetime.fromisoformat(ts_str)
    except Exception:
        return None


def search_logs(path: str, keyword: str) -> List[str]:
    """Legacy-friendly helper: returns list of raw matching lines.

    This keeps backward compatibility with the original primitive tool.
    """
    lines = read_lines(path)
    matches = [ln for ln in lines if keyword.lower() in ln.lower()]
    return matches


def search(path: str, keyword: str, context: int = 0) -> Dict[str, Any]:
    """Search the file at path for keyword and return structured results.

    Returned structure:
    {
      "matches": [
         {
           "line_number": int,
           "line": str,
           "timestamp": isoformat or None,
           "context_before": [ {"line_number":int, "line":str}, ...],
           "context_after": [ ... ]
         }, ...
      ],
      "total_lines": int,
      "matches_count": int,
      "earliest_timestamp": iso or None,
      "latest_timestamp": iso or None,
      "keyword": keyword,
    }
    """
    lines = read_lines(path)
    total_lines = len(lines)
    matches = []
    earliest = None
    latest = None

    for idx, line in enumerate(lines, start=1):
        if keyword.lower() in line.lower():
            ts = _parse_timestamp_from_line(line)
            if ts is not None:
                if earliest is None or ts < earliest:
                    earliest = ts
                if latest is None or ts > latest:
                    latest = ts

            before = []
            after = []
            # collect context lines
            for i in range(max(1, idx - context), idx):
                before.append({"line_number": i, "line": lines[i - 1]})
            for i in range(idx + 1, min(total_lines + 1, idx + context + 1)):
                after.append({"line_number": i, "line": lines[i - 1]})

            matches.append(
                {
                    "line_number": idx,
                    "line": line,
                    "timestamp": ts.isoformat() if ts is not None else None,
                    "context_before": before,
                    "context_after": after,
                }
            )

    return {
        "matches": matches,
        "total_lines": total_lines,
        "matches_count": len(matches),
        "earliest_timestamp": earliest.isoformat() if earliest else None,
        "latest_timestamp": latest.isoformat() if latest else None,
        "keyword": keyword,
    }
