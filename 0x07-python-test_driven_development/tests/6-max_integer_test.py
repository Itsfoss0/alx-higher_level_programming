#!/usr/bin/python3
import unittest

def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result


class TestMaxInteger(unittest.TestCase):
    """Test cases"""
    def __init__(self):
        pass
    def test_maxinteget(self):
        self.AssertEqual(max_integer([1, 2, 3, 4]), 4)
        self.AsserRaises(max_integer("some string"), None)
