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
        """width getter method"""
        return self.__width

    @property
    def height(self):
        """height getter method"""
        return self.__height

    @width.setter
    def width(self, value):
        """width setter method"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """setter method"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area"""
        return self.__height * self.__width

    def perimeter(self):
        """perimeter"""
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
