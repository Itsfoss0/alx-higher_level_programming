#!/usr/bin/python3

"""Serialize an object and write to a file"""


import json


def save_to_json_file(my_obj, filename):
    """Serialize an object to JSON and write to a file
    Args:
        my_obj(object) -> Any serializable object
        file_name(str) -> The file to write to
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
