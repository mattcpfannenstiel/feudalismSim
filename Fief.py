import random
from Gollyhandler import Gollyhandler

g = Gollyhandler()


class Fief:
    def __init__(self, fiefnum):
        self.fiefnumber = fiefnum
        self.atWar = False
        self.preparedForWar = False
        self.containedLand = []
        self.borders = []
        self.attackoptions = []

    def changewarstatus(self):
        """
        Changes at War status to at war or not at war
        """
        self.atWar = -self.atWar

    def changepreparedness(self):
        """
        Changes a fief preparedness to be either prepared for war or unprepared for war
        """
        self.preparedForWar = -self.preparedForWar

    def addland(self, LandUnit):
        """
        Adds land to the end of the contained land list
        """
        self.containedLand.append(LandUnit)

    def removeland(self, x, y):
        """
        Removes land from fiefs list
        """
        i = 0
        t = False
        while i < len(self.containedLand):
            if self.containedLand[i].gridloc.xloc == x and self.containedLand[i].gridloc.yloc == y:
                self.containedLand.pop(i)
            i += 1
            if t:
                break

    def findborders(self, fmap):
        """
        Looks through landunits and finds the ones that border other fiefdoms it then adds it to the bordering units list
        """
        g.toconsole("Finding Borders")
        i = 0
        while i < len(self.containedLand):
            c = self.containedLand[i].getvonneumann(fmap)
            g.toconsole("Found Von Neumann Neighborhood. Length is " + str(len(c)))
            j = 0
            while j < len(c):
                if c[j].owner.fiefnumber != self.fiefnumber:
                    g.toconsole("Found non member")
                    if -self.borders.__contains__(self.containedLand[i]):
                        self.borders.append(self.containedLand[i])
                        g.toconsole("Added to borders")
                    self.attackoptions.append(c[j])
                    g.toconsole("Added to attack options")
                j += 1
            i += 1

    def getfiefsize(self):
        return len(self.containedLand)

    def getattackoptions(self):
        return self.attackoptions

    def removeattackoption(self, x, y):
        """
        Removes attack option from the list after it has been used
        """
        i = 0
        t = False
        while i < len(self.attackoptions):
            if self.attackoptions[i].gridloc.xloc == x and self.attackoptions[i].gridloc.yloc == y:
                self.attackoptions.remove(i)
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
            g.toconsole("Placing serf")
            r = random.randint(0, (len(self.containedLand) - 1))
            if self.containedLand[r].full == False:
                self.containedLand[r].addserf()
                g.cellchange(self.containedLand[r].gridloc.xloc, self.containedLand[r].gridloc.yloc, 2)
                g.toconsole("Serf placed in " + str(self.containedLand[r].gridloc.xloc) +
                            ", " + str(self.containedLand[r].gridloc.yloc) + " by " + self.ruler.name)
                g.update()
                x = 1
            else:
                g.topopup("Land unit " + str(r) + " is full")

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
        g.toconsole(str(self.ruler.name) + " has " + str(self.stores.wealth) + " grain at his disposal")