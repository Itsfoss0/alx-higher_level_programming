#!/usr/bin/python3


""" Module to assert if an object is an instance
of a class that inherited from the specifed classs
"""


def inherits_from(obj, a_class):
    """Check if an object is an instance of class that inherits from a_class.
    Args:
        obj (any) ->  The object to check.
        a_class (type) ->  The class to match the type of obj to.
    Returns:
        True if class of obj inherits a_class; False Otherwise
    """
    obj_class = type(obj)
    return issubclass(obj_class, a_class) and type(obj) != a_class
