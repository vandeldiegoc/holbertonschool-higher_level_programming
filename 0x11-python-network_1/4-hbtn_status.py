#!/usr/bin/python3
"""new module"""
import requests


if __name__ == "__main__":
    reque = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(reque.text)))
    print("\t- content: {}".format(reque.text))
