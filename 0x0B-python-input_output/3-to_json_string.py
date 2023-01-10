#!/usr/bin/python3

""" Function to serialize an object to JSON"""


import json


def to_json_string(my_obj):
    """Serialize an object to JSON
    Args:
        my_obj(object) -> Any serializable object
    """
    return (json.dumps(my_obj))
