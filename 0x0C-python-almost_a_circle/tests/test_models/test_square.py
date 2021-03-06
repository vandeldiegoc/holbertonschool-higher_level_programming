"""class test"""

import sys
import os
import unittest
import io
import pep8
import contextlib
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class Test_Square(unittest.TestCase):
    """test square"""

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_size_1(self):
        """test size"""
        s = Square(10)
        self.assertEqual(s.size, 10)

    def test_size_2(self):
        """test size"""
        with self.assertRaises(ValueError):
            Square(0)

    def test_size_3(self):
        """test size"""
        with self.assertRaises(TypeError):
            Square("0")

    def test_update_1(self):
        """test update"""
        s = Square(10, 10, 10, 10)
        self.assertEqual(str(s), "[Square] (10) 10/10 - 10")

if __name__ == '__main__':
    unittest.main()
