#!/usr/bin/python3
"""this is the base """

import json


class Base:
    """this is the class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor method"""
        self.id = id
        if self.id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return string"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the JSON string """
        if json_string is None or json_string is "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes Json string in file"""
        name = "{}.json".format(cls.__name__)
        new_list = []
        if list_objs is not None:
            for i in list_objs:
                new_list.append(cls.to_dictionary(i))
        with open(name, mode='w')as wfile:
            wfile.write(cls.to_json_string(new_list))

    @classmethod
    def create(cls, **dictionary):
        """crete a new object"""
        if cls.__name__ == "Rectangle":
            from models.rectangle import Rectangle
            new = Rectangle(1, 1)
        if cls.__name__ == "Square":
            from models.square import Square
            new = Square(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """return lis of intancias"""
        namej = cls.__name__ + ".json"
        new_list = []
        try:
            with open(namej, 'r') as rfile:
                fjson = cls.from_json_string(rfile.read())
            for x in fjson:
                new_list.append(cls.create(**x))
            return new_list
        except:
            return new_list
