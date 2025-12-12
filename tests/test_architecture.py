import importlib
import os


def test_modular_structure():
    # package modules exist
    pkg = importlib.import_module("logviewer")
    base = os.path.dirname(pkg.__file__)
    assert os.path.exists(os.path.join(base, "reader.py"))
    assert os.path.exists(os.path.join(base, "searcher.py"))
    assert os.path.exists(os.path.join(base, "formatters"))
