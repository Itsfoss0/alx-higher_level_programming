#!/usr/bin/python3


""" Base class """


class BaseGeometry:
    """BaseGeometry as the base class"""

    def area(self):
        """Lets raise an exception """
        raise Exception("area() is not implemented")
