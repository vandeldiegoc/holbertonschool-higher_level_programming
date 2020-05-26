#!/usr/bin/python3
"""make a new class"""


class Rectangle:
    """class rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """constructor"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def __str__(self):
        """
        print rectangle
        """
        xy = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for y in range(self.__height):
            for x in range(self.__width):
                xy += '#'
            if y != self.__height - 1:
                xy += '\n'
        return xy

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        '''del'''
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
