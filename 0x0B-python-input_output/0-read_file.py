#!/usr/bin/python3
"""module"""


def read_file(filename=""):
    """funtion"""
    with open(filename, encoding="utf-8") as reedf:
        print(reedf.read())
