#!/usr/bin/python3
"""
print div
"""


def add_integer(a, b=98):
    if isinstance(a, int) or isinstance(a, float):
        if isinstance(b, int) or isinstance(b, float):
            return (a + b)
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
