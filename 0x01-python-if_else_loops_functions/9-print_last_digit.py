#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        nn = number * -1
        print("{:d}".format(nn % 10), end="")
    else:
        print("{:d}".format(number % 10), end="")
    return number % 10
