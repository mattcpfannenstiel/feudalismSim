class Army:
    def __init__(self):
        self.knightcount = 0
        self.uCost = 10
        self.bCost = 100


    def getknightcount(self):
        return self.knightcount


    def setknightcount(self, k):
        self.knightcount = k


    def getcost(self):
        return self.bCost


    def addknight(self):
        self.knightcount += 1


    def killknight(self):
        self.knightcount -= 1


    def calculateupkeep(self):
        return self.uCost * self.knightcount

