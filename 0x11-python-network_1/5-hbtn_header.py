#!/usr/bin/python3
"""new module"""
import requests
from sys import argv


if __name__ == "__main__":
    reques = requests.get(argv[1])
    header_opc = reques.headers.get("X-Request-Id")
    print(header_opc)
