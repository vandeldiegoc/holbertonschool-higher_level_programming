#!/usr/bin/python3
def text_indentation(text):
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
