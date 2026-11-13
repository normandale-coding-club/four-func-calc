"""Turns the text a user typed into a list of tokens.

ROLE: Medium - Multi Input Handling

Your job: take a string like "3 + 4 * 2" and break it into a list of
numbers and operators that the evaluator can work with.

    tokenize("3 + 4 * 2")  ->  [3.0, "+", 4.0, "*", 2.0]
    tokenize("10/2")       ->  [10.0, "/", 2.0]
    tokenize("1.5 - 0.5")  ->  [1.5, "-", 0.5]

Rules:
  - Numbers become floats.
  - Operators stay as one-character strings: "+", "-", "*", "/".
  - Spaces should be ignored (and are optional).
  - Anything else (letters, "$", etc.) -> raise ValueError.

Stretch goals:
  - Negative numbers: "-3 + 2" -> [-3.0, "+", 2.0]
  - Catch bad sequences like "3 + + 4" or "3 +" -> raise ValueError

Done when: `python -m unittest tests.test_tokenizer` passes.
"""

OPERATORS = {"+", "-", "*", "/"}

Token = float | str


def tokenize(expression: str) -> list[Token]:
    """Split an expression string into numbers and operators."""
    # TODO: implement
    raise NotImplementedError
