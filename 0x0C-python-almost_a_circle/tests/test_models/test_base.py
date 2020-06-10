#!/usr/bin/python3
"""class test"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
import json
import pep8


class Test_Base(unittest.TestCase):
    """test base module"""

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_id_1(self):
        """test id with number"""
        base = Base(2)
        base_1 = Base(3)
        self.assertEqual(base.id, 2)
        self.assertEqual(base_1.id, 3)

    def test_id_2(self):
        """test if id is void"""
        Base._Base__nb_objects = 0
        base = Base()
        base_1 = Base()
        base_2 = Base()
        base_3 = Base()
        self.assertEqual(base.id, 1)
        self.assertEqual(base_1.id, 2)
        self.assertEqual(base_2.id, 3)

    def test_id_3(self):
        """test if id is a negative number"""
        base = Base(-1)
        self.assertEqual(base.id, -1)

    def test_id_4(self):
        """test if id is 0"""
        base = Base(0)
        self.assertEqual(base.id, 0)

    def test_json_to_string_1(self):
        """test  json to string"""
        dictionary = [{'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}]
        dictionary_1 = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        self.assertEqual(Base.to_json_string(dictionary), dictionary_1)

    def test_json_to_string_2(self):
        """test void to string"""
        dictionary = []
        dictionary_1 = '[]'
        self.assertEqual(Base.to_json_string(dictionary), dictionary_1)

    def test_save_to_file_1(self):
        """test if save to file"""
        r1 = Rectangle(4, 7, 2, 8)
        r2 = Rectangle(2, 10)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            rea = file.read()
        self.assertEqual(type(rea), str)

    def test_save_to_file_2(self):
        """test if save to file and is the same type"""
        r1 = Rectangle(4, 7, 2, 8)
        r2 = Rectangle(2, 10)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            rea = file.read()
        self.assertEqual(type(rea), str)

    def test_save_to_file_4(self):
        """empty if save ti file"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            rea = file.read()
        self.assertEqual(rea, '[]')

    def test_create_1(self):
        """create new intance"""
        r1 = Rectangle(5, 3, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual((r1 is r2), False)
        self.assertEqual((r1 == r2), False)
