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
        allQueensPlaced = len(self.queenPositions) == self.size
        if not allQueensPlaced:
            return False

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

            leftColToTest = col
            rightColToTest = col
            for rowToTest in range(row + 1, self.size):
                leftColToTest -= 1
                rightColToTest += 1
                if leftColToTest >= 0:
                    if self.hasQueen(leftColToTest, rowToTest):
                        return False
                if rightColToTest < self.size:
                    if self.hasQueen(rightColToTest, rowToTest):
                        return False

        return True
