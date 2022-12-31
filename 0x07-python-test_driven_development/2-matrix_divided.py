#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divides all the elements of matrix by div and returns a new list
    Args:
        matrix (list)   -> A list of integers or floats
        div (int/float) -> Non Zeoro divisor, Can be int or float
    Returns a new list
    """
    new_list = []
    try:
        for x in matrix:
            for y in x
            if not isinstance(y, int):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for index in range(len(matrix) -1):
            if len(matrix[index]) != len(matrix[index+1]):
                raise TypeError("Each row of the matrix must have the same size")
        if type(div) not in [float, int]:
            raise TypeError("div must be a number")
        elif div == 0:
            raise ZeroDivisionError("division by zero")