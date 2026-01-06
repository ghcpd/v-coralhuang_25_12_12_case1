import unittest
from log_viewer.searcher import search
from log_viewer.formatters.text import format_text


class TestTextOutput(unittest.TestCase):
    def test_text_contains_headers_line_numbers_and_highlight(self):
        res = search("sample_logs.log", "login", context=1)
        txt = format_text(res, context=1)
        # Section headers
        self.assertIn("LOG VIEWER REPORT", txt)
        self.assertIn("RESULTS", txt)
        # Line numbers like [1]
        self.assertRegex(txt, r"\[\d+\]")
        # Highlighted keyword marker <<login>> should appear
        self.assertIn("<<login>>", txt.lower())


if __name__ == "__main__":
    unittest.main()
