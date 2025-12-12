# Log Viewer Enhancement

## Original Limitations

The original `log_viewer.py` (renamed to `log_viewer_original.py`) implements a simple `search_logs` function that returns a list of raw matching lines. It lacks structure, summary information, and extensibility. Output is unstructured text only, with no line numbers, context, or metadata.

## Enhancement Approach

The enhanced version modularizes the code into separate components:
- `reader.py`: Handles file reading and line numbering
- `searcher.py`: Performs keyword search with context and summary generation
- `formatters/`: Multiple output formatters (text, JSON, pretty console)

This allows easy addition of new formats or features without coupling.

## Architecture Overview

```
log_viewer/
├── __init__.py
├── reader.py          # LogReader class
├── searcher.py        # LogSearcher class
└── formatters/
    ├── text.py        # TextFormatter class
    ├── json_fmt.py    # JsonFormatter class
    └── pretty.py      # PrettyFormatter class
```

Main entry point: `log_viewer.py` with `search_logs_enhanced` function.

## How to Run Tests

Execute `python run_tests.py` to run all tests using unittest.

## Environment Assumptions

- Python 3.6+ (for f-strings and pathlib)
- Standard library only (json, re, datetime, os)
- UTF-8 encoded log files
- Timestamps in ISO format (YYYY-MM-DDTHH:MM:SS)