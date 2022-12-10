#!/usr/bin/python3
""" map function that adds "Hello, " in front of each item in the list"""
names = ["Janet", "Sharon", "John", "Doe", "Miranda", "Martin"]
print(list(map(lambda x: "Hello " + x, names)))