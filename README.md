# Enhanced Log Viewer

Original limitations:
- The original tool produced unstructured raw lines and lacked metadata (no line numbers, timestamps summary, or context).
- Not extensible: formatting and search were tightly coupled.

Enhancement approach:
- Implemented a modular architecture (reader, searcher, formatters) with multiple output modes: text, JSON, pretty (ANSI).
- Added structured output with line numbers, optional context lines, and highlighted keywords.
- Added summary (matches count, total lines scanned, earliest/latest timestamps when parseable).
- Added a `log_viewer_original.py` as a baseline for comparison.

Architecture overview:
- log_viewer/
  - reader.py: reads file lines and parses timestamps.
  - searcher.py: performs case-insensitive keyword search and returns structured matches; includes backward-compatible `search_logs_raw`.
  - formatters/
    - text.py: plain structured text output with highlights.
    - json_fmt.py: JSON output with `summary` and `results`.
    - pretty.py: ANSI-colored pretty console output.
- log_viewer_cli.py: simple CLI for interactive use.
- run_tests.py: script to run tests.

How to run tests:
- Ensure Python 3.8+ is available.
- Optionally install pytest for nicer output: `pip install pytest`.
- Run tests:

```bash
python run_tests.py
```

Environment assumptions:
- Uses only Python standard library. Pytest is optional.

Files:
- log_viewer_original.py: original behavior (search_logs(path, keyword) -> list of raw lines)
- log_viewer/: Enhanced modular implementation
- sample_logs.txt: sample log file for testing/demonstration
- tests/: test suite

Demonstration:

- Original output (raw lines):

```
2025-03-01T10:21:30 u1 Alice login ip=1.2.3.4
2025-03-01T10:22:00 u2 Bob login ip=5.6.7.8
2025-03-01T10:30:00 u3 Carol login ip=9.9.9.9
no-ts line contains login as word without iso timestamp
```

- Enhanced output (plain text):

```
LOG SEARCH RESULTS
==================
Matches: 4
Total lines scanned: 7
Earliest: 2025-03-01T10:21:30
Latest: 2025-03-01T10:30:00

Line 1: 2025-03-01T10:21:30 u1 Alice **login** ip=1.2.3.4
  2: 2025-03-01T10:22:00 u2 Bob login ip=5.6.7.8
Line 2: 2025-03-01T10:22:00 u2 Bob **login** ip=5.6.7.8
  1: 2025-03-01T10:21:30 u1 Alice login ip=1.2.3.4

... (other results)
```

- Enhanced output (JSON):

```json
{
  "summary": {
    "matches": 4,
    "total_lines_scanned": 7,
    "earliest": "2025-03-01T10:21:30",
    "latest": "2025-03-01T10:30:00"
  },
  "results": [
    {"line_number": 1, "line": "2025-03-01T10:21:30 u1 Alice login ip=1.2.3.4", "timestamp": "2025-03-01T10:21:30", "context": [...]},
    ...
  ]
}
```

Enhanced outputs more readable, include line numbers, context, and structured metadata.

Enhanced outputs: run `python log_viewer_cli.py sample_logs.txt login --mode text|json|pretty`
