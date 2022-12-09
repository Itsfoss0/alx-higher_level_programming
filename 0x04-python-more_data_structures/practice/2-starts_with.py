#!/usr/bin/python3
"""program to find if a given string starts with a given character using Lambda"""
starts_with = lambda string, char: string[0] == char
print(starts_with("John Doe", 'J'))
