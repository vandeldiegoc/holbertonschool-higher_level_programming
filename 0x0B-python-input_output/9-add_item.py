#!/usr/bin/python3
"""save ti json file"""

import sys


load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

try:
    prevl = load_from_json_file("add_item.json")
except Exception as e:
    prevl = []
for i in range(1, len(sys.argv)):
    prevl.append(sys.argv[i])
save_to_json_file(prevl, "add_item.json")
