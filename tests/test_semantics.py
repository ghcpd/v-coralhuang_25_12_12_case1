import unittest
import json
from log_viewer_original import search_logs as original_search
from log_viewer import search_logs_enhanced

class TestSemantics(unittest.TestCase):
    def test_number_of_matches_equals_original(self):
        original_matches = original_search('sample.log', 'Alice')
        enhanced_result = search_logs_enhanced('sample.log', 'Alice', format='json')
        data = json.loads(enhanced_result)
        num_matches = len(data['matches'])
        self.assertEqual(len(original_matches), num_matches)

    def test_matched_lines_correspond(self):
        original_matches = [line.strip() for line in original_search('sample.log', 'Alice')]
        enhanced_result = search_logs_enhanced('sample.log', 'Alice', format='json')
        data = json.loads(enhanced_result)
        enhanced_lines = [match['line'] for match in data['matches']]
        self.assertEqual(set(original_matches), set(enhanced_lines))