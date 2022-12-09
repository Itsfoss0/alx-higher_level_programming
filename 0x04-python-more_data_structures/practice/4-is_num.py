#!/usr/bin/python3
"""check whether a given string is number or not using Lambda"""
is_num = lambda string : string.replace(".", "", 2).isdigit()
print(is_num("12.3"))