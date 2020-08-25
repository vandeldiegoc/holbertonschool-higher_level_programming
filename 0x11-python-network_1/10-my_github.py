#!/usr/bin/python3
"""new script"""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(argv[1], argv[2])
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=auth)
    reques = r.json()
    print(reques.get('id'))
