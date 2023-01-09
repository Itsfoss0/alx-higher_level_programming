#!/usr/bin/python3

"""Function that adds attributes to object if possible"""


def add_attribute(objct, attribute, value):
    """Add attribute to an object if possible
    Args:
        objct(object) -> The object to be added an attribute
        attribute(str) -> Name of the attribute to add to objct
        value(object) -> The value of the atttribute
    """
    if not hasattr(objct, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(objct, attribute, value)
