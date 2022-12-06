#!/usr/bin/python3
""" Count the number of spaces in a string """
def space_count(string):
    return len([x for x in string if x == " "])
    
my_string = "John Doe is Cool!"
print(space_count(my_string))
