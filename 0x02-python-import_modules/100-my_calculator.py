#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1);

    else:
        opcode = str(sys.argv[2])
        operand_1 = int(sys.argv[1])
        operand_2 = int(sys.argv[3])

        if  opcode == '+':
            print("{0} + {1} = {2}".format(operand_1, operand_2, add(operand_1, operand_2)))
        elif opcode == '-':
            print("{0} - {1} = {2}".format(operand_1, operand_2, sub(operand_1, operand_2)))
        elif opcode == '*':
            print("{0} * {1} = {2}".format(operand_1, operand_2, mul(operand_1, operand_2)))
        elif opcode == '/':
            print("{0} / {1} = {2}".format(operand_1, operand_2, div(operand_1, operand_2)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
            
