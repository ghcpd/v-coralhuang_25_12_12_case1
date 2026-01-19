"""Log file reader module."""

import datetime


class LogReader:
    """Reads and parses log files or raw log data."""
    
    @staticmethod
    def read_file(filepath):
        """Read log file and return list of lines."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.readlines()
        except Exception as e:
            raise RuntimeError(f"Failed to read file {filepath}: {e}")
    
    @staticmethod
    def parse_timestamp(ts_str):
        """Try to parse a timestamp string, return None if fails."""
        if not ts_str:
            return None
        
        formats = [
            "%Y-%m-%dT%H:%M:%S",
            "%Y-%m-%d %H:%M:%S",
            "%Y-%m-%d",
        ]
        
        for fmt in formats:
            try:
                return datetime.datetime.strptime(ts_str.strip(), fmt)
            except ValueError:
                continue
        
        return None
