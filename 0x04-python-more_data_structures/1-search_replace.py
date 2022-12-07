#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return ([item if item != search else replace for item in my_list])
