from Climate import Climate
from Location import Location
xmax = 1000
ymax = 1000

class LandUnit:
    serfMax = 10
    productionvalue = 50
    upkeepcost = 5

    def __init__(self, x, y, fief):
        self.farmable = True
        self.serfs = 0
        self.weather = Climate()
        self.owner = fief
        self.full = False
        self.gridloc = Location(x, y)


    def changeowner(self, newowner):
        self.owner = newowner

    def getlandunit(self, x, y, fmap):
        return fmap[x][y][2]

    def getproduction(self):
        return self.productionvalue * self.serfs

    def getupkeep(self):
        return self.serfs * self.upkeepcost

    def getvonneumann(self, fmap):
        c = []
        if (len(fmap) > self.gridloc.xloc + 1 >= 0) and (0 <= self.gridloc.yloc < len(fmap)):
            c.append(self.getlandunit(self.gridloc.xloc + 1, self.gridloc.yloc, fmap))
        if (len(fmap) > self.gridloc.xloc >= 0) and (0 <= self.gridloc.yloc + 1 < len(fmap)):
            c.append(self.getlandunit(self.gridloc.xloc, self.gridloc.yloc + 1, fmap))
        if (len(fmap) > self.gridloc.xloc - 1 >= 0) and (0 <= self.gridloc.yloc < len(fmap)):
            c.append(self.getlandunit(self.gridloc.xloc - 1, self.gridloc.yloc, fmap))
        if (len(fmap) > self.gridloc.xloc >= 0) and (0 <= self.gridloc.yloc - 1 < len(fmap)):
            c.append(self.getlandunit(self.gridloc.xloc, self.gridloc.yloc - 1, fmap))
        return c

    def addserf(self):
        if self.serfs <= self.serfMax:
            self.serfs += 1
        else:
            self.full = True
