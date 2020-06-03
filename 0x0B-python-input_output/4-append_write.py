#!/usr/bin/python3
"""module"""


def append_write(filename="", text=""):
    """write in file"""
    with open(filename, 'a', encoding="utf-8") as filew:
        j = filew.write(text)
        return j
