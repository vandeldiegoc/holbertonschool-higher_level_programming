#!/usr/bin/python3
"""module"""

import json


def save_to_json_file(my_obj, filename):
    """save json"""
    with open(filename, 'w') as json_file:
        json.dump(my_obj, json_file)
