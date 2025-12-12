import unittest
import json
from log_viewer import search_logs_enhanced

class TestSummary(unittest.TestCase):
    def test_summary_includes_required_fields(self):
        result = search_logs_enhanced('sample.log', 'INFO', format='json')
        data = json.loads(result)
        summary = data['summary']
        self.assertIn('total_lines', summary)
        self.assertIn('num_matches', summary)
        self.assertIn('earliest_ts', summary)
        self.assertIn('latest_ts', summary)

    def test_summary_values_correct(self):
        result = search_logs_enhanced('sample.log', 'INFO', format='json')
        data = json.loads(result)
        summary = data['summary']
        self.assertEqual(summary['total_lines'], 4)
        self.assertEqual(summary['num_matches'], 4)  # All lines have INFO