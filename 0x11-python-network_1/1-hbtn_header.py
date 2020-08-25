#!/usr/bin/python3
"""new module"""
from urllib import request
import sys


if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as response:
        headers = response.info()
        print(headers['X-Request-Id'])
