class Chessboard:

    @staticmethod
    def create(size):
        if (size > 0):
            return Chessboard(size)
        else:
            raise ValueError("Board must have size > 0")

    def __init__(self, size):
        self.size = size
        self.queenPositions = []

    def raiseErrorIfPositionIsInvalid(self, x, y):
        if (x < 0 or x >= self.size or y < 0 or y >= self.size):
            raise ValueError(str(x) + ", " + str(y) + " is outside board")

    def hasQueen(self, x, y):
        self.raiseErrorIfPositionIsInvalid(x, y)
        return (x, y) in self.queenPositions

    def placeQueen(self, x, y):
        self.raiseErrorIfPositionIsInvalid(x, y)
        if (x, y) in self.queenPositions:
            raise ValueError("Attempted to place queen in non-empty space")
        self.queenPositions.append((x, y))

    def isValid(self):
        attackedRows = []
        attackedColumns = []
        for pos in self.queenPositions:
            col = pos[0]
            row = pos[1]

            if row in attackedRows:
                return False
            attackedRows.append(row)

            if col in attackedColumns:
                return False
            attackedColumns.append(col)

            if self.hasDiagonalClash(col, row, -1):
                return False
            if self.hasDiagonalClash(col, row, 1):
                return False

        return True

    def hasDiagonalClash(self, x, y, direction):
        x = x + direction
        y = y + 1

        if y >= self.size:
            return False
        if (x < 0 or x >= self.size):
            return False

        if self.hasQueen(x, y):
            return True
        else:
            return self.hasDiagonalClash(x, y, direction)
