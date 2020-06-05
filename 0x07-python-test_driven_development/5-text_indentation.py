#!/usr/bin/python3
"""module"""


def text_indentation(text):
    """module indentation"""
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    string = ""
    list_s = ['.', '?', ':']
    x = 0
    while x != (len(text)):
        if text[x] in list_s:
            string += text[x]
            string += "\n\n"
            x += 2
            continue
        string += text[x]
        x += 1
    print(string, end="")
