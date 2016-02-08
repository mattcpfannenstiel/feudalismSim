class Army:
    def __init__(self):
        self.knightcount = 0
        self.uCost = 10
        self.bCost = 100


    def getknightcount(self):
        """
        Returns the number of Knights in the army
        """
        return self.knightcount


    def setknightcount(self, k):
        """
        Sets the number of Knights in the army
        """
        self.knightcount = k


    def getcost(self):
        """
        Returns the buy costs of Knights
        """
        return self.bCost


    def addknight(self):
        """
        Adds a knight to the army
        """
        self.knightcount += 1


    def killknight(self):
        """
        Takes a knight out of the army
        """
        self.knightcount -= 1


    def calculateupkeep(self):
        """
        Returns the upkeep cost of the army
        """
        return self.uCost * self.knightcount

