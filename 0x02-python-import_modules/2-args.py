#!/usr/bin/python3
import sys
if __name__ == '__main__':
    print("{} arguments:".format(len(sys.argv[1:])))
    for i in range(len(sys.argv[1:])):
        print("{}: {}".format(i + 1, sys.argv[i+1]))
