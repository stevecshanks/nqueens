class Solver:

    @staticmethod
    def create():
        return Solver()

    def solve(self, board):
        return self.tryToPlaceValidQueen(board)

    def tryToPlaceValidQueen(self, solution):
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
                        newSolution = self.tryToPlaceValidQueen(solution)
                        if newSolution is not None:
                            return newSolution
                    solution.removeQueen(x, y)

        return None
