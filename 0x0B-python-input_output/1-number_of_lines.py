#!/usr/bin/python3
"""module"""

def number_of_lines(filename="" ):
    """return line number"""
    line_number = 0
    with open(filename) as readf:
        for read_line in readf:
            line_number += 1
        return line_number
