import unittest
import json
from log_viewer.searcher import search
from log_viewer.formatters.json_fmt import format_json


class TestJsonOutput(unittest.TestCase):
    def test_json_is_well_formed_and_contains_metadata(self):
        res = search("sample_logs.log", "login", context=0)
        j = format_json(res)
        parsed = json.loads(j)
        # Top-level keys
        self.assertIn("matches", parsed)
        self.assertIn("matches_count", parsed)
        # Each match should include line_number and line
        self.assertGreaterEqual(len(parsed["matches"]), 1)
        for m in parsed["matches"]:
            self.assertIn("line_number", m)
            self.assertIn("line", m)


if __name__ == "__main__":
    unittest.main()
