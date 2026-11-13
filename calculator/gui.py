"""The calculator window.

ROLE: Medium - App GUI

Your job: build the calculator's window using tkinter (built into Python,
nothing to install). A starter window is already here so you can run it.

Want a different GUI library? Go for it - just add it to requirements.txt
so everyone else can install it, and keep run() as the entry point
(main.py calls it).

To do:
  - A display that shows what the user has typed so far.
  - Buttons for 0-9, ".", +, -, *, /, = and C (clear).
  - Clicking a number/operator button adds it to the display.
  - "=" calls calculate(display_text) and shows the result.
  - "C" clears the display.
  - If calculate() raises ValueError or ZeroDivisionError, show
    "Error" (or the message) instead of crashing.

Stretch goals:
  - Keyboard support (typing numbers, Enter for =, Escape for clear).
  - Make it look nice!

You don't need the other roles to be finished to work on layout -
until they are, "=" will just show an error.

Run it with: python main.py
"""

import tkinter as tk  # |||| feel free to use whatever library you want |||

from calculator import calculate


class CalculatorApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Calculator")

        # The text shown at the top of the calculator.
        self.display = tk.StringVar(value="")
        tk.Entry(root, textvariable=self.display, font=("Arial", 20), justify="right").grid(
            row=0, column=0, columnspan=4, sticky="ew"
        )

        # TODO: create the buttons and lay them out in a grid.

    def press(self, char: str) -> None:
        """Called when a number or operator button is clicked."""
        # TODO: add char to the end of the display
        raise NotImplementedError

    def clear(self) -> None:
        """Called when C is clicked."""
        # TODO: empty the display
        raise NotImplementedError

    def equals(self) -> None:
        """Called when = is clicked."""
        # TODO: call calculate(self.display.get()), show the result,
        # and handle ValueError / ZeroDivisionError.
        raise NotImplementedError


def run() -> None:
    root = tk.Tk()
    CalculatorApp(root)
    root.mainloop()
