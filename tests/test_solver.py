import unittest
from nqueens.chessboard import Chessboard
from nqueens.solver import Solver


class TestSolver(unittest.TestCase):

    def setUp(self):
        self.standardBoard = Chessboard.create(8)

    def testSimpleSolution(self):
        board = Chessboard.create(1)
        solver = Solver.create(board)
        solution = solver.solve()
        self.assertIsNotNone(solution)
        self.assertEqual(solution.getSize(), 1)
        self.assertTrue(solution.hasQueen(0, 0))
        self.assertTrue(solution.isValid())

    def testImpossible(self):
        board = Chessboard.create(2)
        solver = Solver.create(board)
        solution = solver.solve()
        self.assertIsNone(solution)

    def runTestFor(self, n):
        board = Chessboard.create(n)
        solver = Solver.create(board)
        solution = solver.solve()
        self.assertIsNotNone(solution)
        self.assertEqual(solution.getQueenCount(), n)
        self.assertTrue(solution.isValid())

    # Useful to have a quick-running but still reasonably-sized test
    def testSmall(self):
        self.runTestFor(6)

    @unittest.skip("Too slow")
    def testStandard(self):
        self.runTestFor(8)
