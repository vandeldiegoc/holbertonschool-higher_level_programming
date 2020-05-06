#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for v in matrix:
        print(' '.join("{:d}".format(h) for h in v))
