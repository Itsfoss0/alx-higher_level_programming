#!/usr/bin/python3

"""Serialize an object and write to a file"""


import json


def save_to_json_file(my_obj, filename):
    """Serialize an object to JSON and write to a file
    Args:
        my_obj(object) -> Any serializable object
        file_name(str) -> The file to write to
    """
    if filename and my_obj:
        serialized_object = json.dumps(my_obj)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(serialized_object)
