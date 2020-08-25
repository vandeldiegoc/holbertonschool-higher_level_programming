#!/usr/bin/python3
"""new module"""
from urllib import request
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode("ascii"))
    except HTTPError as error:
        print("Error code: {}".format(error.code))
