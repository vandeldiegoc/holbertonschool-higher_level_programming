#!/usr/bin/python3
"""class Square"""


class Square:
    """Class private instance"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """mthod tha return private attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """method that return current area"""
        return self.__size ** 2

    def my_print(self):
        """method that print"""
        if self.size == 0:
            print()
        else:
            for x in range(self.size):
                print("#" * self.size)
