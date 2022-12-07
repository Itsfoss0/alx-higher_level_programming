#!/usr/bin/python3
"""Find all of the words in a string that are less than 4 letters"""
def less_than_4(string):
    return ([x for x in string.split(" ") if len(x) < 4])


my_string = "I love programming in python and C"
string_2 = "Did John join the DevOps team?"
print(less_than_4(my_string))
print(less_than_4(string_2))