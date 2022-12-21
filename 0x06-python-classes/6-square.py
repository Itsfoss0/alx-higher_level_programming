#!/usr/bin/python3
"""class Square that defines a square"""


class Square():
    """Implementing the square class"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Get the value of size
        Args:
            None
        Returns:
            __size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the value of the square
        Args:
            value (int)
        Returns:
            None
        """
        if (not isinstance(value, int)):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """"set position"""
        if (not is isinstance(value, tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[0]) is not int) or (type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Compute and Return area
        Args:
            None
        Returns
            __size x 4
        """
        return self.__size ** 2

    def my_print(self):
        if not self.__size:
            print("")
        for i in range(self.__size):
            print("#" * self.__size)
