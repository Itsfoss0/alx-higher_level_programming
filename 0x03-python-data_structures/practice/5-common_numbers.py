#!/usr/bin/python3
"""Find the common numbers in two lists (without using a tuple or set)"""
list_a = 1, 2, 3, 4
list_b = 2, 3, 4, 5

common = [number for number in list_a if number in list_b]
print(common)