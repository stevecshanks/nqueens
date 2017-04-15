import unittest
from nqueens.diagonal import Diagonal


class TestDiagonal(unittest.TestCase):

    def testIdentical(self):
        a = Diagonal.fromPosition(0, 0)
        b = Diagonal.fromPosition(0, 0)
        self.assertEqual(a, b)

    def testDifferent(self):
        a = Diagonal.fromPosition(0, 0)
        b = Diagonal.fromPosition(0, 2)
        self.assertTrue(a != b)

    def testRealDiagonalLeft(self):
        a = Diagonal.fromPosition(4, 4)
        b = Diagonal.fromPosition(3, 3)
        c = Diagonal.fromPosition(5, 5)
        self.assertEqual(a, b)
        self.assertEqual(a, c)

    def testRealDiagonalRight(self):
        a = Diagonal.fromPosition(4, 4)
        b = Diagonal.fromPosition(5, 3)
        c = Diagonal.fromPosition(3, 5)
        self.assertEqual(a, b)
        self.assertEqual(a, c)
