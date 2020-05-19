#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as argument:
        import sys
        sys.stderr.write("Exception: {}\n".format(argument))
        return False
    return True
