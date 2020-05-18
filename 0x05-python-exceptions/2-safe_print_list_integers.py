#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for a in range(0, x):
        try:
            print("{:d}".format(my_list[a]), end="")
        except ValueError:
            continue
        except TypeError:
            continue
        i += 1
    print()
    return i
