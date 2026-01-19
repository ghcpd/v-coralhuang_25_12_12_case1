import os
import unittest


class ArchitectureTests(unittest.TestCase):
    def test_layout(self):
        base = os.path.join(os.getcwd())
        self.assertTrue(os.path.exists(os.path.join(base, "log_viewer", "reader.py")))
        self.assertTrue(os.path.exists(os.path.join(base, "log_viewer", "searcher.py")))
        self.assertTrue(os.path.exists(os.path.join(base, "log_viewer", "formatters", "text.py")))
        self.assertTrue(os.path.exists(os.path.join(base, "log_viewer", "formatters", "json_fmt.py")))
        self.assertTrue(os.path.exists(os.path.join(base, "log_viewer", "formatters", "pretty.py")))


if __name__ == "__main__":
    unittest.main()
