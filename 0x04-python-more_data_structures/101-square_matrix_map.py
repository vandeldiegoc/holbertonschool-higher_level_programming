#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new = list(map(lambda x: list(map(lambda j: j ** 2, x)), matrix))
    return new
