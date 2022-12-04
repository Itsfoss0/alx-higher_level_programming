#!/usr/bin/python3
if __name__ == "__main__":
    def print_reversed_list_integer(my_list=[]):
        reversed_list = reversed(my_list)
        for item in reversed_list:
            print("{0:d}".format(item))
