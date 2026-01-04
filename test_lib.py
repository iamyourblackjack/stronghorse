"""Shared test utilities for LeetCode problems."""


def test(func, args, expected, name):
    """Run a single test case and print the result."""
    result = func(*args)
    status = "✓" if result == expected else "✗"
    print(f"  {status} {name}: {args} → {result}")
    assert result == expected, f"Expected {expected}, got {result}"


def run_tests(tests):
    """Run multiple test cases.

    Args:
        tests: List of tuples (func, args, expected, name)
    """
    print("Running tests...")
    for t in tests:
        test(*t)
    print("All tests passed!")

