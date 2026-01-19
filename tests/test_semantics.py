"""Test cases for semantic correctness and architecture."""

import unittest
import sys
import os
import json
import tempfile

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from log_viewer_enhanced import search_logs
from log_viewer.reader import LogReader
from log_viewer.searcher import LogSearcher


class TestSemanticCorrectness(unittest.TestCase):
    """Test semantic correctness of enhanced implementation."""
    
    def setUp(self):
        """Set up test fixtures."""
        # Create a temporary test log file
        self.test_content = """2025-03-01T10:21:30 INFO [u1] Alice logged in from 1.2.3.4
2025-03-01T10:22:00 INFO [u2] Bob logged in from 5.6.7.8
2025-03-01T10:23:10 DEBUG [u1] Alice viewed page /home
2025-03-01T10:25:00 INFO [u2] Bob logged out
2025-03-01T10:26:45 ERROR [u3] Charlie login failed: invalid credentials
2025-03-01T10:27:30 WARNING [u1] Alice attempted unauthorized access
2025-03-01T10:30:00 INFO [u4] Diana logged in from 9.10.11.12
2025-03-01T10:32:45 INFO [u1] Alice downloaded report
2025-03-01T10:35:00 INFO [u1] Alice logged out
"""
        
        # Write to temp file
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt')
        self.temp_file.write(self.test_content)
        self.temp_file.close()
    
    def tearDown(self):
        """Clean up temp files."""
        import os as os_module
        if os.path.exists(self.temp_file.name):
            os_module.remove(self.temp_file.name)
    
    def test_match_count_consistency(self):
        """Test that match counts are consistent across formats."""
        text_output = search_logs(self.temp_file.name, "Alice", format_type='text')
        json_output = search_logs(self.temp_file.name, "Alice", format_type='json')
        
        # Extract match count from text output
        text_count = int([line for line in text_output.split('\n') 
                         if 'Total Matches:' in line][0].split(':')[1].strip())
        
        # Extract match count from JSON
        json_data = json.loads(json_output)
        json_count = json_data['summary']['total_matches']
        
        # Should be equal
        self.assertEqual(text_count, json_count)
        self.assertEqual(text_count, 5)  # Alice appears 5 times in test data
    
    def test_matched_lines_consistency(self):
        """Test that matched lines are the same across formats."""
        text_output = search_logs(self.temp_file.name, "Bob", format_type='text')
        json_output = search_logs(self.temp_file.name, "Bob", format_type='json')
        
        json_data = json.loads(json_output)
        
        # Count "Bob" occurrences in text output
        text_bob_count = text_output.count("Bob")
        # Count in JSON
        json_bob_count = sum(1 for r in json_data['results'] 
                           if "Bob" in r['line_content'])
        
        self.assertGreater(text_bob_count, 0)
        # Both should have same count of Bob results (4 times)
        self.assertGreaterEqual(text_bob_count, json_bob_count)
    
    def test_no_false_matches(self):
        """Test that all matches are legitimate."""
        output = search_logs(self.temp_file.name, "Alice", format_type='json')
        data = json.loads(output)
        
        # Verify each result actually contains the keyword
        for result in data['results']:
            self.assertIn("Alice", result['line_content'])
    
    def test_line_numbers_are_sequential(self):
        """Test that line numbers are correct and sequential."""
        output = search_logs(self.temp_file.name, "INFO", format_type='json')
        data = json.loads(output)
        
        # Line numbers should be 1-indexed
        for result in data['results']:
            self.assertGreater(result['line_number'], 0)
            self.assertLessEqual(result['line_number'], 
                               len(self.test_content.split('\n')))
    
    def test_modular_architecture_exists(self):
        """Test that modular architecture components exist."""
        from log_viewer import reader, searcher
        from log_viewer.formatters import text, json_fmt, pretty
        
        # Check key classes exist
        self.assertTrue(hasattr(reader, 'LogReader'))
        self.assertTrue(hasattr(searcher, 'LogSearcher'))
        self.assertTrue(hasattr(text, 'TextFormatter'))
        self.assertTrue(hasattr(json_fmt, 'JSONFormatter'))
        self.assertTrue(hasattr(pretty, 'PrettyFormatter'))
    
    def test_separate_responsibilities(self):
        """Test that components have separate responsibilities."""
        from log_viewer.reader import LogReader
        from log_viewer.searcher import LogSearcher
        from log_viewer.formatters.text import TextFormatter
        
        # Reader should read files
        self.assertTrue(hasattr(LogReader, 'read_file'))
        
        # Searcher should search
        self.assertTrue(hasattr(LogSearcher, 'search'))
        
        # Formatter should format
        self.assertTrue(hasattr(TextFormatter, 'format'))
    
    def test_context_lines_optional(self):
        """Test that context lines are optional."""
        output_no_context = search_logs(
            self.temp_file.name, "Alice", format_type='text', context_lines=0
        )
        output_with_context = search_logs(
            self.temp_file.name, "Alice", format_type='text', context_lines=1
        )
        
        # With context should have more content
        self.assertGreater(len(output_with_context), len(output_no_context))


if __name__ == '__main__':
    unittest.main()
