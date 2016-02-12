import math
from Gollyhandler import Gollyhandler
from Fief import Fief
from Grain import Grain
from LandUnit import LandUnit
from Lord import Lord
from Logger import Logger



class Load():
    """
    Creates the map grid and sets up the lords for the simulation
    """
    log = Logger("Load", "Low")
    g = Gollyhandler()

    def __init__(self, Name):
        """
        Makes a new load of the simulation and gets user input for variables
        :param Name: Name of the simulation
        """
        self.name = Name
        self.g.setsimname(self.name)

        # Parameters of the simulation for testing purposes
        self.runs = self.g.getuserinputint("Enter the number of iterations", "5000")
        self.lords = self.g.getuserinputint("Enter the number of lords that can be square rooted(Max 100)", "4")
        self.landcount = self.g.getuserinputint("Enter the number of landunits per lord that can be square rooted(Max 100)", "4")
        self.height = math.sqrt(self.landcount) * math.sqrt(self.lords)
        self.width = math.sqrt(self.landcount) * math.sqrt(self.lords)

        # Sets Golly into a rule set with 8 states to work with
        self.g.setrule("LifeHistory")

        # Sets Golly to the position view of the x and y coordinates in the center
        self.g.setpos(x, y)

        # State 5 is fought over land and is red
        self.g.setstatecolors(5, 255, 0, 0)


        # State 4 is occupied and battle scarred land and is blue
        self.g.setstatecolors(4, 0, 0, 255)


        # State 3 is occupied and underproducing land and is yellow
        self.g.setstatecolors(3, 230, 216, 90)


        # State 2 is occupied and normal production land and is green
        self.g.setstatecolors(2, 0, 255, 0)

        # State 1 is farmable land and is white
        self.g.setstatecolors(1, 255, 255, 255)


    def initialize(self):
        """
        Sets up the entire state of the board to the user's specifications
        :return: the state of the board including the map, lords, number of years to go through,
        and width and height of the map
        """

        #Goes through each land unit to give it an initial state and initializes the board
        #Lords are also created with their given fiefs
        fiefnum = 0
        startpointx = 0
        startpointy = 0
        lordslist = []
        sidelength = int(math.sqrt(self.landcount))
        lordside = int(math.sqrt(self.lords))
        sidemod = lordside
        if lordside < 2:
            sidemod = lordside - 1
        if lordside % 2 == 1:
            sidemod += 1

        # Sets up landowner and state tracking map
        fmap = self.makemap(self.width, self.height)

        # Sets landunits into fiefs and fiefs into lords ownership
        x = 0
        while fiefnum < self.lords:
            self.log.tracktext("Fiefnum is " + str(fiefnum) + "\nSidemod is " + str(sidemod) + "\nSidelength is " + str(sidelength))
            if fiefnum == 0:
                self.log.tracktext("Starting fief construction")
            elif fiefnum >= lordside:
                if fiefnum % sidemod == 0:
                    startpointx = 0
                    x = startpointx
                    startpointy += sidelength
                else:
                    startpointx += sidelength
                    x = startpointx
            else:
                startpointx += sidelength
                x = startpointx
            fief = Fief(fiefnum)
            while x < startpointx + sidelength:
                y = 0 + startpointy
                while y < startpointy + sidelength:
                    self.populatemap(fief, fmap, x, y, fiefnum)
                    y += 1
                x += 1
            grain = Grain(fief)
            fief.stores = grain
            lord = Lord("Lord " + str(fiefnum), fief)
            lord.land.ruler = lord
            lordslist.append(lord)
            fiefnum += 1
            self.g.update()
        boardstate = self.makeboardstate(fmap, lordslist, self.runs, self.width, self.height)
        self.log.tracktext("Board Creation done")
        return boardstate

    def makemap(self, width, height):
        """
        Makes the map based on the height and width made by the user input
        :param width: square root of the number of lords multiplied by the
        square root of the number of land units per fief
        :param height: square root of the number of lords multiplied by the
        square root of the number of land units per fief
        :return: the created map of the simulation
        """
        fmap = []
        self.log.tracktext("Start map")
        i = 0
        while i < width:
            j = 0
            fmap.append([])
            while j < height:
                fmap[i].append([])
                j += 1
            i += 1
        self.log.tracktext("Map made")
        return fmap

    def makeboardstate(self, fmap, lordslist, runs, width, height):
        """
        Puts all the parameters created in the initialization into a list to be easily referenced
        :param fmap: map of the land units and their state
        :param lordslist: a list including all the lords in the simulation
        :param runs: number years to simulate
        :param width: x size of the simulation
        :param height: y size of the simulation
        :return: a list including all the given parameters
        """
        # Boardstate set up as [fmap, lordslist, runs, width, height]
        boardstate = []
        boardstate.append(fmap)
        boardstate.append(lordslist)
        boardstate.append(runs)
        boardstate.append(width)
        boardstate.append(height)
        return boardstate

    def populatemap(self, fief, fmap, x, y, fiefnum):
        """
        Takes all the given information and adds it to the map and fiefs, then updates the board in Golly to match
        :param fief: the fief the new land unit is being added to
        :param fmap: the map that is updated with new information
        :param x: x location on the map
        :param y: y location on the map
        :param fiefnum: the number of the fief that is being delt with(also the lord's number)
        """
        self.log.tracktext("Lord " + str(fiefnum) + " landunit at " + str(x) + ", " + str(y))
        land = LandUnit(x, y, fief)
        fief.containedLand.append(land)
        fmap[x][y].append(x)
        fmap[x][y].append(y)
        fmap[x][y].append(land)
        fmap[x][y].append(1)
        self.g.cellchange(x, y, 1)