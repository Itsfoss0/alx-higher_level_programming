#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Return new list with item at position idx set to elelement"""
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    new_list = [item for item in my_list]
    new_list[idx] = element
    return new_list
