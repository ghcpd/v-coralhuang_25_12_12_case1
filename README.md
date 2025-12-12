Log Viewer Enhancement

Original limitations:
- The original tool printed raw matching lines with no structure, no context, and no summary.
- It was not modular or extensible.

Enhancement approach:
- Implemented a small modular package (logviewer/) that separates reading, searching, and formatting.
- Added multiple output formats: plain structured text, JSON, and pretty (ANSI) output.
- Added summary information: number of matches, total lines scanned, earliest/latest timestamps when parsable.
- Preserved original behavior in log_viewer_original.py for semantics comparison.

Architecture:
- logviewer/
  - reader.py: reads lines and extracts timestamps
  - searcher.py: finds matches and collects context and summary
  - formatters/
    - text.py: plain structured text output with simple highlight markers
    - json_fmt.py: JSON output (includes raw and highlighted text)
    - pretty.py: ANSI-colored output for terminals

How to run the demo:
- python demo.py

How to run tests:
- python run_tests.py

Requirements:
- Python 3.8+
- pytest (for running the test suite)

Notes:
- The JSON output is stable and machine-readable; text output is designed to be easy to read and parse.
- The code uses only the Python standard library except for pytest used in tests.
