import unittest
from nqueens.chessboard import Chessboard


class TestNQueens(unittest.TestCase):

    def setUp(self):
        self.standardBoard = Chessboard.create(8)

    def testCreateOk(self):
        self.assertEqual(self.standardBoard.size, 8)

    def testCreateInvalid(self):
        try:
            board = Chessboard.create(0)
            self.fail("Invalid board size did not raise exception")
        except ValueError:
            pass

    def testHasQueenOk(self):
        self.assertFalse(self.standardBoard.hasQueen(0, 0))

    def testBoundaries(self):
        boundary_positions = [(0, 0), (0, 7), (7, 0), (7, 7)]
        for pos in boundary_positions:
            self.assertFalse(self.standardBoard.hasQueen(pos[0], pos[1]))

    def testInvalidPositions(self):
        invalid_positions = [(-1, -1), (-1, 0), (0, -1), (8, 0), (0, 8),
                             (8, 8)]
        for pos in invalid_positions:
            try:
                self.standardBoard.hasQueen(pos[0], pos[1])
                self.fail("Invalid hasQueen did not throw exception")
            except ValueError:
                pass

    def testPlaceQueens(self):
        self.standardBoard.placeQueen(1, 1)
        self.standardBoard.placeQueen(2, 2)
        self.assertTrue(self.standardBoard.hasQueen(1, 1))
        self.assertTrue(self.standardBoard.hasQueen(2, 2))
