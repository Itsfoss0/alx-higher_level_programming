#!/usr/bin/python3

"""
Almost a circle Project
Preparing for the AirBnB Clone project
"""
import json
import os.path
import csv


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
