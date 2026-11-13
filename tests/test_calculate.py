"""End-to-end tests: text in, answer out. These pass once ALL the
non-GUI roles are done - the integration person's finish line."""

import unittest

from calculator import calculate


class TestCalculate(unittest.TestCase):
    def test_end_to_end(self):
        self.assertEqual(calculate("3 + 4 * 2"), 11.0)
        self.assertEqual(calculate("10 / 4"), 2.5)
        self.assertEqual(calculate("2*3+8/4-1"), 7.0)

    def test_errors(self):
        with self.assertRaises(ZeroDivisionError):
            calculate("5 / 0")
        with self.assertRaises(ValueError):
            calculate("hello")


if __name__ == "__main__":
    unittest.main()
