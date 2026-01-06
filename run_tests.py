"""Run all tests in tests/ and exit with appropriate status code.

This script uses unittest discovery by default. If pytest is installed,
it will prefer pytest for nicer output, but pytest is optional.
"""
import sys
import subprocess
import importlib


def run_with_pytest():
    try:
        import pytest  # type: ignore
        # Run pytest in-process
        errno = pytest.main(["-q", "tests"])
        return 0 if errno == 0 else 1
    except Exception:
        return None


def run_with_unittest():
    import unittest

    loader = unittest.TestLoader()
    suite = loader.discover("tests")
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return 0 if result.wasSuccessful() else 1


def main():
    # Prefer pytest if available
    rc = run_with_pytest()
    if rc is None:
        rc = run_with_unittest()
    sys.exit(rc)


if __name__ == "__main__":
    main()
