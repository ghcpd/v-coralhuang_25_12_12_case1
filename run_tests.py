#!/usr/bin/env python
import sys
import subprocess
import os


def main():
    # Try pytest
    try:
        import pytest  # noqa: F401
        ret = pytest.main(["-q", "tests"])  # -q quiet
        sys.exit(ret)
    except Exception:
        # Fallback to unittest
        import unittest

        loader = unittest.TestLoader()
        suite = loader.discover("tests")
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        sys.exit(0 if result.wasSuccessful() else 1)


if __name__ == "__main__":
    main()
