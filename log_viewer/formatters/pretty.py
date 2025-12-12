"""Pretty console formatter with ANSI coloring."""
from typing import Any, Dict


# ANSI codes
_BOLD = "\x1b[1m"
_RESET = "\x1b[0m"
_CYAN = "\x1b[36m"
_YELLOW = "\x1b[33m"
_RED = "\x1b[31m"


def _color(text: str, code: str) -> str:
    return f"{code}{text}{_RESET}"


def _highlight(line: str, keyword: str) -> str:
    low = line.lower()
    kw = keyword.lower()
    parts = []
    i = 0
    while True:
        j = low.find(kw, i)
        if j == -1:
            parts.append(line[i:])
            break
        parts.append(line[i:j])
        parts.append(_color(line[j : j + len(kw)], _RED))
        i = j + len(kw)
    return "".join(parts)


def format_pretty(result: Dict[str, Any], context: int = 0) -> str:
    keyword = result.get("keyword", "")
    lines = []
    header = _color("LOG VIEWER REPORT", _BOLD + _CYAN)
    lines.append(header)
    lines.append(_color("=================", _CYAN))
    lines.append(_color(f"Matches: {result.get('matches_count', 0)}", _YELLOW))
    lines.append(_color(f"Total lines: {result.get('total_lines', 0)}", _YELLOW))
    et = result.get("earliest_timestamp")
    lt = result.get("latest_timestamp")
    if et and lt:
        lines.append(_color(f"Time range: {et} -> {lt}", _YELLOW))
    elif et:
        lines.append(_color(f"Time range: from {et}", _YELLOW))
    else:
        lines.append(_color("Time range: UNKNOWN", _YELLOW))

    lines.append("")
    lines.append(_color("RESULTS", _BOLD + _CYAN))
    lines.append(_color("-------", _CYAN))

    for m in result.get("matches", []):
        ln = m["line_number"]
        for cb in m.get("context_before", []):
            lines.append(f"  [{cb['line_number']}] {cb['line']}")
        if keyword:
            hl = _highlight(m["line"], keyword)
        else:
            hl = m["line"]
        ts = m.get("timestamp")
        if ts:
            # Avoid duplicating the timestamp if it's already present in the
            # original line.
            if m["line"].startswith(ts):
                lines.append(f"[{ln}] " + hl)
            else:
                lines.append(f"[{ln}] " + _color(ts, _CYAN) + " " + hl)
        else:
            lines.append(f"[{ln}] " + hl)
        for ca in m.get("context_after", []):
            lines.append(f"  [{ca['line_number']}] {ca['line']}")
        lines.append("")

    return "\n".join(lines)
