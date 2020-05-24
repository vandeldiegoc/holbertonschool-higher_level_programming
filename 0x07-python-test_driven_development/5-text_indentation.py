#!/usr/bin/python3
def text_indentation(text):
    string = ""
    list_s = ['.', '?', ':']
    for x in range(len(text)):
        if text[x] in list_s:
            print(text[x])
        elif text[x - 1] in list_s:
            print()
        else:
            print(text[x], en<F12>d='')
