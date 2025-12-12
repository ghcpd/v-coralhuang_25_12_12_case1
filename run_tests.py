"""
One-click test runner for the enhanced log viewer.

Discovers and runs all tests in the tests/ directory.
"""

import unittest
import sys
import os


def run_tests():
    """Discover and run all tests."""
    # Get the directory containing this script
    root_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(root_dir, 'tests')
    
    # Discover tests
    loader = unittest.TestLoader()
    suite = loader.discover(tests_dir, pattern='test_*.py')
    
    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Exit with appropriate status code
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    exit_code = run_tests()
    sys.exit(exit_code)
