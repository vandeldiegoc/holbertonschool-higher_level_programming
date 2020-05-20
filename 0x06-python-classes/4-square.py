#!/usr/bin/python3
"""class Square"""


class Square:
    """Class private instance"""
    def __init__(self, size=0):
        """initialization attribute"""
        self.size = size

    @getter
    def size(self):
        """mthod tha return private attribute"""
        return self.__size

    @setter
    def size(self, value):
        """setter"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """method that return current area"""
        return self.size ** 2
