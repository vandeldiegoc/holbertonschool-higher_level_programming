#!/usr/bin/python3
"""obj"""


class Student:
    """new class"""

    def __init__(self, first_name, last_name, age):
        """contructor"""
        self.first_namename = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return self dict"""
        return self.__dict__
