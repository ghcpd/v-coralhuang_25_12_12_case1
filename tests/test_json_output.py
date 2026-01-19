"""Test cases for JSON output formatting."""

import unittest
import json
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from log_viewer.searcher import SearchResult
from log_viewer.formatters.json_fmt import JSONFormatter


class TestJSONOutput(unittest.TestCase):
    """Test JSON formatter output structure."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.formatter = JSONFormatter()
        
        # Create sample results
        self.result1 = SearchResult(
            line_number=5,
            line_content="2025-03-01T10:23:10 DEBUG [u1] Alice viewed page /home\n",
            keyword="Alice"
        )
        
        self.result2 = SearchResult(
            line_number=15,
            line_content="2025-03-01T10:32:45 INFO [u1] Alice downloaded report\n",
            keyword="Alice"
        )
    
    def test_json_output_is_valid_json(self):
        """Test that output is valid JSON."""
        output = self.formatter.format(
            [self.result1, self.result2],
            total_lines_scanned=20
        )
        
        # Should not raise an exception
        data = json.loads(output)
        self.assertIsInstance(data, dict)
    
    def test_json_output_contains_summary(self):
        """Test that JSON includes summary section."""
        output = self.formatter.format(
            [self.result1, self.result2],
            total_lines_scanned=20
        )
        
        data = json.loads(output)
        
        self.assertIn('summary', data)
        self.assertEqual(data['summary']['total_matches'], 2)
        self.assertEqual(data['summary']['total_lines_scanned'], 20)
    
    def test_json_output_contains_results(self):
        """Test that JSON includes results array."""
        output = self.formatter.format(
            [self.result1, self.result2],
            total_lines_scanned=20
        )
        
        data = json.loads(output)
        
        self.assertIn('results', data)
        self.assertIsInstance(data['results'], list)
        self.assertEqual(len(data['results']), 2)
    
    def test_json_result_has_required_fields(self):
        """Test that each result has required metadata."""
        output = self.formatter.format(
            [self.result1],
            total_lines_scanned=20
        )
        
        data = json.loads(output)
        result = data['results'][0]
        
        self.assertIn('line_number', result)
        self.assertIn('line_content', result)
        self.assertIn('keyword', result)
    
    def test_json_result_line_number_correct(self):
        """Test that result line numbers are correct."""
        output = self.formatter.format(
            [self.result1, self.result2],
            total_lines_scanned=20
        )
        
        data = json.loads(output)
        
        self.assertEqual(data['results'][0]['line_number'], 5)
        self.assertEqual(data['results'][1]['line_number'], 15)
    
    def test_json_result_keyword_correct(self):
        """Test that result keywords are correct."""
        output = self.formatter.format(
            [self.result1, self.result2],
            total_lines_scanned=20
        )
        
        data = json.loads(output)
        
        self.assertEqual(data['results'][0]['keyword'], 'Alice')
        self.assertEqual(data['results'][1]['keyword'], 'Alice')
    
    def test_json_includes_timestamps(self):
        """Test that JSON includes timestamp information."""
        import datetime
        
        earliest = datetime.datetime(2025, 3, 1, 10, 0, 0)
        latest = datetime.datetime(2025, 3, 1, 10, 30, 0)
        
        output = self.formatter.format(
            [self.result1],
            total_lines_scanned=20,
            earliest_ts=earliest,
            latest_ts=latest
        )
        
        data = json.loads(output)
        
        self.assertIsNotNone(data['summary']['time_range']['earliest'])
        self.assertIsNotNone(data['summary']['time_range']['latest'])
    
    def test_json_context_not_included_by_default(self):
        """Test that context is not included by default."""
        output = self.formatter.format(
            [self.result1],
            total_lines_scanned=20,
            include_context=False
        )
        
        data = json.loads(output)
        result = data['results'][0]
        
        self.assertNotIn('context_before', result)
        self.assertNotIn('context_after', result)
    
    def test_json_empty_results(self):
        """Test JSON formatting with no matches."""
        output = self.formatter.format(
            [],
            total_lines_scanned=20
        )
        
        data = json.loads(output)
        
        self.assertEqual(data['summary']['total_matches'], 0)
        self.assertEqual(len(data['results']), 0)


if __name__ == '__main__':
    unittest.main()
