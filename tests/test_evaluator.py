"""Evaluator tests use hand-written token lists, so they don't depend on
the tokenizer being finished. (They DO need operations.py to work.)"""

import unittest

from calculator.evaluator import evaluate


class TestEvaluator(unittest.TestCase):
    def test_single_number(self):
        self.assertEqual(evaluate([7.0]), 7.0)

    def test_simple(self):
        self.assertEqual(evaluate([3.0, "+", 4.0]), 7.0)

    def test_multiply_before_add(self):
        self.assertEqual(evaluate([3.0, "+", 4.0, "*", 2.0]), 11.0)

    def test_divide_before_subtract(self):
        self.assertEqual(evaluate([10.0, "-", 6.0, "/", 2.0]), 7.0)

    def test_left_to_right_same_level(self):
        self.assertEqual(evaluate([8.0, "/", 2.0, "/", 2.0]), 2.0)
        self.assertEqual(evaluate([10.0, "-", 3.0, "-", 2.0]), 5.0)

    def test_mixed(self):
        # 2 * 3 + 8 / 4 - 1 = 6 + 2 - 1 = 7
        tokens = [2.0, "*", 3.0, "+", 8.0, "/", 4.0, "-", 1.0]
        self.assertEqual(evaluate(tokens), 7.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            evaluate([1.0, "/", 0.0])

    def test_invalid(self):
        with self.assertRaises(ValueError):
            evaluate([])
        with self.assertRaises(ValueError):
            evaluate([3.0, "+"])


if __name__ == "__main__":
    unittest.main()
