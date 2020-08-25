#!/usr/bin/python3
"""new script"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    r = requests.post(url, data={'q': q})
    try:
        reques = r.json()
        if "id" in reques and "name" in reques:
            print("[{}] {}i".format(reques['id'], reques['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
