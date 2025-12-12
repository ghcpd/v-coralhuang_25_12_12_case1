from .reader import read_lines, parse_timestamp


def search_logs(path, keyword, context=0):
    """Search lines in a file for keyword and return list of matches.

    Returns list of dicts: {
        "line_number": int,
        "line": str,
        "context": list of (line_number, text),
        "timestamp": datetime or None
    }
    """
    matches = []
    # Read all lines into memory for easy context extraction (acceptable for test)
    lines = list(read_lines(path))
    for i, (ln, text) in enumerate(lines):
        if keyword.lower() in text.lower():
            ctx_start = max(0, i - context)
            ctx_end = min(len(lines), i + 1 + context)
            ctx = lines[ctx_start:ctx_end]
            matches.append(
                {
                    "line_number": ln,
                    "line": text,
                    "context": ctx,
                    "timestamp": parse_timestamp(text),
                }
            )
    return matches


# Provide compatibility wrapper as original simple function

def search_logs_raw(path, keyword):
    """Backward compatible simple function returning raw lines only"""
    return [line for _, line in read_lines(path) if keyword.lower() in line.lower()]
