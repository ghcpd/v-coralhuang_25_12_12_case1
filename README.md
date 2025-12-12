Log Viewer — Enhanced
=====================

Overview
--------

This repository contains a small enhanced log viewer implemented with a
modular architecture. The original primitive tool (legacy behavior) is
provided as log_viewer_original.py for comparison.

Original limitations
--------------------
- Returned raw matching lines only (no structure)
- No context lines, no highlighting, no summary metadata
- No easy way to extend output formats

Enhancements
------------
- Structured search results with line numbers, context, and timestamps
- Multiple output formats: plain text, JSON, and pretty (ANSI colored)
- Modular architecture: reader, searcher, formatters
- Backward-compatible helper search_logs for legacy usage

Architecture
------------

log_viewer/ (package)
  reader.py          # file reading utilities
  searcher.py        # structured search and legacy helper
  formatters/        # output formatters
    text.py          # plain structured text output
    json_fmt.py      # JSON output
    pretty.py        # ANSI colored pretty output

Legacy/compat
-------------
log_viewer_original.py  # primitive search_logs(path, keyword) CLI

Sample data and demos
---------------------
sample_logs.log         # sample log file used in demos and tests
run_enhanced.py         # demo: shows original and enhanced outputs

Running tests
-------------

This project uses only Python standard library and is compatible with
pytest if available. To run the test suite:

    python run_tests.py

This will discover tests in the tests/ directory and run them, exiting
with a non-zero code if any test fails.

Environment
-----------
- Python 3.8+
- No external dependencies required
