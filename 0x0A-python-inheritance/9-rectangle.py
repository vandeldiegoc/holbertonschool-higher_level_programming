#!/usr/bin/python3
"""module that has a empty class"""


class BaseGeometry:
    """class empty"""
    pass

    def area(self):
        """raise Exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validator"""
        if type(value) is not int:
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')


class Rectangle(BaseGeometry):
    """new class"""

    def __init__(self, width, height):
        """constructor"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """area"""
        return (self.__width * self.__height)

    def __str__(self):
        """print"""
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
