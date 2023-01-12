#!/usr/bin/python3
from models.base import Base

"""Rectangle class based on the Base class"""


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, w):
        """Width setter
        Args:
            w(int) -> Width of the rectangle
        """
        self.__width = w

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, h):
        """Height setter
        Args:
            h(int) -> Height of the rectangle
        """
        self.__height = h

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter
        Args:
            x(int) -> value of x
        """
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter
        Args:
            y(int) -> value of y
        """
        self.__y = y
