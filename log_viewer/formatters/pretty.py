"""Pretty console formatter with ANSI colors."""


class PrettyFormatter:
    """Formats search results with ANSI colors for console."""
    
    # ANSI color codes
    RESET = '\033[0m'
    BOLD = '\033[1m'
    HIGHLIGHT = '\033[93m'  # Yellow
    MATCH_BG = '\033[102m'  # Bright green background
    SECTION = '\033[94m'    # Blue
    INFO = '\033[96m'       # Cyan
    
    @staticmethod
    def colorize_keyword(line, keyword):
        """Highlight keyword in line with color."""
        import re
        # Case-insensitive replacement with color
        pattern = re.compile(re.escape(keyword), re.IGNORECASE)
        colored = pattern.sub(
            f'{PrettyFormatter.MATCH_BG}{keyword}{PrettyFormatter.RESET}',
            line
        )
        return colored
    
    @staticmethod
    def format(results, total_lines_scanned, earliest_ts=None, latest_ts=None,
               include_context=False):
        """
        Format results as pretty console output with colors.
        
        Args:
            results: List of SearchResult objects
            total_lines_scanned: Total number of lines scanned
            earliest_ts: Earliest timestamp in logs
            latest_ts: Latest timestamp in logs
            include_context: Whether to include context lines
            
        Returns:
            Formatted string with ANSI colors
        """
        output = []
        
        # Header
        output.append(f"\n{PrettyFormatter.SECTION}{'=' * 70}{PrettyFormatter.RESET}")
        output.append(f"{PrettyFormatter.BOLD}{PrettyFormatter.SECTION}SEARCH RESULTS{PrettyFormatter.RESET}")
        output.append(f"{PrettyFormatter.SECTION}{'=' * 70}{PrettyFormatter.RESET}\n")
        
        # Summary
        output.append(f"{PrettyFormatter.INFO}SUMMARY{PrettyFormatter.RESET}")
        output.append(f"{PrettyFormatter.SECTION}{'-' * 70}{PrettyFormatter.RESET}")
        output.append(f"  Total Matches: {PrettyFormatter.HIGHLIGHT}{len(results)}{PrettyFormatter.RESET}")
        output.append(f"  Total Lines Scanned: {PrettyFormatter.HIGHLIGHT}{total_lines_scanned}{PrettyFormatter.RESET}")
        
        if earliest_ts and latest_ts:
            output.append(f"  Time Range: {earliest_ts} to {latest_ts}")
        elif earliest_ts:
            output.append(f"  Time Range: from {earliest_ts}")
        else:
            output.append(f"  Time Range: {PrettyFormatter.HIGHLIGHT}UNKNOWN{PrettyFormatter.RESET}")
        
        output.append("")
        
        # Results
        if results:
            output.append(f"{PrettyFormatter.INFO}RESULTS{PrettyFormatter.RESET}")
            output.append(f"{PrettyFormatter.SECTION}{'-' * 70}{PrettyFormatter.RESET}")
            
            for i, result in enumerate(results, 1):
                output.append(f"\n{PrettyFormatter.BOLD}Match #{i}{PrettyFormatter.RESET}")
                output.append(f"Line {PrettyFormatter.HIGHLIGHT}{result.line_number}{PrettyFormatter.RESET}: "
                            f"{PrettyFormatter.colorize_keyword(result.line_content, result.keyword)}")
                output.append(f"Keyword: {PrettyFormatter.HIGHLIGHT}'{result.keyword}'{PrettyFormatter.RESET}")
                
                if include_context:
                    if result.context_before:
                        output.append("Context (before):")
                        for ctx_line in result.context_before:
                            output.append(f"  {PrettyFormatter.INFO}>{PrettyFormatter.RESET} {ctx_line.rstrip()}")
                    
                    if result.context_after:
                        output.append("Context (after):")
                        for ctx_line in result.context_after:
                            output.append(f"  {PrettyFormatter.INFO}>{PrettyFormatter.RESET} {ctx_line.rstrip()}")
            
            output.append("")
        else:
            output.append(f"{PrettyFormatter.HIGHLIGHT}No matches found.{PrettyFormatter.RESET}\n")
        
        output.append(f"{PrettyFormatter.SECTION}{'=' * 70}{PrettyFormatter.RESET}\n")
        
        return "\n".join(output)
