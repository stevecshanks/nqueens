import unittest
from nqueens.threat import Threat


class TestThreat(unittest.TestCase):

    def testIdentical(self):
        a = Threat.fromPosition(0, 0)
        b = Threat.fromPosition(0, 0)
        self.assertEqual(a, b)

    def testDifferent(self):
        a = Threat.fromPosition(0, 0)
        b = Threat.fromPosition(1, 2)
        self.assertTrue(a != b)

    def testEqualHorizonatal(self):
        a = Threat.fromPosition(0, 0)
        b = Threat.fromPosition(1, 0)
        self.assertEqual(a, b)

    def testEqualVertical(self):
        a = Threat.fromPosition(0, 6)
        b = Threat.fromPosition(4, 6)
        self.assertEqual(a, b)

    def testEqualThreatLeft(self):
        a = Threat.fromPosition(4, 4)
        b = Threat.fromPosition(3, 3)
        c = Threat.fromPosition(5, 5)
        self.assertEqual(a, b)
        self.assertEqual(a, c)

    def testEqualThreatRight(self):
        a = Threat.fromPosition(4, 4)
        b = Threat.fromPosition(5, 3)
        c = Threat.fromPosition(3, 5)
        self.assertEqual(a, b)
        self.assertEqual(a, c)
