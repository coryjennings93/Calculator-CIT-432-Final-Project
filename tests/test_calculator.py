import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(-1, 1), 0)
        # Add more test cases for addition function

    def test_sub(self):
        self.assertEqual(self.calculator.sub(5, 3), 2)
        # Add more test cases for subtraction function

    def test_multiply(self):
        self.assertEqual(self.calculator.mult(2, 3), 6)
        # Add more test cases for multiplication function

    def test_divide(self):
        self.assertEqual(self.calculator.divide(6, 3), 2)
        # Add more test cases for division function

    def test_sqroot(self):
        self.assertAlmostEqual(self.calculator.sqroot(4), 2)
        # Add more test cases for square root function

if __name__ == '__main__':
    unittest.main()