#!/usr/bin/python3
"""
function that add numbers
"""


def add_integer(a, b=98):
    """module fuinction that add numbers"""
    if isinstance(a, int) or isinstance(a, float):
        if isinstance(b, int) or isinstance(b, float):
            return int(a) + int(b)
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
