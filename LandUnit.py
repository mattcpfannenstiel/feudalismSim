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
        """
        Changes the current owner of the land unit to the new owner
        """
        self.owner = newowner

    def getlandunit(self, x, y, fmap):
        """
        Returns the land unit from the x, y location from the map
        """
        return fmap[x][y][2]

    def getproduction(self):
        """
        Return the production of the land unit
        """
        return self.productionvalue * self.serfs

    def getupkeep(self):
        return self.serfs * self.upkeepcost

    def getvonneumann(self, fmap):
        """
        Looks in the land unit's Von Neumann Neighborhood and returns cells inside the map grid
        """
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
        """
        Adds a serf to the land unit unless the land unit is full
        """
        if self.serfs < self.serfMax:
            self.serfs += 1
        else:
            self.full = True
