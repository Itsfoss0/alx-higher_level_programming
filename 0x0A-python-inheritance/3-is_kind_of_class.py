#!/usr/bin/python3


""" Is kind of a class, object is an instance of a class or inherited class """


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.
    Args:
        obj (any) ->  The object to check.
        a_class (type) ->  The class to match the type of obj to.
    Returns:
        True if isinstance(obj, a_class); False Otherwise
    """
    return isinstance(obj, a_class)
