#!/usr/bin/python
import json

""" Function to serialize an object to JSON"""


def to_json_string(my_obj):
    """Serialize an object to JSON
    Args:
        my_obj(object) -> Any serializable object
    """
    return (json.dump(my_obj))
