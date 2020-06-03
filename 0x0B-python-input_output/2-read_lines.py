#!usr/bin/python3
"""module"""


def read_lines(filename="", nb_lines=0):
    """print line number"""
    line_number = 0
    with open(filename, 'r', encoding="utf-8") as readf:
        for a_line in readf:
            print(a_line, end="")
            line_number += 1
            if line_number == nb_lines:
                break
