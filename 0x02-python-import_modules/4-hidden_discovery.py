#!/usr/bin/python3
if __name__ == "__main__":
    for a in dir(hidden_4):
        if not a.startwith("__"):
            print("{}".format(a))
