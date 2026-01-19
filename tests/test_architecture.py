import unittest
import os

class TestArchitecture(unittest.TestCase):
    def test_modular_structure_exists(self):
        self.assertTrue(os.path.exists('log_viewer'))
        self.assertTrue(os.path.exists('log_viewer/reader.py'))
        self.assertTrue(os.path.exists('log_viewer/searcher.py'))
        self.assertTrue(os.path.exists('log_viewer/formatters'))
        self.assertTrue(os.path.exists('log_viewer/formatters/text.py'))
        self.assertTrue(os.path.exists('log_viewer/formatters/json_fmt.py'))
        self.assertTrue(os.path.exists('log_viewer/formatters/pretty.py'))