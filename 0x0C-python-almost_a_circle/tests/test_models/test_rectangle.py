"""class test"""

import sys
import os
import io
import contextlib
import unittest

from models.rectangle import Rectangle
from models.base import Base


class Test_Rectangle(unittest.TestCase):
    """test rectangle"""

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_id_1(self):
        """test id in rectangle"""
        rectangl = Rectangle(3, 4)
        rectangl_1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(rectangl.id, 14)
        self.assertEqual(rectangl_1.id, 12)

    def test_atribute_width_1(self):
        """test width"""
        w = Rectangle(1, 4)
        self.assertEqual(w.width, 1)

    def test_atribute_width_2(self):
        """test width"""
        with self.assertRaises(ValueError):
            Rectangle(-1, 4)

    def test_atribute_width_3(self):
        """test width"""
        with self.assertRaises(TypeError):
            Rectangle("-1", 4)

    def test_atribute_height_1(self):
        """test height"""
        h = Rectangle(1, 4)
        self.assertEqual(h.height, 4)

    def test_atribute_height_2(self):
        """test width"""
        with self.assertRaises(ValueError):
            Rectangle(1, -4)

    def test_atribute_height_3(self):
        """test width"""
        with self.assertRaises(TypeError):
            Rectangle(1, "-4")

    def test_atribute_x_1(self):
        """test width"""
        x1 = Rectangle(1, 4, 3)
        self.assertEqual(x1.x, 3)

    def test_atribute_x_2(self):
        """test width"""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -3)

    def test_atribute_x_2(self):
        """test width"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, ['1', '2'])

    def test_atribute_y_1(self):
        """test width"""
        y1 = Rectangle(1, 4, 3, 2)
        self.assertEqual(y1.y, 2)

    def test_atribute_y_2(self):
        """test width"""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -3, -2)

    def test_atribute_y_2(self):
        """test width"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 3, ('1', '2'))

    def test_area_1(self):
        """test area"""
        r = Rectangle(5, 5)
        self.assertEqual(r.area(), 25)

    def test_update_1(self):
        """test update"""
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (15) 10/10 - 10/10")

if __name__ == '__main__':
    unittest.main()
