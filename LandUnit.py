from Climate import Climate
from Location import Location


class LandUnit:
    """
    The basic unit that produces grain and houses serfs
    """
    SERF_MAX = 10
    PRODUCTION_VALUE = 50
    SERF_UPKEEP_COST = 5

    def __init__(self, x, y, fief):
        """
        Makes a new land unit
        :param x: the x location of the land unit on the map
        :param y: the y location of the land unit on the map
        :param fief: the fief that the land unit belongs to
        """
        self.farmable = True
        self.serfs = 0
        self.WEATHER = Climate()
        self.owner = fief
        self.full = False
        self.GRID_LOCATION = Location(x, y)


    def changeowner(self, newowner):
        """
        Changes the current owner of the land unit to the new owner
        """
        self.owner = newowner

    def getlandunit(self, x, y, fmap):
        """
        Returns the land unit from the x, y location from the map
        :return: sends back the landunit at that location
        """
        return fmap[x][y][2]

    def getproduction(self):
        """
        Return the production of the land unit
        :return: the production of the landunit
        """
        return self.PRODUCTION_VALUE * self.serfs

    def getupkeep(self):
        """
        Returns the upkeep of the landunit
        :return: the upkeep from multiplying number of serfs by their upkeep cost
        """
        return self.serfs * self.SERF_UPKEEP_COST

    def getvonneumann(self, fmap):
        """
        Looks in the land unit's Von Neumann Neighborhood and returns cells inside the map grid
        :param fmap: the map grid to reference from
        :return: the list of cells around the cell
        """
        c = []
        if (len(fmap) > self.GRID_LOCATION.xloc + 1 >= 0) and (0 <= self.GRID_LOCATION.yloc < len(fmap)):
            c.append(self.getlandunit(self.GRID_LOCATION.xloc + 1, self.GRID_LOCATION.yloc, fmap))
        if (len(fmap) > self.GRID_LOCATION.xloc >= 0) and (0 <= self.GRID_LOCATION.yloc + 1 < len(fmap)):
            c.append(self.getlandunit(self.GRID_LOCATION.xloc, self.GRID_LOCATION.yloc + 1, fmap))
        if (len(fmap) > self.GRID_LOCATION.xloc - 1 >= 0) and (0 <= self.GRID_LOCATION.yloc < len(fmap)):
            c.append(self.getlandunit(self.GRID_LOCATION.xloc - 1, self.GRID_LOCATION.yloc, fmap))
        if (len(fmap) > self.GRID_LOCATION.xloc >= 0) and (0 <= self.GRID_LOCATION.yloc - 1 < len(fmap)):
            c.append(self.getlandunit(self.GRID_LOCATION.xloc, self.GRID_LOCATION.yloc - 1, fmap))
        return c

    def addserf(self):
        """
        Adds a serf to the land unit unless the land unit is full
        """
        if self.serfs < self.SERF_MAX:
            self.serfs += 1
        else:
            self.full = True
