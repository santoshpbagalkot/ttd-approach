"""
Calculator class tests.
"""
import unittest

from calculator import Calculator

class TestCalculatorAdd(unittest.TestCase):
    """Test the add method of the Calculator class."""
    
    def setUp(self) -> None:
        """Set up the test fixtures."""
        pass
    def test_empty_string_returns_zero(self):
        calc_obj = Calculator()
        self.assertEqual(calc_obj.add(""), 0)

    def test_single_number_returns_the_number(self):
        calc_obj = Calculator()
        self.assertEqual(calc_obj.add("1"), 1)

    def test_sum_of_two_numbers(self):
        calc_obj = Calculator()
        self.assertEqual(calc_obj.add("1,5"), 6)

    def test_sum_of_multiple_numbers(self):
        calc_obj = Calculator()
        self.assertEqual(calc_obj.add("1,5,10, 4"), 20)
