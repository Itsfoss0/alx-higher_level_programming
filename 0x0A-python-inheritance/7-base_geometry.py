#!/usr/bin/python3


""" Base class """


class BaseGeometry:
    """BaseGeometry as the base class"""

    def area(self):
        """Lets raise an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate name and value
        Args:
            name(string)
            value(int)
        Raises:
            TypeError: if not isinstance(value, int)
            ValueError: if value <= 0
        """
        try:
            if type(value) != int:
                raise TypeError("{} must be an integer".format(name))
            if value <= 0:
                raise ValueError("{} must be greater than 0".format(name))
        except Exception as e:
            return e
