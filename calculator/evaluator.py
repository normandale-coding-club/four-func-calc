"""Evaluates a list of tokens, respecting order of operations.

ROLE: Medium - Order of Operations

Your job: take a token list (made by tokenizer.py) and compute the answer.
Multiplication and division happen BEFORE addition and subtraction,
and operators of the same level go left to right.

    evaluate([3.0, "+", 4.0, "*", 2.0])  ->  11.0   (not 14.0!)
    evaluate([8.0, "/", 2.0, "/", 2.0])  ->  2.0    (left to right)

Use the functions from operations.py to do the actual math -
don't use Python's + - * / directly on the numbers.

Hint: one approach is two passes over the list - first collapse all
* and /, then work through the + and -.

Invalid token lists (e.g. empty, or [3.0, "+"]) -> raise ValueError.

Stretch goal: support parentheses "(" and ")" (coordinate with the
tokenizer person!).

Done when: `python -m unittest tests.test_evaluator` passes.
"""

from calculator import operations
from calculator.tokenizer import Token

# Maps each operator symbol to the function that performs it.
OPERATIONS = {
    "+": operations.add,
    "-": operations.subtract,
    "*": operations.multiply,
    "/": operations.divide,
}


def evaluate(tokens: list[Token]) -> float:
    """Compute the result of a token list using order of operations."""
    # TODO: implement
    raise NotImplementedError
