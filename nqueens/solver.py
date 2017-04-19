class Solver:

    @staticmethod
    def create(board):
        return Solver(board)

    def __init__(self, board):
        self._board = board

    def solve(self):
        return self._tryToPlaceValidQueen(self._board)

    def _tryToPlaceValidQueen(self, solution):
        columns = self._getNonThreatenedList(solution.getThreatenedColumns())
        rows = self._getNonThreatenedList(solution.getThreatenedRows())
        for x in columns:
            for y in rows:
                if solution.isSafeQueenPosition(x, y):
                    solution.placeQueen(x, y)
                    if solution.getQueenCount() == solution.getSize():
                        return solution

                    newSolution = self._tryToPlaceValidQueen(solution)
                    if newSolution is not None:
                        return newSolution

                    solution.removeQueen(x, y)

        return None

    def _getNonThreatenedList(self, threatenedList):
        solutionRange = range(0, self._board.getSize())
        return [i for i in solutionRange if i not in threatenedList]
