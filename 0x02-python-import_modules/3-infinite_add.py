#!/usr/bin/python
import sys
if __name__ == "__main__":
    sum_total = 0
    for i in range(len(sys.argv) - 1):
        sum_total += int(sys.argv[i + 1])
    print("{0:d}".format(sum_total))
