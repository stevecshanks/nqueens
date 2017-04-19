import unittest
from nqueens.queen import Queen
from nqueens.threat import Threat


class TestQueen(unittest.TestCase):

    def setUp(self):
        self.queen = Queen(1, 2)

    def testGetPosition(self):
        self.assertEqual(self.queen.getPosition(), (1, 2))

    def testGetThreat(self):
        self.assertEqual(self.queen.getThreat(), Threat.fromPosition(1, 2))

    def testIdentical(self):
        a = Queen(0, 0)
        b = Queen(0, 0)
        self.assertEqual(a, b)
