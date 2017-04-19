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
        self._queenPositions = []

    def getSize(self):
        return self._size

    def getQueenCount(self):
        return len(self._queenPositions)

    def raiseErrorIfPositionIsInvalid(self, x, y):
        if (x < 0 or x >= self._size or y < 0 or y >= self._size):
            raise ValueError(str(x) + ", " + str(y) + " is outside board")

    def hasQueen(self, x, y):
        self.raiseErrorIfPositionIsInvalid(x, y)
        return (x, y) in self._queenPositions

    def placeQueen(self, x, y):
        self.raiseErrorIfPositionIsInvalid(x, y)
        if (x, y) in self._queenPositions:
            raise ValueError("Attempted to place queen in non-empty space")
        self._queenPositions.append((x, y))

    def removeQueen(self, x, y):
        self.raiseErrorIfPositionIsInvalid(x, y)
        if (x, y) in self._queenPositions:
            self._queenPositions.remove((x, y))
        else:
            raise ValueError("Attempted to remove queen from empty space")

    def isSafeQueenPosition(self, x, y):
        return Threat.fromPosition(x, y) not in self.getUniqueThreats()

    def isValid(self):
        # If the number of unique threats doesn't match the number of queens,
        # then two or more queens must be threatening each other
        return len(self.getUniqueThreats()) == len(self._queenPositions)

    def getThreatenedColumns(self):
        threatenedColumns = []
        for pos in self._queenPositions:
            if pos[0] not in threatenedColumns:
                threatenedColumns.append(pos[0])
        return threatenedColumns

    def getThreatenedRows(self):
        threatenedRows = []
        for pos in self._queenPositions:
            if pos[1] not in threatenedRows:
                threatenedRows.append(pos[1])
        return threatenedRows

    def getUniqueThreats(self):
        threats = []
        for pos in self._queenPositions:
            threat = Threat.fromPosition(pos[0], pos[1])
            if threat not in threats:
                threats.append(threat)
        return threats
