#!/usr/bin/python3
"""find the values of length six in a given list using"""
less_6 = lambda strings : [x for x in strings if len(x) == 6]
print(less_6(["John", "Doe", "Martin", "Riggs"]))