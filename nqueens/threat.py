class Threat:

    @staticmethod
    def fromPosition(x, y):
        return Threat(x, y)

    def __init__(self, x, y):
        self._actualX = x
        self._actualY = y
        # If you followed this point diagonally to the top of the board, what
        # would the resulting columns be?
        self._diagonalLeftX = x - y
        self._diagonalRightX = x + y

    def __eq__(self, other):
        return (self._actualX == other._actualX or
                self._actualY == other._actualY or
                self._diagonalLeftX == other._diagonalLeftX or
                self._diagonalRightX == other._diagonalRightX)

    def __repr__(self):
        return "Threat(" + str(self._actualX) + ", " + str(self._actualY) + ")"
