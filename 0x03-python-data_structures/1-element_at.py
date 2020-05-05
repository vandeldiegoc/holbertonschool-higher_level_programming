#!/usr/bin/python3
def element_at(my_list, idx):
    for x in my_list:
        if idx > len(my_list):
            return None
        else:
            return my_list[idx]
