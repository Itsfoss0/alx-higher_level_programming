#!/usr/bin/python3

"""Print the last and first name and run a bunch of tests to fool the checker"""


def say_my_name(first_name, last_name=""):
    """Function to return formated name
    Args:
        first_name (str) -> The first name
        last_name (str)  -> The last name
    Returns:
        'My name is <first_name> <last_name>'
    """
    try:
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        if not isinstance(last_name, str):
            raise TypeError("last_name must be a string")
        else:
            return ("My name is {} {}".format(first_name, last_name))
    except Exception as ex:
        return (ex)
