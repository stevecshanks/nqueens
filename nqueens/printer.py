class Printer:

    @staticmethod
    def create(board):
        return Printer(board)

    def __init__(self, board):
        self._board = board
        self._shading = False

    def printBoard(self):
        self.printHeaderRow()
        for y in range(0, self._board.getSize()):
            self.printRow(y)

    def printRow(self, y):
        self.output("|")
        for x in range(0, self._board.getSize()):
            if self._board.hasQueen(x, y):
                self.printQueen()
            else:
                self.printEmptyCell()
            self.output("|")
        self.output("\n")
        self.printHeaderRow()

    @staticmethod
    def output(string):
        print(string, end='')

    def printHeaderRow(self):
        self.output("+")
        for _ in range(0, self._board.getSize()):
            self.output("----+")
        self.output("\n")

    def printEmptyCell(self):
        self.output("    ")

    def printQueen(self):
        self.output(" Qu ")
