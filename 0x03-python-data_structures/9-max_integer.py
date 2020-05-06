#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) < 1:
        return None
    else:
        max = my_list[0]
        for a in my_list:
            if a > max:
                max = a
        return max
