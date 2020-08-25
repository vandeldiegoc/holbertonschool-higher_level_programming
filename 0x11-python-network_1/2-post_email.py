#!/usr/bin/python3
"""new module"""
from urllib import parse
from urllib import request
import sys


if __name__ == "__main__":
    email = {'email': sys.argv[2]}
    encode = parse.urlencode(email).encode('ascii')
    reque = request.Request(sys.argv[1], encode)
    with request.urlopen(reque) as s_imail:
        print(s_imail.read().decode('utf-8'))
