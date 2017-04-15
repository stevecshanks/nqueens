from nqueens.chessboard import Chessboard
from nqueens.printer import Printer


board = Chessboard.create(8)
board.placeQueen(4, 7)
board.placeQueen(1, 1)
board.placeQueen(2, 3)
printer = Printer.create(board)
printer.printBoard()
