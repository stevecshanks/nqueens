import unittest
from nqueens.chessboard import Chessboard
from nqueens.printer import Printer
from unittest.mock import MagicMock


class TestPrinter(unittest.TestCase):

    def setUp(self):
        self.standardBoard = Chessboard.create(8)
        self.printer = Printer.create(self.standardBoard)
        self.printer.printEmptyCell = MagicMock()
        self.printer.printQueen = MagicMock()
        self.printer.output = MagicMock()

    def testSimplePrint(self):
        self.printer.printBoard()
        self.assertEqual(self.printer.printEmptyCell.call_count, 8 * 8)

    def testQueenPrint(self):
        self.standardBoard.placeQueen(1, 1)
        self.standardBoard.placeQueen(3, 5)
        self.printer.printBoard()
        self.assertEqual(self.printer.printEmptyCell.call_count, 8 * 8 - 2)
        self.assertEqual(self.printer.printQueen.call_count, 2)

    def testPrintedRowCount(self):
        # This will confuse our row count, so have it do nothing
        self.printer.printHeaderRow = MagicMock()
        
        self.printer.printBoard()
        newline_count = 0
        for call in self.printer.output.mock_calls:
            args = call[1]
            if '\n' in args[0]:
                newline_count += 1
        self.assertEqual(newline_count, 8)
