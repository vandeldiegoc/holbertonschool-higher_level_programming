def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return None
    else:
        my_list.reverse()
        for a in my_list:
            print("{:d}".format(a))
