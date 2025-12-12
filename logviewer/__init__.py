from .reader import read_lines
from .searcher import search_lines
from .formatters.text import format_text
from .formatters.json_fmt import format_json
from .formatters.pretty import format_pretty

__all__ = [
    "read_lines",
    "search_lines",
    "format_text",
    "format_json",
    "format_pretty",
]


def search_logs(path, keyword, context=0, fmt="text"):
    lines = read_lines(path)
    matches, summary = search_lines(lines, keyword, context=context)
    if fmt == "text":
        return format_text(matches, summary)
    elif fmt == "json":
        return format_json(matches, summary)
    elif fmt == "pretty":
        return format_pretty(matches, summary)
    else:
        raise ValueError("Unknown format: %r" % fmt)
