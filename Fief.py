class Fief:
    def __init__(self, fiefnum):
        self.fiefnumber = fiefnum
        self.atWar = False
        self.preparedForWar = False
        self.containedLand = []
        self.borders = []
        self.attackoptions = []



    def changewarstatus(self):
        # Changes at War status
        self.atWar = -self.atWar

    def changepreparedness(self):
        # Changes a fief preparedness
        self.preparedForWar = -self.preparedForWar

    def addland(self, LandUnit):
        # adds land to the end of the contained land list
        self.containedLand.append(LandUnit)

    def removeland(self, x, y):
        # removes land from fiefs list
        i = 0
        t = False
        while i < len(self.containedLand):
            if self.containedLand[i].gridloc.xloc == x and self.containedLand[i].gridloc.yloc == y:
                self.containedLand.pop(i)
            i += 1
            if t:
                break

    def findborders(self):
        # Looks through landunits and finds the ones that border other fiefdoms it then adds
        i = 0
        while i < len(self.containedLand):
            c = self.containedLand[i].getvonneumann()
            j = 0
            while j < len(c):
                if c[j].owner is not self.ruler:
                    if -self.borders.__contains__(self.containedLand[i]):
                        self.borders.append(self.containedLand[i])
                    self.attackoptions.append(c[j])

    def getfiefsize(self):
        return len(self.containedLand)

    def getattackoptions(self):
        return self.attackoptions

    def removeattackoption(self, x, y):
        i = 0
        t = False
        while i < len(self.attackoptions):
            if self.attackoptions[i].gridloc.xloc == x and self.attackoptions[i].gridloc.yloc == y:
                self.attackoptions.remove(i)
            i += 1
            if t:
                break

    def getupkeep(self):
        i = 0
        cost = 0
        while i < len(self.containedLand):
            cost += self.containedLand[i].getupkeep
        return cost
