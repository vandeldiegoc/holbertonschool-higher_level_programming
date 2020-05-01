#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    for i in dir():
        if i[1] != "_":
            print(i)
#   for a in dir(hidden_4):
#        if not a.startwith("__"):
#            print("{}".format(a))
