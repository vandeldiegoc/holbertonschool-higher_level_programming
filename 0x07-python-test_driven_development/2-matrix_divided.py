#!/usr/bin/python3
"""
print matrix
"""


def matrix_divided(matrix, div):
    error1 = "matrix must be a matrix (list of lists) of integers/floats"
    error2 = "matrix must be a matrix (list of lists) of integers/floats"
    new_matrix = []
    new_list = []
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not (isinstance(matrix, list)):
        raise TypeError(error1)
    for x in matrix:
        if len(matrix[0]) != len(x):
            raise TypeError("Each row of the matrix must have the same size")
        for y in x:
            if not isinstance(y, (int, float)):
                raise TypeError(error2)
            res = y / div
            new_list.append(round(res, 2))
        new_matrix.append(new_list)
        new_list = []
    return new_matrix
