"""Tests for calculator - some are intentionally failing."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from calculator import add, subtract, multiply, divide, average, percentage


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide_normal():
    assert divide(10, 2) == 5.0


def test_divide_by_zero():
    """This test will FAIL - divide doesn't handle zero."""
    try:
        result = divide(10, 0)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


def test_average_normal():
    assert average([1, 2, 3, 4, 5]) == 3.0


def test_average_empty():
    """This test will FAIL - average doesn't handle empty list."""
    try:
        result = average([])
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


def test_percentage_normal():
    assert percentage(25, 100) == 25.0


def test_percentage_zero_total():
    """This test will FAIL - percentage doesn't handle zero total."""
    try:
        result = percentage(10, 0)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
