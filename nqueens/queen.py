from nqueens.threat import Threat


class Queen:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getPosition(self):
        return (self.x, self.y)

    def getThreat(self):
        return Threat.fromPosition(self.x, self.y)

    def __repr__(self):
        return "Queen(" + str(self.x) + ", " + str(self.y) + ")"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
