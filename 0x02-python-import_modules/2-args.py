#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arguments = []
    if len(sys.argv) == 2:
        print("1 argument:")
        print("{0}: {1}".format((len(sys.argv)-1), sys.argv[1]))
    else:
        for arg in sys.argv:
            arguments.append(arg)

        if len(sys.argv) == 1:
            print("{0} arguments.".format(len(sys.argv)-1))

        else:
            print("{} arguments: ".format(len(sys.argv)-1))

            for i in range(1, len(arguments)):
                print("{0}: {1}".format(i, arguments[i]))
