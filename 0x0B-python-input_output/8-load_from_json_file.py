#!/usr/bin/python3
"""module"""
import json


def load_from_json_file(filename):
    """load file"""
    with open(filename, 'r') as filer:
        return json.loads(filer.read())
