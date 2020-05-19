#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        x = fct(*args)
        return x
    except Exception as argument:
        import sys
        sys.stderr.write("Exception: {}\n".format(argument))
        return None
