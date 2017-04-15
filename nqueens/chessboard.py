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

    def isValid(self):
        if len(self.getThreatenedColumns()) != len(self._queenPositions):
            return False
        if len(self.getThreatenedRows()) != len(self._queenPositions):
            return False

        for pos in self._queenPositions:
            col = pos[0]
            # Since one queen must be above the other to attack diagonally, we
            # only need to check for downward clashes
            row = pos[1] + 1
            if self.hasDiagonalClash(col, row, -1):
                return False
            if self.hasDiagonalClash(col, row, 1):
                return False

        return True

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

    def hasDiagonalClash(self, x, y, direction):
        x = x + direction

        if y >= self._size:
            return False
        if (x < 0 or x >= self._size):
            return False

        if self.hasQueen(x, y):
            return True
        else:
            return self.hasDiagonalClash(x, y + 1, direction)
