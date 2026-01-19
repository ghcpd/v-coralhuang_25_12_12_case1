"""JSON formatter."""

import json


class JSONFormatter:
    """Formats search results as JSON."""
    
    @staticmethod
    def format(results, total_lines_scanned, earliest_ts=None, latest_ts=None,
               include_context=False):
        """
        Format results as JSON.
        
        Args:
            results: List of SearchResult objects
            total_lines_scanned: Total number of lines scanned
            earliest_ts: Earliest timestamp in logs
            latest_ts: Latest timestamp in logs
            include_context: Whether to include context lines
            
        Returns:
            JSON string
        """
        output_dict = {
            "summary": {
                "total_matches": len(results),
                "total_lines_scanned": total_lines_scanned,
                "time_range": {
                    "earliest": earliest_ts.isoformat() if earliest_ts else None,
                    "latest": latest_ts.isoformat() if latest_ts else None
                }
            },
            "results": []
        }
        
        for result in results:
            result_dict = {
                "line_number": result.line_number,
                "line_content": result.line_content,
                "keyword": result.keyword
            }
            
            if include_context:
                result_dict["context_before"] = [
                    ctx.rstrip() for ctx in result.context_before
                ]
                result_dict["context_after"] = [
                    ctx.rstrip() for ctx in result.context_after
                ]
            
            output_dict["results"].append(result_dict)
        
        return json.dumps(output_dict, indent=2)
