import json
from typing import List


def format_json(matches: List[dict], total_lines: int = None) -> str:
    # Convert datetime objects to isoformat if present
    results = []
    ts_list = []
    for m in matches:
        ts = m.get("timestamp")
        if ts is not None:
            ts_list.append(ts)
            ts_out = ts.isoformat()
        else:
            ts_out = None
        results.append(
            {
                "line_number": m["line_number"],
                "line": m["line"],
                "timestamp": ts_out,
                "context": [{"line_number": ln, "line": txt} for ln, txt in m.get("context", [])],
            }
        )

    summary = {
        "matches": len(results),
    }
    if total_lines is not None:
        summary["total_lines_scanned"] = total_lines
    if ts_list:
        summary["earliest"] = min(ts_list).isoformat()
        summary["latest"] = max(ts_list).isoformat()
    else:
        summary["earliest"] = None
        summary["latest"] = None

    out = {"summary": summary, "results": results}
    return json.dumps(out, indent=2)
