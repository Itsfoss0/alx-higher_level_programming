#!/usr/bin/python3
for num in range(0, 100):
    if num == 99:
        print("{0:02d}".format(num), end="\n")
    else:
        print("{0:02d}, ".format(num), end="")
