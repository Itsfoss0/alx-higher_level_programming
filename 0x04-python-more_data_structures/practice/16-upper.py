#!/usr/bin/python3
"""convert all the characters in uppercase and lowercase 
and eliminate duplicate letters from a given sequence. Use map() function """
letters = ["a", "b", "c", "d", "e", "f","a", "b"]
print(list(set(map(lambda x : x.upper(), letters))))