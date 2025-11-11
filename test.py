import unittest
from calculator_app import Calculator

class TestOperations(unittest.TestCase):

    def test_sum(self):
        calc = Calculator(10, 2)
        self.assertEqual(calc.get_quotient(), 5, "The division is wrong")

    # Test: difference, product, sum

    def test_sum(self):
        calc = Calculator(2, 3)
        self.assertEqual(calc.get_product(), 6, "The product is wrong")

if __name__ == "__main__":
    unittest.main()


