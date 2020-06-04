#!/usr/bin/python3
"""obj"""


class Student:
    """new class"""

    def __init__(self, first_name, last_name, age):
        """contructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        "return new dict"""
        new = {}
        if attrs is None:
            return self.__dict__
        else:
            for i in attrs:
                if i in self.__dict__:
                    new[i] = self.__dict__[i]
            return new
