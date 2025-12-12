"""Reader utilities for log_viewer

Responsibilities:
- reading files into lines
"""
from typing import List


def read_lines(path: str) -> List[str]:
    """Read a file and return a list of lines (without trailing newlines)."""
    with open(path, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]
