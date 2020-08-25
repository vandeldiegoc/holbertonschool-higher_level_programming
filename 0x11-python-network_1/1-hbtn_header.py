#!/usr/bin/python3
from urllib import request
import sys
"""new module"""


if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as response:
        headers = response.info()
        print(headers['X-Request-Id'])
