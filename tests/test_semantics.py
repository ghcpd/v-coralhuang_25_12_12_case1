import unittest
import log_viewer_original
from log_viewer.searcher import search_logs


class SemanticTests(unittest.TestCase):
    def test_matches_equal_original(self):
        keyword = "login"
        path = "sample_logs.txt"
        original = log_viewer_original.search_logs(path, keyword)
        enhanced_matches = search_logs(path, keyword)
        # original contains raw lines; enhanced contains dicts
        self.assertEqual(len(original), len(enhanced_matches))
        # compare raw content by line number
        for raw_line, match in zip(original, enhanced_matches):
            self.assertIn(raw_line, match["line"])  # raw line is a substring


if __name__ == "__main__":
    unittest.main()
