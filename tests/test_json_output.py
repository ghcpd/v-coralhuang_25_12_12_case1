import unittest
import json
from log_viewer.searcher import search_logs
from log_viewer.formatters.json_fmt import format_json


class JsonOutputTests(unittest.TestCase):
    def test_json_struct_and_metadata(self):
        path = "sample_logs.txt"
        keyword = "login"
        matches = search_logs(path, keyword, context=0)
        total = sum(1 for _ in open(path, "r", encoding="utf-8"))
        out = format_json(matches, total)
        parsed = json.loads(out)
        self.assertIsInstance(parsed, dict)
        self.assertIn("summary", parsed)
        self.assertIn("results", parsed)
        self.assertEqual(parsed["summary"]["matches"], len(parsed["results"]))
        # each result has fields
        for r in parsed["results"]:
            self.assertIn("line_number", r)
            self.assertIn("line", r)
            self.assertIn("timestamp", r)


if __name__ == "__main__":
    unittest.main()
