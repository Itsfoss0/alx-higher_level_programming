#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(int(value)))
    except ValueError, TypeError:
        pass
    return isinstance(value, int)
