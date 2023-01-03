#!/usr/bin/python3
"""Defining my rectangle class"""


class Rectangle:
    """Rectangle class with setters and getters"""
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int) ->  The width of the new rectangle.
            height (int)->  The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height Getter
        Args:
            None
        Returns:
            self.__height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height Setter
        Args:
            value(int) -> The new value of the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """String representation of object
        of the Rectangle class
        """
        if self.__height == 0 or self.__width == 0:
            return ("")
        rectangles = []
        for i in range(self.__height):
            [rectangle.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rectangles.append("\n")
        return ("".join(rectangles))
