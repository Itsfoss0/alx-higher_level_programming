#!/usr/bin/python3
"""Square class to represent a square"""


class Square():
    """square class with it's size and proper validation"""

    def __init__(self, size=0, position=(0, 0)):
        """"Initialize data"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """"get size"""
        return self.__size

    @property
    def position(self):
        """"get position"""
        return self.__position

    @size.setter
    def size(self, value):
        """"set size"""
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """"set position"""
        if (not isinstance(value, tuple)):
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
        """"get area of the square"""
        return self.size ** 2

    def my_print(self):
        """print the square"""
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print("")
            for i in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
