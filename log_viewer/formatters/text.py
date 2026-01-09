from typing import List
from ..searcher import Match


HIGHLIGHT_START = "<<"
HIGHLIGHT_END = ">>"


def _highlight(text: str, keyword: str) -> str:
    return text.replace(keyword, HIGHLIGHT_START + keyword + HIGHLIGHT_END)


def format_text(matches: List[Match], summary: dict) -> str:
    out = []
    out.append("LOG SEARCH REPORT")
    out.append("=================")
    out.append(f"Matches: {summary['matches']}")
    out.append(f"Total lines scanned: {summary['total_lines']}")
    if summary.get("earliest_ts") and summary.get("latest_ts"):
        out.append(f"Time range: {summary['earliest_ts']} -> {summary['latest_ts']}")
    out.append("")

    out.append("RESULTS:")
    for m in matches:
        out.append(f"- Line {m.line_no}: {m.text}")
        if m.context_before:
            for ln, txt in m.context_before:
                out.append(f"    {ln}: {txt}")
        if m.context_after:
            for ln, txt in m.context_after:
                out.append(f"    {ln}: {txt}")
        out.append("")

    return "\n".join(out)
