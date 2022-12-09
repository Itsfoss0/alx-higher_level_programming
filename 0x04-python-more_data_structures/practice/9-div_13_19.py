#!/usr/bin/python3
"""find numbers divisible by nineteen or thirteen from a list of numbers"""
divibles = lambda int_list : [x for x in int_list if (x % 13 == 0 ) and (x % 19 == 0)]