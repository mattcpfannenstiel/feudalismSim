import random

from Army import Army
from Logger import Logger


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

    def getlordnum(self):
        return self.lordnum

    def getserfs(self):
        return self.serfCount

    def prepared(self):
        return self.ready

    def decision(self):
        # 33% Chance to attack, buy, or do nothing each year
        r = random.randint(0, 98)
        if r < 33:
            if self.land.stores > 100:
                while self.land.stores > 100:
                    self.buyknight()
        if r >= 66:
            if self.combatants.getknightcount > 0:
                streak = 1
                while streak == 1:
                    y = random.randint(0, len(self.land.attackoptions))
                    streak = self.attack(self.land.attackoptions[y])
        else:
            if self.turn == 0:
                t = random.randint(0, len(self.land.containedLand))
                self.land.containedLand[t].placeserf()
                self.turn = -self.turn

    def attack(self, landUnit):
        # Sends troops into combat, determines the winner and either takes land or defends it
        lose = 0
        win = 1
        if self.combatants.getknightcount > landUnit.owner.combatants.getknightcount:
            landUnit.changeowner(self)
            self.land.containedLand.append(landUnit)
            landUnit.owner.land.containedLand.removeland(landUnit.gridloc.xloc, landUnit.gridloc.yloc)
            return win
        if self.combatants.getknightcount == landUnit.owner.combatants.getknightcount:
            r = random.randint(0, 99)
            if r > 49:
                landUnit.changeowner(self)
                self.land.containedLand.append(landUnit)
                landUnit.owner.land.containedLand.removeland(landUnit.gridloc.xloc, landUnit.gridloc.yloc)
                return win
            else:
                return lose
        else:
            return lose

    def buyknight(self):
        # Buys a knight and adds him to the army that the lord has at his disposal
        self.land.stores.setwealth(-self.combatants.getcost)
        if self.land.stores.getwealth() < 0:
            self.log.track("stores are less than zero", self.land.stores.getwealth(), True)
        self.combatants.addknight()
