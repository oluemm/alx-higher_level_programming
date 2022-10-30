#!/usr/bin/python3

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """Unittest for Square Class"""

    def test_update_square(self):
        s1 = Square(5)
        expected = "[Square] (89) 12/1 - 7"
        s1.update(size=7, id=89, x=12, y=1)
        self.assertEqual(expected,str(s1))