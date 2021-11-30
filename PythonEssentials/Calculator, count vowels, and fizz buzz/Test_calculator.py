import calculator
import unittest

class CalculatorTests(unittest.TestCase):

    # Test add method.
    def test_add(self):
        a = 4
        b = 23
        result = calculator.Calculator.add(self, a, b)
        self.assertEqual(result, 27)

    # Test subtract method.
    def test_subtract(self):
        a = 3
        b = 39
        result = calculator.Calculator.subtract(self, a, b)
        self.assertEqual(result, -36)

    # Test multiply method.
    def test_multiply(self):
        a = 2
        b = 17
        result = calculator.Calculator.multiply(self, a, b)
        self.assertEqual(result, 34)

    # Test divide method.
    def test_divide(self):
        a = 6
        b = 3
        result = calculator.Calculator.divide(self, a, b)
        self.assertEqual(result, 2.0)

    # Test divicion on zero.
    def test_divide_on_zero(self):
        a = 5
        b = 0
        result = calculator.Calculator.divide(self, a, b)
        self.assertEqual(result, 'Divicion on zero')

if __name__=='__main__':
    unittest.main()