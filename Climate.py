import random as r


class Climate:
    def __init__(self):
        self.growthmax = 300
        self.growthmin = 80
        self.growthdays = r.randint(self.growthmin, self.growthmax)


    def getgrowthdays(self):
        return self.growthdays