#!/usr/bin/python3


def number_of_lines(filename=""):

    line_number = 0
    with open(filename) as readf:
        for read_line in readf:
            line_number += 1
        return line_number
