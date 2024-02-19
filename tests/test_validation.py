import unittest
from validation import Validation

class TestValidation(unittest.TestCase):
    def test_validate_numeric_input(self):
        self.assertEqual(Validation.validate_numeric_input('10'), 10)
        self.assertEqual(Validation.validate_numeric_input('0.5'), 0.5)
        self.assertRaises(ValueError, Validation.validate_numeric_input, 'abc')
        # Add more test cases for validate_numeric_input function

    def test_validate_menu_choice(self):
        self.assertEqual(Validation.validate_menu_choice('1'), 1)
        self.assertRaises(ValueError, Validation.validate_menu_choice, 'abc')
        self.assertRaises(ValueError, Validation.validate_menu_choice, '7')
        # Add more test cases for validate_menu_choice function

    def test_validate_yes_or_no(self):
        self.assertEqual(Validation.validate_yes_or_no('y'), 'Y')
        self.assertEqual(Validation.validate_yes_or_no('n'), 'N')
        self.assertEqual(Validation.validate_yes_or_no('Y'), 'Y')
        self.assertEqual(Validation.validate_yes_or_no('N'), 'N')
        self.assertRaises(ValueError, Validation.validate_yes_or_no, 'abc')
        # Add more test cases for validate_yes_or_no function

if __name__ == '__main__':
    unittest.main()