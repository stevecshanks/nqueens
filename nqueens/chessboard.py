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
        self.queenPositions.append((x, y))
