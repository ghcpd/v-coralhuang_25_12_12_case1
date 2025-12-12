"""Log search module."""

from .reader import LogReader


class SearchResult:
    """Represents a single search result."""
    
    def __init__(self, line_number, line_content, keyword, context_before=None, context_after=None):
        """
        Initialize a search result.
        
        Args:
            line_number: 1-indexed line number
            line_content: The matched line
            keyword: The keyword that was searched for
            context_before: List of lines before the match
            context_after: List of lines after the match
        """
        self.line_number = line_number
        self.line_content = line_content.rstrip('\n')
        self.keyword = keyword
        self.context_before = context_before or []
        self.context_after = context_after or []


class LogSearcher:
    """Searches logs for keywords."""
    
    @staticmethod
    def search(lines, keyword, case_sensitive=False, context_lines=0):
        """
        Search for keyword in lines.
        
        Args:
            lines: List of log lines
            keyword: Keyword to search for
            case_sensitive: Whether search is case-sensitive
            context_lines: Number of lines to include before/after match
            
        Returns:
            List of SearchResult objects
        """
        results = []
        search_term = keyword if case_sensitive else keyword.lower()
        
        for idx, line in enumerate(lines):
            compare_line = line if case_sensitive else line.lower()
            
            if search_term in compare_line:
                line_number = idx + 1
                
                # Extract context
                context_before = []
                context_after = []
                
                if context_lines > 0:
                    start_context = max(0, idx - context_lines)
                    context_before = lines[start_context:idx]
                    
                    end_context = min(len(lines), idx + context_lines + 1)
                    context_after = lines[idx + 1:end_context]
                
                result = SearchResult(
                    line_number=line_number,
                    line_content=line,
                    keyword=keyword,
                    context_before=context_before,
                    context_after=context_after
                )
                results.append(result)
        
        return results
    
    @staticmethod
    def extract_timestamps(lines):
        """
        Extract timestamps from log lines.
        
        Returns tuple: (earliest_ts, latest_ts)
        """
        reader = LogReader()
        timestamps = []
        
        for line in lines:
            # Try to find ISO format timestamp patterns
            import re
            # Match patterns like: 2025-03-01T10:21:30 or 2025-03-01 10:21:30
            match = re.search(r'\d{4}-\d{2}-\d{2}[T\s]\d{2}:\d{2}:\d{2}', line)
            if match:
                ts_str = match.group(0).replace('T', ' ')
                ts = reader.parse_timestamp(ts_str)
                if ts:
                    timestamps.append(ts)
        
        if timestamps:
            return (min(timestamps), max(timestamps))
        return (None, None)
