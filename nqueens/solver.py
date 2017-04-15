class Solver:

    @staticmethod
    def create(board):
        return Solver(board)

    def __init__(self, board):
        self._board = board

    def solve(self):
        return self._tryToPlaceValidQueen(self._board)

    def _tryToPlaceValidQueen(self, solution):
        if solution.getQueenCount() == solution.getSize():
            if solution.isValid():
                return solution
            else:
                return None

        for x in range(0, solution.getSize()):
            for y in range(0, solution.getSize()):
                if not solution.hasQueen(x, y):
                    solution.placeQueen(x, y)
                    if (solution.isValid()):
                        newSolution = self._tryToPlaceValidQueen(solution)
                        if newSolution is not None:
                            return newSolution
                    solution.removeQueen(x, y)

        return None
