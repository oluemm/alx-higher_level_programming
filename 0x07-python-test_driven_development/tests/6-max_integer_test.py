#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer([..])"""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_rand_list(self):
        """Test a random list of integers."""
        self.assertEqual(max_integer([1, 7, 4, 3]), 7)

    def test_fraction_list(self):
        """Test list of fractions."""
        self.assertEqual(max_integer([1/5, 1/2, 1/4, 2/5]), 1/2)

    def test_floats_list(self):
        """Test a list of floats."""
        self.assertEqual(max_integer([1.7, 1.2, 2.4, 5.3]), 5.3)

    def test_negative_list(self):
        """Test a list of negative integers."""
        self.assertEqual(max_integer([-10, -12, -24, -53]), -10)

    def test_mixed_list(self):
        """Test a list of mixed numeric values."""
        self.assertEqual(max_integer([-10, 1/2, 2.4, -5.3, 21/7]), 21/7)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_string(self):
        """Test a string."""
        string = "Emmanuel"
        self.assertEqual(max_integer(string), 'u')

    def test_list_string(self):
        """Test a list strings."""
        string = ["Emmanuel", "Elnatha", "Ezekiel", "Esther"]
        self.assertEqual(max_integer(string), "Ezekiel")


if __name__ == '__main__':
    unittest.main()
