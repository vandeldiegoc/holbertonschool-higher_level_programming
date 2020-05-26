#!/usr/bin/python3
"""make a new class"""


class Rectangle:
    """class rectangle"""
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def height(self):
        return self.__whidth

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__whidth

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__width = value

    def void(self):
        pass
