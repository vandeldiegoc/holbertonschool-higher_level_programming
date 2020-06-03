#!/usr/bin/python3
"""module"""


def write_file(filename="", text=""):
    """write in file"""
    with open(filename, mode='w', encoding="utf-8") as filew:
        j = filew.write(text)
        return j
