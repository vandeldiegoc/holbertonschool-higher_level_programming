#!/usr/bin/python3
"""funtion"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    size = len(list_of_integers)
    if size == 0:
        return 0
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)
    half = int(size / 2)
    peak = list_of_integers[half]
    if peak > list_of_integers[half - 1] and peak > list_of_integers[half + 1]:
        return peak
    elif peak < list_of_integers[half - 1]:
        return find_peak(list_of_integers[:half])
    elif peak < list_of_integers[half + 1]:
        return find_peak(list_of_integers[half + 1:])
