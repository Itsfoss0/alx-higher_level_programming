#!/usr/bin/python3

"""Add all arguments to a list and save them to a .json"""


import os
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    save_to_json_file(sys.argv[1:], "add_item.json")
