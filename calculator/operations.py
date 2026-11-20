"""Basic operations.

ROLE: Simple - Basic Functions

Your job: implement the four basic math functions below.
Every function takes two numbers and returns a number.

Done when: `python -m unittest tests.test_operations` passes.
"""


def add(a: float, b: float) -> float:
    """Return a + b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return a - b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return a * b."""
    return a * b

def divide(a: float, b: float) -> float:
    """Return a / b.

    If b is 0, raise ZeroDivisionError with a friendly message,
    e.g. raise ZeroDivisionError("Cannot divide by zero")
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
