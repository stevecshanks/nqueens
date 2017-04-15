class Printer:

    @staticmethod
    def create(board):
        return Printer(board)

    def __init__(self, board):
        self.board = board

    def printBoard(self):
        self.printHeaderRow()
        for y in range(0, self.board.size):
            self.printRow(y)

    def printRow(self, y):
        self.output("|")
        for x in range(0, self.board.size):
            if self.board.hasQueen(x, y):
                self.printQueen()
            else:
                self.printEmptyCell()
            self.output("|")
        self.output("\n")
        self.printHeaderRow()

    def output(self, string):
        print(string, end='')

    def printHeaderRow(self):
        self.output("+")
        for i in range(0, self.board.size):
            self.output("---+")
        self.output("\n")

    def printEmptyCell(self):
        self.output("   ")

    def printQueen(self):
        self.output(" Q ")
