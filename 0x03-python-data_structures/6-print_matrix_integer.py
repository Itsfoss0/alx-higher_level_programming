#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers"""
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if not j == 0:
                print(" ", end='')
            print("{:d}".format(matrix[i][j]), end='')
        print()
