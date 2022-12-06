#!/usr/bin/python3
"""Get only the numbers in a sentence like
 In 1984 there were 13 instances of a protest with over 1000 people attending
"""
string = "In 1984 there were 13 instances of a protest with over 1000 people attending"
only_numbers = [ x for x in string if isinstance(x, int)]
print(only_numbers)