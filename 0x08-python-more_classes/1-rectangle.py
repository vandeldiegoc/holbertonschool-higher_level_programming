#!/usr/bin/python3
"""make a new class"""


class Rectangle:
    """class rectangle"""
    def __init__(self, width=0, height=0):
        """constructor"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width getter method"""
        return self.__width

    @property
    def height(self):
        """ height getter method"""
        return self.__height

    @width.setter
    def width(self, value):
        """ width setter method"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """setter method"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__height = value
