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

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def void(self):
        pass

    def __str__(self):
        """
        print rectangle
        """
        xy = ""
        for y in range(self.__height):
            for x in range(self.__width):
                xy += '#'
            if y != self.__height - 1:
                xy += '\n'
        return xy
