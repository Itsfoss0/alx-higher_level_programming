#!/usr/bin/python3

"""Insert a string of text, after each line matching the search term"""


def append_after(filename="", search_string="", new_string=""):
    """Insert <new_string> after everly line that has <search_string>
    Args:
        filename(str) -> Name of the file
        search_string(str) -> string to match
        new_string(str) -> string to append
    """
    text_string = ""
    with open(filename) as f_read:
        for line in f_read:
            text_string += line
            if search_string in line:
                text_string += new_string
    with open(filename, "w") as f_write:
        f_write.write(text_string)
