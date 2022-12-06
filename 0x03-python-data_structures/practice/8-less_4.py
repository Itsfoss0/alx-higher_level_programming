#!/usr/bin/python3
"""Find all of the words in a string that are less than 4 letters"""

string = "I love programming in python and C"
less_4 = [x for x in string.split(" ") if len(x) < 4]
print(less_4)