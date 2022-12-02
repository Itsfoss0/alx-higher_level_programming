#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        opcode = str(sys.argv[2])
        a = int(sys.argv[1])
        b = int(sys.argv[3])

        if opcode == '+':
            print("{0} + {1} = {2}".format(a, b, add(a, b)))
        elif opcode == '-':
            print("{0} - {1} = {2}".format(a, b, sub(a, b)))
        elif opcode == '*':
            print("{0} * {1} = {2}".format(a, b, mul(a, b)))
        elif opcode == '/':
            print("{0} / {1} = {2}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
