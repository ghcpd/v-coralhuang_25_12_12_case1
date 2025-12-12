"""log_viewer package - public API

This package exposes a small, well-factored API for reading and searching
log files and for formatting results in multiple output modes.
"""
from .searcher import search_logs, search

__all__ = ["search_logs", "search"]
