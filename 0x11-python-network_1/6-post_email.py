#!/usr/bin/python3
"""new module"""
import requests
from sys import argv


if __name__ == "__main__":
    value = {'email': argv[2]}
    pos_t = requests.post(argv[1], data=value)
    print(pos_t.text)
