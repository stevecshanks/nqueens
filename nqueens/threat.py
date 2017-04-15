class Diagonal:

    @staticmethod
    def fromPosition(x, y):
        return Diagonal(x, y)

    def __init__(self, x, y):
        # If you followed this point diagonally to the top of the board, what
        # would the resulting columns be?
        self._leftX = x - y
        self._rightX = x + y

    def __eq__(self, other):
        return self._leftX == other._leftX or self._rightX == other._rightX

    def __repr__(self):
        return "Diagonal(" + str(self._leftX) + ", 0)"
