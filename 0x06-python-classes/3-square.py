#!/usr/bin/python3
"""class Square"""


class Square:
    """Class private instance"""
    def __init__(self, size=0):
        """initialization attribute"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """method that return current area"""
        return self.__size ** 2
