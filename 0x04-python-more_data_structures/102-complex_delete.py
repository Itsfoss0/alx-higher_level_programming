#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in dictionary.items():
        return a_dictionary
    for key, val in a_dictionary.items():
        if val == value:
            del a_dictionary[val]
    return a_dictionary
