from typing import List
from ..searcher import Match

CSI = "\x1b["
RESET = CSI + "0m"
RED = CSI + "31m"
BOLD = CSI + "1m"


def format_pretty(matches: List[Match], summary: dict) -> str:
    out = []
    out.append(BOLD + "LOG SEARCH REPORT" + RESET)
    out.append("=================")
    out.append(f"Matches: {summary['matches']}")
    out.append(f"Total lines scanned: {summary['total_lines']}")
    if summary.get("earliest_ts") and summary.get("latest_ts"):
        out.append(f"Time range: {summary['earliest_ts']} -> {summary['latest_ts']}")
    out.append("")

    out.append("RESULTS:")
    for m in matches:
        colored = m.text.replace("<<", BOLD + RED).replace(">>", RESET)
        out.append(f"- Line {m.line_no}: {colored}")
        if m.context_before:
            for ln, txt in m.context_before:
                out.append(f"    {ln}: {txt}")
        if m.context_after:
            for ln, txt in m.context_after:
                out.append(f"    {ln}: {txt}")
        out.append("")

    return "\n".join(out)
