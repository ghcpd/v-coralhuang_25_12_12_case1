"""Demo runner to show original vs enhanced output modes."""
import sys
import json

from log_viewer_original import search_logs as original_search
from log_viewer.searcher import search
from log_viewer.formatters.text import format_text
from log_viewer.formatters.json_fmt import format_json
from log_viewer.formatters.pretty import format_pretty


def demo(path: str, keyword: str):
    print("--- ORIGINAL TOOL OUTPUT (raw lines) ---")
    orig = original_search(path, keyword)
    for l in orig:
        print(l)
    print(f"\n{len(orig)} matches\n")

    print("--- ENHANCED TOOL OUTPUT (text mode) ---")
    structured = search(path, keyword, context=1)
    print(format_text(structured, context=1))

    print("--- ENHANCED TOOL OUTPUT (JSON mode) ---")
    print(format_json(structured))

    print("--- ENHANCED TOOL OUTPUT (pretty mode) ---")
    print(format_pretty(structured, context=1))


def _main(argv):
    if len(argv) < 3:
        print("Usage: python run_enhanced.py <logfile> <keyword>")
        return 2
    demo(argv[1], argv[2])
    return 0


if __name__ == "__main__":
    raise SystemExit(_main(sys.argv))
