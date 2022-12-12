#!/usr/bin/python3
""" convert a given list of strings into list of lists using map function"""
strings = ["Python", "is", "Awesome", "and", "so", "is", "she"]
print(list(map(list,strings)))