#!/usr/bin/python3

"""Deserialize an JSON from a file"""


import json


def load_from_json_file(filename):
    """Create an object from JSON
    Args:
        filename(str) -> The filename holding JSON
    """
    if filename:
        with open(filename, 'r', encoding="utf-8") as f:
            return json.load(f)
