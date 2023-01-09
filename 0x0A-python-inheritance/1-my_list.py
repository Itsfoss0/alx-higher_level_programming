#!/usr/bin/python3


"""MyList class"""


class MyList(list):
    """My list class inheritting list"""

    def print_sorted(self):
        """Print a list sorted in ascending order"""
        print(sorted(self, reverse=False))
