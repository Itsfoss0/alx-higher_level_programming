#!/usr/bin/python3

"""Read a file and print its content to stdout"""


def read_file(filename=""):
    """Read filename's content
    Args:
        filename(str) -> the name of the file
    Returns:
        None
    """
    if filename:
        try:
            with open(filename, "w", encoding="UTF-8") as file:
                print(file.read())
        except Exception as e:
            return (e)
