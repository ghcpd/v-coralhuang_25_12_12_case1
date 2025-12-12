import unittest
from log_viewer_original import search_logs as original_search
from log_viewer.searcher import search, search_logs


class TestSummaryAndSemantics(unittest.TestCase):
    def test_match_counts_and_lines_equal_original(self):
        keyword = "login"
        orig = original_search("sample_logs.log", keyword)
        enhanced_raw = search_logs("sample_logs.log", keyword)
        # Legacy helper should preserve original behavior
        self.assertEqual(len(orig), len(enhanced_raw))
        # All matched lines should correspond (order preserved)
        self.assertEqual(orig, enhanced_raw)

    def test_summary_timestamps_and_counts(self):
        res = search("sample_logs.log", "login", context=0)
        self.assertEqual(res["matches_count"], len(res["matches"]))
        # earliest and latest should be parseable or None
        et = res.get("earliest_timestamp")
        lt = res.get("latest_timestamp")
        # If present they should be strings in ISO format
        if et:
            self.assertIsInstance(et, str)
        if lt:
            self.assertIsInstance(lt, str)


if __name__ == "__main__":
    unittest.main()
