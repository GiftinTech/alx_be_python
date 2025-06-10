import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
  # Test addition
  def test_addition(self):
    result = SimpleCalculator.add(self, 5, 6)
    self.assertEqual(result, 11)

  # Test subtraction
  def test_subtraction(self):
    result = SimpleCalculator.subtract(self, 10, 5)
    self.assertEqual(result, 5)

  # Test multiplication
  def test_multiplication(self):
    result = SimpleCalculator.multiply(self, 2, 10)
    self.assertEqual(result, 20)

  # Test division
  def test_division(self):
    result = SimpleCalculator.divide(self, 10, 2)
    self.assertEqual(result, 5)

  # Test Zero division
  def test_zero_division(self):
    result = SimpleCalculator.divide(self, 10, 0)
    self.assertEqual(result, None)

if __name__ == "__main__":
  unittest.main()