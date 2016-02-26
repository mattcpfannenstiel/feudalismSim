import random as r
from Army import Army
from Logger import Logger
view = False

if(view == True):
    from Gollyhandler import Gollyhandler
    g = Gollyhandler()


class Lord:
    """
    Lords are the main players in the simulation and make all the decisions such as attacking, buying knights, waiting
    or placing a serf.
    """
    log = Logger("Lord", "High")
    turn = 0

    def __init__(self, name, Fief):
        """
        Makes a new lord
        :param name: the name of the lord
        :param Fief: the fief that he rules over
        """
        self.name = name
        self.serfCount = 0
        self.combatants = Army()
        self.ready = False
        self.land = Fief
        self.log.tracktext(self.log.Name + ": " +
                       "\nLord's name: " + self.name +
                       "\nNumber of serfs on Fief: " + str(self.serfCount) +
                       "\nNumber of Knights: " + str(self.combatants.getknightcount()) +
                       "\nReady for War status: " + str(self.ready))

    def addserf(self):
        """
        Adds a serf to the number of serfs the Lord has
        """
        self.serfCount += 1
        if self.serfCount < 0:
            self.log.tracktext("serfcount less than zero")

    def getname(self):
        """
        Returns the name
        """
        return self.name

    def getserfs(self):
        """
        Gets the number of serfs on the Fief
        """
        return self.serfCount

    def prepared(self):
        """
        Returns the boolean ready
        """
        return self.ready

    def decision(self):
        """
        33% Chance to attack, buy, or wait
        Governs the decision mechanism of the Lords (Decision Rule)
        Lords attack the most productive land unit nearby
        """
        self.log.tracktext("In decision")
        j = r.randint(0, 98)
        if j < 33:
            self.log.tracknum(self.name + " is buying knights", self.combatants.getknightcount())
            if self.land.stores.getwealth() > 100:
                self.log.tracktext("In buy phase for " + str(self.name))
                while self.land.stores.getwealth() > 100:
                    self.buyknight()
            self.log.tracktext(str(self.name) + " now has " + str(self.combatants.getknightcount()) + " and " + str(
                      self.land.stores.getwealth()))
        if j >= 66:
            self.log.tracktext("In combat phase")
            if self.combatants.getknightcount > 0:
                target = self.lookforwealthyland()
                if target is not None:
                    if view:
                        g.cellchange(target.GRID_LOCATION.xloc, target.GRID_LOCATION.yloc, 5)
                        g.update()
                    self.log.tracktext(str(self.name) + " is attacking " + str(target.owner.ruler.name)
                          + " over land unit at " + str(target.GRID_LOCATION.xloc) + ", " + str(target.GRID_LOCATION.yloc))
                    self.land.removeattackoption(target.GRID_LOCATION.xloc, target.GRID_LOCATION.yloc)
                    self.attack(target)
                    if view:
                        g.cellchange(target.GRID_LOCATION.xloc, target.GRID_LOCATION.yloc, 2)
                        g.update()
                else:
                    self.log.tracktext("No target available")
        else:
            self.log.tracktext("Waiting")

    def attack(self, landUnit):
        """
        Sends troops into combat, determines the winner and either takes land or defends it
        Rule that governs the battles and decides combat by numbers but if they have the same number of knights
        the battle is decided by a coin flip
        :param landUnit: the land unit that is being targeted by the lord
        """

        if self.combatants.getknightcount() > landUnit.owner.ruler.combatants.getknightcount():
            landUnit.changeowner(self.land)
            self.land.containedLand.append(landUnit)
            landUnit.owner.removeland(landUnit.GRID_LOCATION.xloc, landUnit.GRID_LOCATION.yloc)
            self.log.tracktext(str(self.name) + " wins the battle")
        if self.combatants.getknightcount() == landUnit.owner.ruler.combatants.getknightcount():
            i = r.randint(0, 99)
            if i > 49:
                landUnit.changeowner(self.land)
                self.land.containedLand.append(landUnit)
                landUnit.owner.removeland(landUnit.GRID_LOCATION.xloc, landUnit.GRID_LOCATION.yloc)
                self.log.tracktext(str(self.name) + " wins the battle")
            else:
                self.log.tracktext(str(landUnit.owner.ruler.name) + " wins the battle")
        else:
            self.log.tracktext(str(landUnit.owner.ruler.name) + " wins the battle")


    def buyknight(self):
        """
        Buys a knight and adds him to the army that the lord has at his disposal
        """
        if self.land.stores.getwealth() < 0:
            self.log.tracknum("stores are less than zero", self.land.stores.getwealth())
        else:
            self.land.stores.subtractwealth(self.combatants.getcost())
            self.combatants.addknight()

    def lookforwealthyland(self):
        """
        Looks for the most productive land unit from the fief's attack options and returns it
        """
        i = 0
        temp = 0
        if len(self.land.attackoptions) != 0:
            target = self.land.attackoptions[0]
            self.log.tracktext("In wealthy lookup")
            while i < len(self.land.attackoptions):
                if temp < self.land.attackoptions[i].getproduction():
                    temp = self.land.attackoptions[i].getproduction()
                    target = self.land.attackoptions[i]
                i += 1
            self.log.tracktext("Target is " + str(target.owner.ruler.name) +" at "+ str(target.GRID_LOCATION.xloc) +
                               ", " + str(target.GRID_LOCATION.yloc))
            return target
        else:
            return None

    def checkifdead(self):
        """
        Checks to see if a lord has any land left
        :return: true means he is defeated, false means he gets to fight on
        """
        if len(self.land.containedLand) == 0:
            return True
        else:
            return False