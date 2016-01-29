class Location:
    def __init__(self, x, y):
        self.xloc = x
        self.yloc = y


    def getx(self):
        return self.xloc


    def gety(self):
        return self.yloc


    def setx(self, x):
        self.xloc = x


    def sety(self, y):
        self.yloc = y


    def tostring(self):
        return "x: " + str(self.xloc) + " y: " + str(self.yloc)