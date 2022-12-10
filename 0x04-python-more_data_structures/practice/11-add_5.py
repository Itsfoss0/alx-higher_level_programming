#!/usr/bin/python3
""" add plus 5 to each item in the list"""
numbers = [1, 2, 3, 4, 5, 6]
print(list(map(lambda x: x+5, numbers)))