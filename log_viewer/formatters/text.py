from typing import List
import datetime


def highlight_keyword(line: str, keyword: str) -> str:
    # Simple case-insensitive highlight by surrounding with **
    lower = line.lower()
    k = keyword.lower()
    start = 0
    out = ""
    while True:
        idx = lower.find(k, start)
        if idx == -1:
            out += line[start:]
            break
        out += line[start:idx] + "**" + line[idx:idx+len(k)] + "**"
        start = idx + len(k)
    return out


def format_text(matches: List[dict], keyword: str, total_lines: int) -> str:
    header = "LOG SEARCH RESULTS\n"
    header += "==================\n"
    header += f"Matches: {len(matches)}\n"
    header += f"Total lines scanned: {total_lines}\n"

    # compute earliest/latest timestamps if any
    ts_list = [m.get("timestamp") for m in matches if m.get("timestamp")]
    if ts_list:
        earliest = min(ts_list)
        latest = max(ts_list)
        header += f"Earliest: {earliest.isoformat()}\n"
        header += f"Latest: {latest.isoformat()}\n"
    else:
        header += "Earliest: UNKNOWN\n"
        header += "Latest: UNKNOWN\n"

    header += "\n"
    body = ""
    for m in matches:
        body += f"Line {m['line_number']}: "
        body += highlight_keyword(m['line'], keyword) + "\n"
        if m.get("context"):
            for ln, txt in m["context"]:
                if ln != m["line_number"]:
                    body += f"  {ln}: {txt}\n"
    return header + body
