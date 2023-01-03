#!/usr/bin/python3
"""Defining my rectangle class"""


class Rectangle:
    """Rectangle class with setters and getters"""
    def __init__(self, width=0, height=0):
        """Init method"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Width getter
        Args:
            None
        Returns:
            self.__width
        """
        return self.__width

    @property
    def height(self):
        """Height getter
        Args:
            None
        Returns:
            self.__width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter
        Args:
            value(int)
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Height setter
        Args:
            value(int)
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__width = value
