"""Test cases for text output formatting."""

import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from log_viewer.searcher import SearchResult
from log_viewer.formatters.text import TextFormatter


class TestTextOutput(unittest.TestCase):
    """Test text formatter output structure."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.formatter = TextFormatter()
        
        # Create sample results
        self.result1 = SearchResult(
            line_number=5,
            line_content="2025-03-01T10:23:10 DEBUG [u1] Alice viewed page /home\n",
            keyword="Alice",
            context_before=["2025-03-01T10:22:00 INFO [u2] Bob logged in from 5.6.7.8\n"],
            context_after=["2025-03-01T10:24:15 INFO [u1] Alice accessed API /users\n"]
        )
        
        self.result2 = SearchResult(
            line_number=15,
            line_content="2025-03-01T10:32:45 INFO [u1] Alice downloaded report\n",
            keyword="Alice"
        )
    
    def test_text_output_contains_headers(self):
        """Test that text output contains required section headers."""
        output = self.formatter.format(
            [self.result1, self.result2],
            total_lines_scanned=20
        )
        
        self.assertIn("SEARCH RESULTS", output)
        self.assertIn("SUMMARY", output)
        self.assertIn("RESULTS", output)
    
    def test_text_output_contains_match_count(self):
        """Test that summary shows number of matches."""
        output = self.formatter.format(
            [self.result1, self.result2],
            total_lines_scanned=20
        )
        
        self.assertIn("Total Matches: 2", output)
    
    def test_text_output_contains_lines_scanned(self):
        """Test that summary shows total lines scanned."""
        output = self.formatter.format(
            [self.result1],
            total_lines_scanned=100
        )
        
        self.assertIn("Total Lines Scanned: 100", output)
    
    def test_text_output_contains_line_numbers(self):
        """Test that results include line numbers."""
        output = self.formatter.format(
            [self.result1, self.result2],
            total_lines_scanned=20
        )
        
        self.assertIn("Line 5:", output)
        self.assertIn("Line 15:", output)
    
    def test_text_output_contains_keyword(self):
        """Test that results show the keyword."""
        output = self.formatter.format(
            [self.result1],
            total_lines_scanned=20
        )
        
        self.assertIn("Keyword: 'Alice'", output)
    
    def test_text_output_includes_context_when_enabled(self):
        """Test that context is included when requested."""
        output = self.formatter.format(
            [self.result1],
            total_lines_scanned=20,
            include_context=True
        )
        
        self.assertIn("Context (before):", output)
        self.assertIn("Context (after):", output)
    
    def test_text_output_no_context_when_disabled(self):
        """Test that context is not included when not requested."""
        output = self.formatter.format(
            [self.result1],
            total_lines_scanned=20,
            include_context=False
        )
        
        # Should not have context markers
        self.assertNotIn("Context (before):", output)
        self.assertNotIn("Context (after):", output)
    
    def test_text_output_no_matches(self):
        """Test formatting when there are no matches."""
        output = self.formatter.format(
            [],
            total_lines_scanned=20
        )
        
        self.assertIn("Total Matches: 0", output)
        self.assertIn("No matches found", output)
    
    def test_text_output_timestamp_range(self):
        """Test that timestamp range is included in summary."""
        import datetime
        
        earliest = datetime.datetime(2025, 3, 1, 10, 0, 0)
        latest = datetime.datetime(2025, 3, 1, 10, 30, 0)
        
        output = self.formatter.format(
            [self.result1],
            total_lines_scanned=20,
            earliest_ts=earliest,
            latest_ts=latest
        )
        
        self.assertIn("Time Range:", output)
        self.assertIn("2025-03-01 10:00:00", output)
        self.assertIn("2025-03-01 10:30:00", output)


if __name__ == '__main__':
    unittest.main()
