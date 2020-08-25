#!/usr/bin/python3
"""new script"""
import requests
from sys import argv


if __name__ == "__main__":
    reques = requests.get(argv[1])
    if reques.status_code > 400:
        print("Error code: {}".format(reques.status_code))
    else:
        print(reques.text)
