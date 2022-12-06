#!/usr/bin/python3
"""
Given a list of numbers, remove floats (numbers with decimals)
"""
original_list = [2,3.75,.04,59.354,6,7.7777,8,9]
only_ints = [ x for x in original_list if isinstance(x, int)]
print(only_ints)