import unittest

from calculator.validator import is_valid_partial


class TestValidator(unittest.TestCase):
    def test_valid_inputs(self):
        for text in ["", "3", "42", "3+", "3+4", "3 + 4 * 2", "1.5", "1.5+2.5", "10/2-"]:
            with self.subTest(text=text):
                self.assertTrue(is_valid_partial(text))

    def test_invalid_character(self):
        for text in ["x", "3+a", "3$", "(3)"]:
            with self.subTest(text=text):
                self.assertFalse(is_valid_partial(text))

    def test_leading_operator(self):
        for text in ["+", "*3", "/2"]:
            with self.subTest(text=text):
                self.assertFalse(is_valid_partial(text))

    def test_double_operator(self):
        for text in ["3++", "3+*", "3 * / 4", "3 + + 4"]:
            with self.subTest(text=text):
                self.assertFalse(is_valid_partial(text))

    def test_double_decimal(self):
        for text in ["1.2.3", "1..2", "3+1.2.5"]:
            with self.subTest(text=text):
                self.assertFalse(is_valid_partial(text))

    def test_decimal_resets_for_each_number(self):
        self.assertTrue(is_valid_partial("1.5+2.5"))


if __name__ == "__main__":
    unittest.main()
