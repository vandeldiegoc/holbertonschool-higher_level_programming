#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newlist = [[i*i for i in element] for element in matrix]
    return newlist
