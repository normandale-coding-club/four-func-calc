"""Four-function calculator package.

calculate() is the single entry point to the GUI (or anything else) uses.
It chains the pieces together:

    text --tokenize--> tokens --evaluate--> number
"""

from calculator.evaluator import evaluate
from calculator.tokenizer import tokenize


def calculate(expression: str) -> float:
    """Turn a typed expression like "3 + 4 * 2" into its answer."""
    return evaluate(tokenize(expression))
