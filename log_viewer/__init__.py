from .reader import LogReader
from .searcher import LogSearcher
from .formatters.text import TextFormatter
from .formatters.json_fmt import JsonFormatter
from .formatters.pretty import PrettyFormatter

def search_logs_enhanced(path, keyword, format='text', context_lines=2):
    reader = LogReader()
    lines = reader.read_lines(path)
    searcher = LogSearcher(context_lines)
    matches = searcher.search(lines, keyword)
    summary = searcher.get_summary(lines, matches)
    if format == 'text':
        formatter = TextFormatter()
        return formatter.format(matches, summary, keyword)
    elif format == 'json':
        formatter = JsonFormatter()
        return formatter.format(matches, summary)
    elif format == 'pretty':
        formatter = PrettyFormatter()
        return formatter.format(matches, summary, keyword)
    else:
        raise ValueError("Invalid format")