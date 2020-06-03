#!usr/bin/python3

def read_lines(filename="", nb_lines=0):
    line_number = 0
    with open(filename, encoding="utf-8") as readf:
        for a_line in readf:
            print('{}'.format(a_line), end="")
            line_number += 1
            if line_number == nb_lines:
                break