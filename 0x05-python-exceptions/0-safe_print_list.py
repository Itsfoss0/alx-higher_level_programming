#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x+1):
            print(my_list[i], end="")
    except IndexError:
        print("Index is out of range")
