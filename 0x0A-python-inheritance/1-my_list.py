#!/usr/bin/python3


"""MyList class"""


class MyList(list):
    """My list class inheritting list"""

    def __init__(self):
        super().__init__()
    
    def print_sorted(self):
        """Print a list sorted in ascending order"""
        print(sorted(self, reverse=False))
