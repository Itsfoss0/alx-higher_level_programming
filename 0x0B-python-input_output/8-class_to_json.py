#!/usr/bin/python3

"""class to JSON function."""


def class_to_json(obj):
    """Return the dictionary representation <obj>'s class
    Args:
        obj(object) -> Any object
    Returns:
        obj.__dict__."""
    return obj.__dict__
