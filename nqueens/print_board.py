from nqueens.chessboard import Chessboard
from nqueens.printer import Printer
from nqueens.solver import Solver


board = Chessboard.create(8)
solver = Solver.create(board)
solution = solver.solve()
if solution is not None:
    printer = Printer.create(solution)
    printer.printBoard()
