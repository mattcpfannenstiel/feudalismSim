import random
from Logger import Logger





class Fief:
    """
    This class is for land management and wealth tracking for a lord
    """
    log = Logger("Fief", "High")
    protected_blue = [90]
    protected_green = [216]
    protected_red = [230]

    def __init__(self, fiefnum):
        """
        Makes a new fief
        :param fiefnum: the number of the fief that should match the lord number
        :return:
        """
        self.fiefnumber = fiefnum
        self.atWar = False
        self.preparedForWar = False
        self.containedLand = []
        self.borders = []
        self.attackoptions = []
        self.ruler = None
        self.stores = None
        self.red = None
        self.green = None
        self.blue = None
        self.color = [self.red, self.green, self.blue]

    def changewarstatus(self):
        """
        Changes at War status to at war or not at war
        """
        self.atWar = not self.atWar

    def changepreparedness(self):
        """
        Changes a fief preparedness to be either prepared for war or unprepared for war
        """
        self.preparedForWar = not self.preparedForWar

    def addland(self, LandUnit):
        """
        Adds land to the end of the contained land list
        :param LandUnit: the landunit to be added
        """
        self.containedLand.append(LandUnit)

    def removeland(self, x, y):
        """
        Removes land from fiefs list
        :param x: the x location of the target landunit
        :param y: the y location of the target landunit
        """
        i = 0
        t = True
        while t:
            while i < len(self.containedLand):
                if self.containedLand[i].GRID_LOCATION.xloc == x and self.containedLand[i].GRID_LOCATION.yloc == y:
                    self.containedLand.pop(i)
                    t = False
                i += 1

    def findborders(self, fmap):
        """
        Looks through landunits and finds the ones that border other fiefdoms it then adds it to the bordering units list
        """
        self.log.tracktext("Finding Borders")
        i = 0
        while i < len(self.containedLand):
            c = self.containedLand[i].getvonneumann(fmap)
            self.log.tracktext("Found Von Neumann Neighborhood. Length is " + str(len(c)))
            j = 0
            while j < len(c):
                if c[j].owner.fiefnumber != self.fiefnumber:
                    self.log.tracktext("Found non member")
                    if -self.borders.__contains__(self.containedLand[i]):
                        self.borders.append(self.containedLand[i])
                        self.log.tracktext("Added to borders")
                    self.attackoptions.append(c[j])
                    self.log.tracktext("Added to attack options")
                j += 1
            i += 1

    def getfiefsize(self):
        return len(self.containedLand)

    def getattackoptions(self):
        return self.attackoptions

    def removeattackoption(self, x, y):
        """
        Removes attack option from the list after it has been used
        :param x: the x location of the target landunit
        :param y: the y location of the target landunit
        """
        i = 0
        t = False
        while i < len(self.attackoptions):
            if self.attackoptions[i].GRID_LOCATION.xloc == x and self.attackoptions[i].GRID_LOCATION.yloc == y:
                self.attackoptions.pop(i)
            i += 1
            if t:
                break

    def findupkeep(self):
        """
        Finds the upkeep for all the serfs on a fief (serfs multiplied by upkeep cost)
        """
        i = 0
        cost = 0
        while i < len(self.containedLand):
            cost += self.containedLand[i].getupkeep()
        return cost

    def placeserf(self):
        """
        Places serf on a random land unit in the fief that isn't full (10 serfs is full)
        """
        x = 0
        while x == 0:
            self.log.tracktext("Placing serf")
            r = random.randint(0, (len(self.containedLand) - 1))
            if self.containedLand[r].full == False:
                self.containedLand[r].addserf()
                g.cellchange(self.containedLand[r].GRID_LOCATION.xloc, self.containedLand[r].GRID_LOCATION.yloc, 2)
                self.log.tracktext("Serf placed in " + str(self.containedLand[r].GRID_LOCATION.xloc) +
                                   ", " + str(self.containedLand[r].GRID_LOCATION.yloc) + " by " + self.ruler.name)
                g.update()
                x = 1
            if self.alllandfull():
                x = 1
            else:
                self.log.tracktext("Land unit " + str(r) + " is full")

    def calculatewealth(self):
        """
        Calculates wealth on entire fief
        Rule that governs wealth calculation based on land unit production
        """
        i = 0
        final = 0
        while i < len(self.containedLand):
            temp = self.containedLand[i].getproduction()
            temp = (temp - self.containedLand[i].getupkeep())
            final += temp
            i += 1
        final = final - self.ruler.combatants.calculateupkeep()
        self.stores.wealth += final
        self.log.tracktext(str(self.ruler.name) + " has " + str(self.stores.wealth) + " grain at his disposal")

    def alllandfull(self):
        """
        Checks to see if all land in a fief is full of serfs
        :return: true for all landunits full and false for room to be utilized
        """
        self.log.tracktext("Got into all land full?")
        self.log.tracktext("Contained land has " + str(len(self.containedLand)) + " land units in it")
        if len(self.containedLand) != 0:
            i = 0
            while i < len(self.containedLand):
                if not self.containedLand[i].full:
                    self.log.tracktext("All good")
                    return False
                else:
                    self.log.tracktext("Shouldn't show again")
                    return True
        else:
            self.log.tracktext("No land")
            return True
