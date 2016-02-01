class Grain:
    def __init__(self, fief):
        self.surplus = False
        self.wealth = 0
        self.upkeep = 0
        self.store = fief

    def addwealth(self, w):
        self.wealth += w

    def subtractwealth(self, s):
        self.wealth -= s

    def getwealth(self):
        return self.wealth

    def setwealth(self, w):
        self.wealth = w

    def atsurplus(self):
        return self.surplus

    def getupkeep(self):
        return self.upkeep

    def setupkeep(self):
        self.upkeep = self.store.ruler.army.calculateupkeep() + self.store.calculateupkeep()
