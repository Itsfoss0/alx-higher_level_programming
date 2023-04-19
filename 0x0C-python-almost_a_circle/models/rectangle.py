#!/usr/bin/python3
"""Rectangle class based on the Base class"""

import json
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif x < 0:
            raise ValueError("y must be >= 0")
        else:
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
        Raises:
            TypeError -> if w is not an interger
            valuError -> if w <= 0
        """
        if not isinstance(w, int):
            raise TypeError("width must be an integer")
        elif w <= 0:
            raise ValueError("width must be > 0")
        else:
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
        Raises:
            TypeError -> if h is not an integer
            ValueError -> if h is <= 0
        """
        if not isinstance(h, int):
            raise TypeError("height must be an integer")
        elif h <= 0:
            raise ValueError("height must be >= 0")
        else:
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
        Raises:
            TypeError -> if x is not an int
            ValueError -> if x < 0
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
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
        Raises:
            TypeError -> if y is not an integer
            ValueError -> if y < 0
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif x < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """Area of the rectangle
        Returns:
            width * height
        """
        return self.__height * self.__width

    def display(self):
        """ Print a rectangle using '#'"""
        rect = self.__y * "\n"
        for i in range(self.__height):
            rect += (" " * self.__x)
            rect += (" " * self.__width) + "\n"

    def __str__(self):
        """str() representation of an instance"""
        return ("[Rectangle] {} {}/{} - {}/{}".format(self.__id,
                self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Update an instance using non-keyworded args
        Args:
            *args(list) -> A list of un-keyworded args.
                        -> Order is super important
        """
        if args is not None and len(args) is not 0:
            attributes = ['__id', '__width', '__height', '__x', '__y']
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Object to dictionary"""
        return (json.dumps(self))
