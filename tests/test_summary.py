import unittest
from log_viewer.searcher import search_logs
from log_viewer.formatters.text import format_text


class SummaryTests(unittest.TestCase):
    def test_summary_earliest_latest(self):
        path = "sample_logs.txt"
        keyword = "login"
        matches = search_logs(path, keyword, context=0)
        total = sum(1 for _ in open(path, "r", encoding="utf-8"))
        out = format_text(matches, keyword, total)
        # check we have Earliest and Latest lines
        self.assertIn("Earliest:", out)
        self.assertIn("Latest:", out)
        # ensure earliest is 2025-03-01T10:21:30 and latest 2025-03-01T10:30:00
        self.assertIn("2025-03-01T10:21:30", out)
        self.assertIn("2025-03-01T10:30:00", out)


if __name__ == "__main__":
    unittest.main()
