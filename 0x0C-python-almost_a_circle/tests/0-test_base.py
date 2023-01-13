#!/usr/bin/python3
from models.base import Base
import unittest

"""Base class test suites"""


class TestBase(unittest.TestCase):
    """Testing the Base class"""
 
    def test_no_args(self):
        """Test Base with no args"""
        self.assertEqual(Base().id, 1)