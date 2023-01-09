#!/usr/bin/python3

"""MyInt class that inherits from int"""


class MyInt(int):
    """MyInt class with != and == interchanged"""
    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
