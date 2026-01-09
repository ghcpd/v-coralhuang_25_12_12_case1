import sys


def main():
    try:
        import pytest
    except Exception as e:
        print("pytest is required to run the tests. Install with pip install pytest")
        return 2
    # run pytest programmatically
    errno = pytest.main(["-q"])
    return errno


if __name__ == "__main__":
    sys.exit(main())
