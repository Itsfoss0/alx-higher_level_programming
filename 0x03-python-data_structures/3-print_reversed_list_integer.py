#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for x in range(len(my_list), 0 -1):
        print("{0:d} ".format(my_list[x]))

print_reversed_list_integer(my_list = [1,2,3,4,5])
