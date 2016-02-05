import random as r
from Army import Army
from Logger import Logger
from Gollyhandler import Gollyhandler

g = Gollyhandler()


class Lord:
    log = Logger("Lord")
    turn = 0

    def __init__(self, name, Fief):
        self.name = name
        self.serfCount = 0
        self.combatants = Army()
        self.ready = False
        self.land = Fief
        self.log.track(self.log.Name + ": " +
                       "\nLord's name: " + self.name +
                       "\nNumber of serfs on Fief: " + str(self.serfCount) +
                       "\nNumber of Knights: " + str(self.combatants.getknightcount()) +
                       "\nReady for War status: " + str(self.ready) +
                       "\nNumber of Fief: " + str(self.land.fiefnumber),
                       " ", False)

    def addserf(self):
        # Adds a serf to the number of serfs the Lord has
        self.serfCount += 1
        if self.serfCount < 0:
            self.log.track("serfcount less than zero", " ", False)

    def getname(self):
        return self.name

    def getserfs(self):
        return self.serfCount

    def prepared(self):
        return self.ready

    def decision(self):
        # 33% Chance to attack, buy, or place a serf
        g.topopup("In decision")
        j = r.randint(0, 98)
        if j < 33:
            self.log.track(" is buying knights", 0, False)
            if self.land.stores.getwealth() > 100:
                g.topopup("In buy phase for " + str(self.name))
                while self.land.stores.getwealth() > 100:
                    self.buyknight()
            g.topopup(str(self.name) + " now has " + str(self.combatants.getknightcount()) + " and " + str(
                      self.land.stores.getwealth()))
        if j >= 66:
            g.topopup("In combat phase")
            if self.combatants.getknightcount > 0:
                target = self.lookforwealthyland()
                g.statechange(target.gridloc.xloc, target.gridloc.yloc, 5)
                g.update()
                g.topopup(str(self.name) + " is attacking " + str(target.owner.ruler.name)
                          + " over land unit at " + str(target.gridloc.xloc) + ", " + str(target.gridloc.yloc))
                self.attack(target)
                g.statechange(target.gridloc.xloc, target.gridloc.yloc, 2)
                g.update()
        else:
            g.topopup("Waiting")

    def attack(self, landUnit):
        # Sends troops into combat, determines the winner and either takes land or defends it
        lose = 0
        win = 1
        if self.combatants.getknightcount() > landUnit.owner.ruler.combatants.getknightcount():
            landUnit.changeowner(self.land)
            self.land.containedLand.append(landUnit)
            landUnit.owner.removeland(landUnit.gridloc.xloc, landUnit.gridloc.yloc)
            g.topopup(str(self.name) + " wins the battle")
            return win
        if self.combatants.getknightcount() == landUnit.owner.ruler.combatants.getknightcount():
            i = r.randint(0, 99)
            if i > 49:
                landUnit.changeowner(self.land)
                self.land.containedLand.append(landUnit)
                landUnit.owner.removeland(landUnit.gridloc.xloc, landUnit.gridloc.yloc)
                g.topopup(str(self.name) + " wins the battle")
                return win
            else:
                g.topopup(str(landUnit.owner.ruler.name) + " wins the battle")
                return lose
        else:
            g.topopup(str(landUnit.owner.ruler.name) + " wins the battle")
            return lose

    def buyknight(self):
        # Buys a knight and adds him to the army that the lord has at his disposal
        if self.land.stores.getwealth() < 0:
            self.log.track("stores are less than zero", self.land.stores.getwealth(), True)
        else:
            self.land.stores.subtractwealth(self.combatants.getcost())
            self.combatants.addknight()

    def lookforwealthyland(self):
        i = 0
        temp = 0
        target = self.land.attackoptions[0]
        g.topopup("In wealthy lookup")
        while i < len(self.land.attackoptions):
            if temp < self.land.attackoptions[i].getproduction():
                temp = self.land.attackoptions[i].getproduction()
                target = self.land.attackoptions[i]
            i += 1
        g.topopup("Target is " + str(target.owner.ruler.name) +" at "+ str(target.gridloc.xloc) + ", " + str(target.gridloc.yloc))
        return target
