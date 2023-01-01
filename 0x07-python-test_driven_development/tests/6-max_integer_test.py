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


if __name__ == '__main__':
    unittest.main()
