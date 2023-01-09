#!/usr/bin/python3


"""Returns true is an object is an instance of a class"""


def is_same_class(obj, a_class):
    """ Returns True if object is instance of class ;
    otherwise False.
    Args:
        obj -> the object in question
        a_class -> the class to compared against
    Returns:
        True if type(obj) == a_class; False otherwise
    """
    return isinstance(obj, a_class) and type(obj) == a_class
