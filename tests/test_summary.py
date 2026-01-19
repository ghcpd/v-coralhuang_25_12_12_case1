"""Test cases for summary information."""

import unittest
import datetime
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from log_viewer.reader import LogReader
from log_viewer.searcher import LogSearcher


class TestSummaryInfo(unittest.TestCase):
    """Test summary information extraction."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.searcher = LogSearcher()
        
        # Create test log lines
        self.test_logs = [
            "2025-03-01T10:21:30 INFO [u1] Alice logged in\n",
            "2025-03-01T10:22:00 INFO [u2] Bob logged in\n",
            "2025-03-01T10:23:10 DEBUG [u1] Alice viewed page\n",
            "2025-03-01T10:25:00 INFO [u2] Bob logged out\n",
            "2025-03-01T10:30:00 ERROR System error occurred\n",
        ]
    
    def test_extract_earliest_timestamp(self):
        """Test extracting earliest timestamp from logs."""
        earliest, latest = self.searcher.extract_timestamps(self.test_logs)
        
        self.assertIsNotNone(earliest)
        self.assertEqual(earliest.hour, 10)
        self.assertEqual(earliest.minute, 21)
    
    def test_extract_latest_timestamp(self):
        """Test extracting latest timestamp from logs."""
        earliest, latest = self.searcher.extract_timestamps(self.test_logs)
        
        self.assertIsNotNone(latest)
        self.assertEqual(latest.hour, 10)
        self.assertEqual(latest.minute, 30)
    
    def test_timestamp_range_correct(self):
        """Test that timestamp range is computed correctly."""
        earliest, latest = self.searcher.extract_timestamps(self.test_logs)
        
        # Latest should be after earliest
        self.assertGreater(latest, earliest)
    
    def test_no_timestamps_returns_none(self):
        """Test handling when no timestamps are found."""
        logs_without_ts = [
            "Log line without timestamp\n",
            "Another line\n",
        ]
        
        earliest, latest = self.searcher.extract_timestamps(logs_without_ts)
        
        self.assertIsNone(earliest)
        self.assertIsNone(latest)
    
    def test_search_count_accuracy(self):
        """Test that search returns correct number of matches."""
        results = self.searcher.search(self.test_logs, "Alice")
        
        # Should find exactly 2 matches (Alice appears twice)
        self.assertEqual(len(results), 2)
    
    def test_search_count_zero_matches(self):
        """Test search when keyword doesn't exist."""
        results = self.searcher.search(self.test_logs, "NonexistentKeyword")
        
        self.assertEqual(len(results), 0)
    
    def test_search_case_sensitivity(self):
        """Test case-sensitive vs case-insensitive search."""
        # Case-insensitive (default)
        results_insensitive = self.searcher.search(
            self.test_logs, "alice", case_sensitive=False
        )
        
        # Case-sensitive
        results_sensitive = self.searcher.search(
            self.test_logs, "alice", case_sensitive=True
        )
        
        # Insensitive should find matches, sensitive should not
        self.assertGreater(len(results_insensitive), 0)
        self.assertEqual(len(results_sensitive), 0)


if __name__ == '__main__':
    unittest.main()
