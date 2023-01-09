#!/usr/bin/python3

"""Rectangle class that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using base geometry"""
    def __init__(self, width, height):
        """ Initializing a new rectangle
        Args:
            width(int) -> The width of the rectangle
            height(int) -> The height of the rectangle
        """
        self.integer_validator("w", width)
        self.__width = width
        self.integer_validator("h", height)
        self.__height = height
