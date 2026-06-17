"""Core arithmetic operations.

Each function is deliberately simple. The point of this repo is NOT the
math — it is to give the CI pipeline something real to lint, test and build.
"""


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return a minus b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return a divided by b.

    Raises:
        ZeroDivisionError: if b is 0. We raise explicitly so the behaviour
        is documented and tested, rather than relying on Python's default.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def power(base: float, exponent: float) -> float:
    """Return base raised to the given exponent."""
    return base**exponent
