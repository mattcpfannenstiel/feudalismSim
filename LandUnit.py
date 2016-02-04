from Climate import Climate
from Location import Location
xmax = 1000
ymax = 1000

class LandUnit:
    serfMax = 10
    fmap = []
    productionvalue = 50
    upkeepcost = 5

    def __init__(self, x, y, fief):
        self.farmable = False
        self.serfs = 0
        self.weather = Climate()
        self.owner = fief
        self.full = False
        self.gridloc = Location(x, y)


    def changeowner(self, newowner):
        self.owner = newowner

    def getlandunit(self, x, y, fmap):
        self.fmap = fmap
        return fmap[x][y][2]

    def getproduction(self):
        return self.productionvalue * self.serfs

    def getupkeep(self):
        return self.serfs * self.upkeepcost

    def getvonneumann(self):
        c = []
        if (xmax > self.gridloc.xloc + 1 >= 0) and (0 <= self.gridloc.yloc < ymax):
            c.append(self.getlandunit(self.gridloc.xloc + 1, self.gridloc.yloc))
        if (xmax > self.gridloc.xloc >= 0) and (0 <= self.gridloc.yloc + 1 < ymax):
            c.append(self.getlandunit(self.gridloc.xloc, self.gridloc.yloc + 1))
        if (xmax > self.gridloc.xloc - 1 >= 0) and (0 <= self.gridloc.yloc < ymax):
            c.append(self.getlandunit(self.gridloc.xloc - 1, self.gridloc.yloc))
        if (xmax > self.gridloc.xloc >= 0) and (0 <= self.gridloc.yloc - 1 < ymax):
            c.append(self.getlandunit(self.gridloc.xloc, self.gridloc.yloc - 1))
        return c

    def addserf(self):
        self.serfs += 1
