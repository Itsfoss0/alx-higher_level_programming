#!/usr/bin/python3

"""Read a file and print its content to stdout"""


def read_file(filename=""):
    """Read <filename>'s content
    Args:
        filename(str) -> the name of the file
    Returns:
        None
    """
    if filename:
        with open(filename, encoding="utf-8") as f:
            print(f.read(), end="")
