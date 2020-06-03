#!/usr/bin/python3
"""module"""


def read_file(filename=""):
    """funtion"""
    with open(filename, 'r', encoding="utf-8") as reedf:
        print(reedf.read(), end="")
