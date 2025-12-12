import unittest
from log_viewer import search_logs_enhanced

class TestTextOutput(unittest.TestCase):
    def test_text_output_contains_headers(self):
        result = search_logs_enhanced('sample.log', 'Alice', format='text')
        self.assertIn('SEARCH RESULTS', result)
        self.assertIn('SUMMARY', result)

    def test_text_output_contains_line_numbers(self):
        result = search_logs_enhanced('sample.log', 'Alice', format='text')
        self.assertIn('Line ', result)

    def test_text_output_highlights_keyword(self):
        result = search_logs_enhanced('sample.log', 'Alice', format='text')
        self.assertIn('**Alice**', result)