#!/usr/bin/python3

import unittest
from models.base import Base
import json
from models.rectangle import Rectangle
from models.square import Square
import os




class Test_Base(unittest.TestCase):
    """test base module"""

    def test_id_1(self):
        base = Base(2)
        base_1 = Base(3)
        self.assertEqual(base.id, 2)
        self.assertEqual(base_1.id, 3)

    def test_id_2(self):
        base = Base()
        base_1 = Base()
        base_2 = Base()
        base_3 = Base()
        self.assertEqual(base.id, 1)
        self.assertEqual(base_1.id, 2)
        self.assertEqual(base_2.id, 3)
    
    def test_id_3(self):
        base = Base(-1)
        self.assertEqual(base.id, -1)

    def test_id_4(self):
        base = Base(0)
        self.assertEqual(base.id, 0)


    
    def test_json_to_string_1(self):
        dictionary = [{'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}]
        dictionary_1 = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        self.assertEqual(Base.to_json_string(dictionary), dictionary_1)

    def test_json_to_string_2(self):
        dictionary = []
        dictionary_1 = '[]'
        self.assertEqual(Base.to_json_string(dictionary), dictionary_1)

    def test_json_to_string_3(self):
        dictionary = [{'id': 1, 'width': '10', 'height': 7, 'x': 2, 'y': 8}]
        dictionary_1 = '[{"id": 1, "width": "10", "height": 7, "x": 2, "y": 8}]'
        self.assertEqual(Base.to_json_string(dictionary), dictionary_1)

    def test_json_to_string_3(self):
        dictionary = [{'id': 1, 'width': '10', 'height': 7, 'x': 2, 'y': 8}]
        self.assertEqual(type(Base.to_json_string(dictionary)), <class 'str'>)


