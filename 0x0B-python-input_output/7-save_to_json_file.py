#!/usr/bin/python3
"""module"""

import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as json_file:
        json_file.write(json.dumps(my_obj))
