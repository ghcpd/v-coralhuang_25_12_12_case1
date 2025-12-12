import unittest
import json
from log_viewer import search_logs_enhanced

class TestJsonOutput(unittest.TestCase):
    def test_json_output_is_valid(self):
        result = search_logs_enhanced('sample.log', 'Alice', format='json')
        data = json.loads(result)
        self.assertIsInstance(data, dict)
        self.assertIn('matches', data)
        self.assertIn('summary', data)

    def test_json_matches_include_metadata(self):
        result = search_logs_enhanced('sample.log', 'Alice', format='json')
        data = json.loads(result)
        if data['matches']:
            match = data['matches'][0]
            self.assertIn('line_number', match)
            self.assertIn('line', match)
            self.assertIn('context', match)