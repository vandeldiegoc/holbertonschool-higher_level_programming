#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = 0
    for a in range(1, len(argv)):
        i += int(argv[a])
    print("{:d}".format(i))
