#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arguments = []
    if len(sys.argv) == 2:
        print("1 argument")
    else:
        print("{} arguments".format(len(sys.argv)-1))
        for arg in sys.argv:
            arguments.append(arg)

        for i in range(1, len(arguments)):
            print("{0}: {1}".format(i, arguments[i]))
