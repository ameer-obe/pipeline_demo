"""Unit tests for the calculator package.

pytest discovers any file named test_*.py and any function named test_*.
The CI pipeline runs exactly these tests on every pull request.
"""

import pytest

from calculator import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10


def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3


def test_divide_by_zero_raises():
    # We expect a ZeroDivisionError. If divide() ever stops raising,
    # this test fails and the pipeline goes red.
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
