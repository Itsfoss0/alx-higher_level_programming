#!/usr/bin/python3
""" Locked class """


class LockedClass():
    """No attribute creation unless attribute = firs_name"""
    __slots__ = ['first_name']

    def __init__(self):
        """Init method"""
        pass
