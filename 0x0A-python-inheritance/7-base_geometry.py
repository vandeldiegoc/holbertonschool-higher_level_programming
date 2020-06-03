#!/usr/bin/python3
"""module that has a empty class"""


class BaseGeometry:

    def area(self):
        """raise Exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validator"""
        if type(value) is not int:
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')
