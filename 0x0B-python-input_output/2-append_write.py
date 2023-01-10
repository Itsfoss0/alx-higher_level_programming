#!/usr/bin/python3

""" Function to append to a file"""


def append_write(filename="", text=""):
    """Append <text> to <filename>
    Args:
        filename(str) -> Name of the file to append to
        text(str)     -> Content to append
    Returns:
        Number of characters written
    """
    if filename:
        with open(filename, "a", encoding="utf-8") as f:
            pre_content = f.tell()
            f.write(text)
            post_content = f.tell()
            return post_content - pre_content
