#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_d = {}
    for i in a_dictionary:
        new_d[i] = 2 * a_dictionary[i]
    return new_d
    
