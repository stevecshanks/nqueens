from nqueens.queen import Queen


class Chessboard:

    @staticmethod
    def create(size):
        if (size > 0):
            return Chessboard(size)
        else:
            raise ValueError("Board must have size > 0")

    def __init__(self, size):
        self._size = size
        self._queens = []

    def getSize(self):
        return self._size

    def getQueenCount(self):
        return len(self._queens)

    def raiseErrorIfPositionIsInvalid(self, x, y):
        if (x < 0 or x >= self._size or y < 0 or y >= self._size):
            raise ValueError(str(x) + ", " + str(y) + " is outside board")

    def hasQueen(self, x, y):
        self.raiseErrorIfPositionIsInvalid(x, y)
        return Queen(x, y) in self._queens

    def placeQueen(self, x, y):
        self.raiseErrorIfPositionIsInvalid(x, y)
        if Queen(x, y) in self._queens:
            raise ValueError("Attempted to place queen in non-empty space")
        self._queens.append(Queen(x, y))

    def removeQueen(self, x, y):
        self.raiseErrorIfPositionIsInvalid(x, y)
        if Queen(x, y) in self._queens:
            self._queens.remove(Queen(x, y))
        else:
            raise ValueError("Attempted to remove queen from empty space")

    def isSafeQueenPosition(self, x, y):
        return Queen(x, y).getThreat() not in self.getThreats()

    def isValid(self):
        for queen in self._queens:
            other_threats = [q.getThreat() for q in self._queens if q != queen]
            if queen.getThreat() in other_threats:
                return False

        return True

    def getThreatenedColumns(self):
        return [queen.x for queen in self._queens]

    def getThreatenedRows(self):
        return [queen.y for queen in self._queens]

    def getThreats(self):
        return [queen.getThreat() for queen in self._queens]
