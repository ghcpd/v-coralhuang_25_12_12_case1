"""Plain text structured formatter."""


class TextFormatter:
    """Formats search results as structured plain text."""
    
    @staticmethod
    def format(results, total_lines_scanned, earliest_ts=None, latest_ts=None, 
               include_context=False):
        """
        Format results as structured plain text.
        
        Args:
            results: List of SearchResult objects
            total_lines_scanned: Total number of lines scanned
            earliest_ts: Earliest timestamp in logs
            latest_ts: Latest timestamp in logs
            include_context: Whether to include context lines
            
        Returns:
            Formatted string
        """
        output = []
        output.append("=" * 70)
        output.append("SEARCH RESULTS")
        output.append("=" * 70)
        output.append("")
        
        # Summary section
        output.append("SUMMARY")
        output.append("-" * 70)
        output.append(f"Total Matches: {len(results)}")
        output.append(f"Total Lines Scanned: {total_lines_scanned}")
        
        if earliest_ts and latest_ts:
            output.append(f"Time Range: {earliest_ts} to {latest_ts}")
        elif earliest_ts:
            output.append(f"Time Range: from {earliest_ts}")
        else:
            output.append("Time Range: UNKNOWN")
        
        output.append("")
        
        # Results section
        if results:
            output.append("RESULTS")
            output.append("-" * 70)
            
            for i, result in enumerate(results, 1):
                output.append(f"\nMatch #{i}")
                output.append(f"Line {result.line_number}: {result.line_content}")
                output.append(f"Keyword: '{result.keyword}'")
                
                if include_context:
                    if result.context_before:
                        output.append("Context (before):")
                        for ctx_line in result.context_before:
                            output.append(f"  > {ctx_line.rstrip()}")
                    
                    if result.context_after:
                        output.append("Context (after):")
                        for ctx_line in result.context_after:
                            output.append(f"  > {ctx_line.rstrip()}")
            
            output.append("")
        else:
            output.append("No matches found.")
            output.append("")
        
        output.append("=" * 70)
        
        return "\n".join(output)
