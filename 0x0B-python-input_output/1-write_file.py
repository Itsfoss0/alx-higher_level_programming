#!/usr/bin/python3

""" Function to write to a file"""


def write_file(filename="", text=""):
    """Write <text> to <filename> overriding
    Args:
        filename(str) -> Name of the file to write to
        text(str)     -> Content to write
    Returns:
        Number of characters written
    """
    if filename:
        with open(filename, "w", encoding="utf-8") as file_to_write:
            original_content = file_to_write.tell()
            file_to_write.write(text)
            new_content = file_to_write.tell()
            return new_content - original_content
