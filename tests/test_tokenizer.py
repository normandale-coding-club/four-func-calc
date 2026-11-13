import unittest

from calculator.tokenizer import tokenize


class TestTokenizer(unittest.TestCase):
    def test_single_number(self):
        self.assertEqual(tokenize("42"), [42.0])

    def test_simple_expression(self):
        self.assertEqual(tokenize("3 + 4"), [3.0, "+", 4.0])

    def test_all_operators(self):
        self.assertEqual(
            tokenize("1 + 2 - 3 * 4 / 5"),
            [1.0, "+", 2.0, "-", 3.0, "*", 4.0, "/", 5.0],
        )

    def test_no_spaces(self):
        self.assertEqual(tokenize("10/2"), [10.0, "/", 2.0])

    def test_multi_digit_and_decimals(self):
        self.assertEqual(tokenize("123.5 * 0.25"), [123.5, "*", 0.25])

    def test_invalid_character(self):
        with self.assertRaises(ValueError):
            tokenize("3 + x")


if __name__ == "__main__":
    unittest.main()
