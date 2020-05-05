#!/usr/bin/python3
def no_c(my_string):
    a = ""
    for x in my_string:
        if x != 'c' and x != 'C':
            a += x
    return a
