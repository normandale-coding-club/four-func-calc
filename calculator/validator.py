"""Checks what the user is typing BEFORE it reaches the display.

ROLE: Medium - Input Validation

Your job: decide whether a piece of text is a sensible *start* of an
expression. The GUI calls this every time a button is pressed, and
ignores the press if you return False. That way bad input like "3++"
never even shows up on screen.

    is_valid_partial("")        ->  True    (nothing typed yet is fine)
    is_valid_partial("3+")      ->  True    (unfinished, but could become valid)
    is_valid_partial("3++")     ->  False   (two operators in a row)
    is_valid_partial("1.2.3")   ->  False   (a number can only have one ".")
    is_valid_partial("*3")      ->  False   (can't start with an operator)
    is_valid_partial("3 + 4")   ->  True    (spaces are ignored)

Rules:
  - Allowed characters: digits 0-9, ".", spaces, and + - * /
    Anything else -> False.
  - An operator can't be first, and can't come right after another operator.
  - Each number can have at most one ".".
  - Notice "3+" is True: you're checking "could this still turn into
    something valid?", not "is this finished?". The evaluator handles
    finished expressions when "=" is pressed.

Hint: loop over the characters and keep track of two things - what the
last non-space character was, and whether the current number already
has a ".".

This file doesn't know the GUI exists - it just takes a string and
returns True/False. That's what makes it easy to test.

Stretch goals:
  - Allow a leading "-" for negative numbers ("-3", "3*-2"). Coordinate
    with the tokenizer person - they have the same stretch goal!
  - Limit numbers to a max length (e.g. 15 digits).

Done when: `python -m unittest tests.test_validator` passes.
"""

from calculator.tokenizer import OPERATORS


def is_valid_partial(text: str) -> bool:
    """Return True if text could be the beginning of a valid expression."""
    # TODO: implement
    # This starts out returning True (allow everything) so the GUI keeps
    # working while you build it. Your tests will fail until you're done.
    return True
