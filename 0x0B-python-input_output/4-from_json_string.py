#!/usr/bin/python3

"""Function to unserialize a JSON string to python object"""


import json


def from_json_string(my_str):
    """Unserialize <my_str>
    Args:
        my_str(str) -> JSON string to unserialize
    Returns:
        unserialized object repesentation of my_str
    """
    if my_str:
        return json.loads(my_str)
