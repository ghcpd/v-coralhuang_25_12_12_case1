"""Simple CLI for enhanced log viewer."""
import argparse
from log_viewer.searcher import search_logs
from log_viewer.formatters.text import format_text
from log_viewer.formatters.json_fmt import format_json
from log_viewer.formatters.pretty import format_pretty
from log_viewer.reader import read_lines


def main():
    p = argparse.ArgumentParser()
    p.add_argument("path")
    p.add_argument("keyword")
    p.add_argument("--context", type=int, default=0)
    p.add_argument("--mode", choices=["text", "json", "pretty"], default="text")
    args = p.parse_args()

    matches = search_logs(args.path, args.keyword, context=args.context)
    total = sum(1 for _ in read_lines(args.path))

    if args.mode == "text":
        print(format_text(matches, args.keyword, total))
    elif args.mode == "json":
        print(format_json(matches, total))
    elif args.mode == "pretty":
        print(format_pretty(matches, args.keyword, total))


if __name__ == "__main__":
    main()
