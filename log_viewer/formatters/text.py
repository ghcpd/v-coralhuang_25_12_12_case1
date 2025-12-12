"""Plain text formatter for structured search results."""
from typing import Any, Dict


HIGHLIGHT_MARKER = ("<<", ">>")


def _highlight(line: str, keyword: str) -> str:
    # Simple case-insensitive highlight replacement using marker
    start, end = HIGHLIGHT_MARKER
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
        parts.append(start + line[j : j + len(kw)] + end)
        i = j + len(kw)
    return "".join(parts)


def format_text(result: Dict[str, Any], context: int = 0) -> str:
    """Return a plain structured text report.

    Highlights keyword with <<keyword>> markers. Includes line numbers
    and configurable context lines (already present in result structure).
    """
    keyword = result.get("keyword", "")
    lines = []
    lines.append("LOG VIEWER REPORT")
    lines.append("=================")
    lines.append(f"Matches: {result.get('matches_count', 0)}")
    lines.append(f"Total lines: {result.get('total_lines', 0)}")
    et = result.get("earliest_timestamp")
    lt = result.get("latest_timestamp")
    if et and lt:
        lines.append(f"Time range: {et} -> {lt}")
    elif et:
        lines.append(f"Time range: from {et}")
    else:
        lines.append("Time range: UNKNOWN")

    lines.append("")
    lines.append("RESULTS")
    lines.append("-------")

    for m in result.get("matches", []):
        ln = m["line_number"]
        # context before
        for cb in m.get("context_before", []):
            lines.append(f"  [{cb['line_number']}] {cb['line']}")
        # main line with highlight
        hl = _highlight(m["line"], keyword) if keyword else m["line"]
        # include timestamp when available. Avoid duplicating if the
        # original line already starts with the same timestamp string.
        ts = m.get("timestamp")
        if ts:
            if m["line"].startswith(ts):
                lines.append(f"[{ln}] {hl}")
            else:
                lines.append(f"[{ln}] {ts} {hl}")
        else:
            lines.append(f"[{ln}] {hl}")
        # context after
        for ca in m.get("context_after", []):
            lines.append(f"  [{ca['line_number']}] {ca['line']}")
        lines.append("")

    return "\n".join(lines)
