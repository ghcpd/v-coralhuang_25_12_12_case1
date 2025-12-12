import unittest
from log_viewer.searcher import search_logs
from log_viewer.formatters.text import format_text


class TextOutputTests(unittest.TestCase):
    def test_text_contains_headers_line_numbers_and_highlight(self):
        path = "sample_logs.txt"
        keyword = "login"
        matches = search_logs(path, keyword, context=1)
        total = sum(1 for _ in open(path, "r", encoding="utf-8"))
        out = format_text(matches, keyword, total)
        self.assertIn("LOG SEARCH RESULTS", out)
        self.assertIn("Matches:", out)
        self.assertIn("Total lines scanned:", out)
        # Ensure at least one Line <num>: marker
        self.assertRegex(out, r"Line \d+: ")
        # keyword highlighted with **
        self.assertIn("**login**", out.lower() if isinstance(out, str) else out)


if __name__ == "__main__":
    unittest.main()
