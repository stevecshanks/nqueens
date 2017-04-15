import unittest
from nqueens.chessboard import Chessboard
from nqueens.solver import Solver


class TestSolver(unittest.TestCase):

    def setUp(self):
        self.solver = Solver.create()

    def testSimpleSolution(self):
        board = Chessboard.create(1)
        solution = self.solver.solve(board)
        self.assertIsNotNone(solution)
        self.assertEqual(solution.size, 1)
        self.assertTrue(solution.hasQueen(0, 0))
        self.assertTrue(solution.isValid())

    def testImpossible(self):
        board = Chessboard.create(2)
        solution = self.solver.solve(board)
        self.assertIsNone(solution)

    def runTestFor(self, n):
        board = Chessboard.create(n)
        solution = self.solver.solve(board)
        self.assertIsNotNone(solution)
        self.assertEqual(len(solution.queenPositions), n)
        self.assertTrue(solution.isValid())

    # Useful to have a quick-running but still reasonably-sized test
    def testSmall(self):
        self.runTestFor(6)

    # def testStandard(self):
    #     self.runTestFor(8)
