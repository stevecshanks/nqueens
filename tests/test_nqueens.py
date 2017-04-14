import unittest
from nqueens.chessboard import Chessboard


class TestNQueens(unittest.TestCase):

    def setUp(self):
        self.standardBoard = Chessboard.create(8)

    def testCreateOk(self):
        self.assertEqual(self.standardBoard.size, 8)

    def testCreateInvalid(self):
        with self.assertRaises(ValueError):
            board = Chessboard.create(0)

    def testHasQueenOk(self):
        self.assertFalse(self.standardBoard.hasQueen(0, 0))

    def testBoundaries(self):
        boundary_positions = [(0, 0), (0, 7), (7, 0), (7, 7)]
        for pos in boundary_positions:
            with self.subTest(pos=pos):
                self.assertFalse(self.standardBoard.hasQueen(pos[0], pos[1]))

    def testInvalidPositions(self):
        invalid_positions = [(-1, -1), (-1, 0), (0, -1), (8, 0), (0, 8),
                             (8, 8)]
        for pos in invalid_positions:
            with self.subTest(pos=pos):
                with self.assertRaises(ValueError):
                    self.standardBoard.hasQueen(pos[0], pos[1])

    def testPlaceQueens(self):
        self.standardBoard.placeQueen(1, 1)
        self.standardBoard.placeQueen(2, 2)
        self.assertTrue(self.standardBoard.hasQueen(1, 1))
        self.assertTrue(self.standardBoard.hasQueen(2, 2))

    def testPlaceDuplicateQueen(self):
        self.standardBoard.placeQueen(1, 1)
        with self.assertRaises(ValueError):
            self.standardBoard.placeQueen(1, 1)

    def testValidateEmpty(self):
        self.assertFalse(self.standardBoard.isValid())

    def testValidateSimple(self):
        board = Chessboard.create(1)
        self.assertFalse(board.isValid())
        board.placeQueen(0, 0)
        self.assertTrue(board.isValid())

    def testValidateHorizontal(self):
        board = Chessboard.create(2)
        self.assertFalse(board.isValid())
        board.placeQueen(0, 0)
        board.placeQueen(1, 0)
        self.assertFalse(board.isValid())

    def testValidateVertical(self):
        board = Chessboard.create(2)
        self.assertFalse(board.isValid())
        board.placeQueen(0, 0)
        board.placeQueen(0, 1)
        self.assertFalse(board.isValid())

    def testValidateDiagonalRight(self):
        board = Chessboard.create(2)
        self.assertFalse(board.isValid())
        board.placeQueen(0, 0)
        board.placeQueen(1, 1)
        self.assertFalse(board.isValid())

    def testValidateDiagonalLeft(self):
        board = Chessboard.create(2)
        self.assertFalse(board.isValid())
        board.placeQueen(1, 0)
        board.placeQueen(0, 1)
        self.assertFalse(board.isValid())
