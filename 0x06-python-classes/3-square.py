#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """Implementing square class """
    def __init__(self, size=0):
        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
