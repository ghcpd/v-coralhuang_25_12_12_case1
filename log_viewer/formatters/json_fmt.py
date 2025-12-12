import json
from typing import List
from ..searcher import Match


def format_json(matches: List[Match], summary: dict) -> str:
    payload = {
        "summary": summary,
        "results": [
            {
                "line": m.line_no,
                "text": m.text,
                "ts": m.ts,
                "context_before": m.context_before,
                "context_after": m.context_after,
            }
            for m in matches
        ],
    }
    return json.dumps(payload, indent=2)
