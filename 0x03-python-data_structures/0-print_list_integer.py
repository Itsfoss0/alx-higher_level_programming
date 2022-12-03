#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Prints all integers of a list"""
    for pos in range(0, len(my_list)):
        print("{0:d}".format(my_list[pos]))
