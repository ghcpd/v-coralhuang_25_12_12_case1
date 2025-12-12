"""Simple original log viewer (primitive implementation).

Provides a single function search_logs(path, keyword) that returns raw
matching lines (as the legacy tool did). This module also acts as a tiny
CLI so we can demonstrate original behavior.
"""
import sys


def search_logs(path, keyword):
    """Return a list of raw lines from file at path that contain keyword.

    Matching is case-insensitive and returns the raw line strings (with\n).
    """
    matches = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                if keyword.lower() in line.lower():
                    matches.append(line.rstrip("\n"))
    except FileNotFoundError:
        raise
    return matches


def _main(argv):
    if len(argv) < 3:
        print("Usage: python log_viewer_original.py <logfile> <keyword>")
        return 2
    path = argv[1]
    keyword = argv[2]
    matches = search_logs(path, keyword)
    # Legacy behavior: print raw lines only
    for m in matches:
        print(m)
    # also print a trailing summary line (not structured)
    print(f"\n{len(matches)} matches")
    return 0


if __name__ == "__main__":
    raise SystemExit(_main(sys.argv))
