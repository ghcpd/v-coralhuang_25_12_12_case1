"""Enhanced log viewer implementation using modular architecture."""

from log_viewer.reader import LogReader
from log_viewer.searcher import LogSearcher
from log_viewer.formatters.text import TextFormatter
from log_viewer.formatters.json_fmt import JSONFormatter
from log_viewer.formatters.pretty import PrettyFormatter


def search_logs(path, keyword, case_sensitive=False, format_type='text', 
                context_lines=0):
    """
    Enhanced search_logs function with multiple output formats.
    
    Args:
        path: Path to log file
        keyword: Keyword to search for
        case_sensitive: Whether search is case-sensitive (default: False)
        format_type: Output format - 'text', 'json', or 'pretty' (default: 'text')
        context_lines: Number of context lines to include (default: 0)
        
    Returns:
        Formatted search results as string
    """
    # Read log file
    reader = LogReader()
    lines = reader.read_file(path)
    
    # Search for keyword
    searcher = LogSearcher()
    results = searcher.search(lines, keyword, case_sensitive=case_sensitive, 
                             context_lines=context_lines)
    
    # Extract timestamp range
    earliest_ts, latest_ts = searcher.extract_timestamps(lines)
    
    # Format results based on requested format
    if format_type == 'json':
        formatter = JSONFormatter()
    elif format_type == 'pretty':
        formatter = PrettyFormatter()
    else:  # default to text
        formatter = TextFormatter()
    
    output = formatter.format(
        results,
        total_lines_scanned=len(lines),
        earliest_ts=earliest_ts,
        latest_ts=latest_ts,
        include_context=(context_lines > 0)
    )
    
    return output


if __name__ == "__main__":
    # Example usage
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: python log_viewer_enhanced.py <log_file> <keyword> [--json|--pretty] [--context N]")
        sys.exit(1)
    
    log_file = sys.argv[1]
    keyword = sys.argv[2]
    format_type = 'text'
    context_lines = 0
    
    for arg in sys.argv[3:]:
        if arg == '--json':
            format_type = 'json'
        elif arg == '--pretty':
            format_type = 'pretty'
        elif arg.startswith('--context'):
            if '=' in arg:
                context_lines = int(arg.split('=')[1])
    
    result = search_logs(log_file, keyword, format_type=format_type, 
                        context_lines=context_lines)
    print(result)
