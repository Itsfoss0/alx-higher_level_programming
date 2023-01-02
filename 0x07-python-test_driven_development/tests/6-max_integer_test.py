#!/usr/bin/python3
import unittest
max_integer = __import__('6-max-integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defining unit tests for max_integer function"""
    def test_maxinteger_sorted(self):
        """Test for a sorted list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_maxinteger_unsorted(self):
        """Tests for an unsorted list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_maxinteger_reverse(self):
        """"Tests for a reverse sorted lists"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_maxinteger_empty(self):
        """"Test for empty list"""
        self.assertEqual(max_integer([]), None)

    def test_maxinteger_nan(self):
        """Test for NaN values in the list"""
        self.assertEqual(max_integer(["1", "2", "3", "4"]), "4")

    def test_maxinteger_string(self):
        """Test for a string"""
        self.assertEqual(max_integer("John Doe"), "o")

    def test_maxinteger_floats(self):
        """Test for floats"""
        self.assertEqual(max_integer([1.2, 3.1, 2.5, 4.9]), 4.9)

    def test_maxinteger_one(self):
        """Tesf for one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_maxinteger_none(self):
        """Test for none object"""
        self.assertRaises(TypeError, max_integer, None)

    def test_maxinteger_negatives(self):
        """Test for negative numbers"""
        self.assertEqual(max_integer([-1, -3, -5, -7]), -1)
if __name__ == '__main__':
    unittest.main()
