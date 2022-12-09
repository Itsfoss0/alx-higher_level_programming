#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in dictionary.items():
        return a_dictionary
    for val in a_dictionary.values():
        if val == value:
            del a_dictionary[value]
    return a_dictionary
