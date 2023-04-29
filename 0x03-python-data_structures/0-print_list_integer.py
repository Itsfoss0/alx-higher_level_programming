#!/usr/bin/python3
"""Module to print numbers in a list"""


def print_list_integer(my_list=[]):
    """Prints all integers of a list"""
    for num in my_list:
        print("{:d}".format(num))
