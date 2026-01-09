from typing import List, Tuple, Dict, Any
from dataclasses import dataclass

@dataclass
class Match:
    line_no: int
    text: str
    ts: str | None
    context_before: list
    context_after: list


def search_lines(lines: List, keyword: str, context: int = 0) -> Tuple[List[Match], Dict[str, Any]]:
    matches: List[Match] = []
    total = len(lines)
    earliest = None
    latest = None

    for i, line in enumerate(lines):
        if keyword in line.text:
            before = []
            after = []
            for j in range(max(0, i - context), i):
                l = lines[j]
                before.append((l.number, l.text))
            for j in range(i + 1, min(total, i + 1 + context)):
                l = lines[j]
                after.append((l.number, l.text))
            highlighted = line.text.replace(keyword, "<<" + keyword + ">>")
            match = Match(line_no=line.number, text=highlighted, ts=line.ts, context_before=before, context_after=after)
            setattr(match, "raw_text", line.text)
            matches.append(match)
        if line.ts:
            if earliest is None or line.ts < earliest:
                earliest = line.ts
            if latest is None or line.ts > latest:
                latest = line.ts

    summary = {
        "matches": len(matches),
        "total_lines": total,
        "earliest_ts": earliest,
        "latest_ts": latest,
    }
    return matches, summary
