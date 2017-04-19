from nqueens.queen import Queen
from nqueens.threat import Threat


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
        return Threat.fromPosition(x, y) not in self.getUniqueThreats()

    def isValid(self):
        # If the number of unique threats doesn't match the number of queens,
        # then two or more queens must be threatening each other
        return len(self.getUniqueThreats()) == len(self._queens)

    def getThreatenedColumns(self):
        threatenedColumns = []
        for queen in self._queens:
            if queen.x not in threatenedColumns:
                threatenedColumns.append(queen.x)
        return threatenedColumns

    def getThreatenedRows(self):
        threatenedRows = []
        for queen in self._queens:
            if queen.y not in threatenedRows:
                threatenedRows.append(queen.y)
        return threatenedRows

    def getUniqueThreats(self):
        threats = []
        for queen in self._queens:
            if queen.getThreat() not in threats:
                threats.append(queen.getThreat())
        return threats
