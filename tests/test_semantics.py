import unittest
import importlib


class TestArchitectureAndModules(unittest.TestCase):
    def test_modular_structure_exists(self):
        # Import modules to ensure modular architecture present
        pkg = importlib.import_module("log_viewer")
        reader = importlib.import_module("log_viewer.reader")
        searcher = importlib.import_module("log_viewer.searcher")
        fmt_text = importlib.import_module("log_viewer.formatters.text")
        fmt_json = importlib.import_module("log_viewer.formatters.json_fmt")
        fmt_pretty = importlib.import_module("log_viewer.formatters.pretty")

        # Basic sanity checks
        self.assertTrue(hasattr(reader, "read_lines"))
        self.assertTrue(hasattr(searcher, "search"))
        self.assertTrue(hasattr(fmt_text, "format_text"))
        self.assertTrue(hasattr(fmt_json, "format_json"))
        self.assertTrue(hasattr(fmt_pretty, "format_pretty"))


if __name__ == "__main__":
    unittest.main()
