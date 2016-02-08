import math
from Gollyhandler import Gollyhandler
from Fief import Fief
from Grain import Grain
from LandUnit import LandUnit
from Lord import Lord

g = Gollyhandler()


class Load():
    def __init__(self, Name):
        self.name = Name

    def initialize(self):
        """
        Displayed name of the simulation
        """
        g.setsimname("Feudalism Simulation")

        """
        Max size of hight and width
        """
        xmax = 1000
        ymax = 1000

        """
        User entered parameters for testing
        """
        runs = g.getuserinputint("Enter the number of iterations", "5000")
        lords = g.getuserinputint("Enter the number of lords that can be square rooted(Max 100)", "4")
        landcount = g.getuserinputint("Enter the number of landunits per lord that can be square rooted(Max 100)", "4")
        height = math.sqrt(landcount) * math.sqrt(lords)
        width = math.sqrt(landcount) * math.sqrt(lords)

        """
        Switches to a rule that has at least 5 states to use in Golly
        """
        g.setrule("LifeHistory")

        """
        State 5 is fought over land and is red
        """
        g.setstatecolors(5, 255, 0, 0)

        """
        State 4 is occupied and battle scarred land and is blue
        """
        g.setstatecolors(4, 0, 0, 255)

        """
        State 3 is occupied and underproducing land and is yellow
        """
        g.setstatecolors(3, 230, 216, 90)

        """
        State 2 is occupied and normal production land and is green
        """
        g.setstatecolors(2, 0, 255, 0)

        """
        State 1 is farmable land and is white
        """
        g.setstatecolors(1, 255, 255, 255)

        """
        Goes through each land unit to give it an initial state and initializes the board
        Lords are also created with their given fiefs
        """
        fmap = []
        fiefnum = 0
        startpointx = 0
        startpointy = 0
        lordslist = []
        sidelength = int(math.sqrt(landcount))

        """
        Boardstate set up as [fmap, lordslist, xmax, ymax]
        """
        boardstate = []

        """
        Sets up landowner and state tracking map
        """
        g.toconsole("Start map")
        i = 0
        while i < width:
            j = 0
            fmap.append([])
            while j < height:
                fmap[i].append([])
                j += 1
            i += 1
        g.toconsole("Map made")

        """
        Sets landunits into fiefs and fiefs into lords ownership
        """
        x = 0
        while fiefnum < lords:
            if fiefnum == 0:
                g.toconsole("Starting fief construction")
            elif fiefnum >= sidelength:
                if fiefnum % (sidelength + 1) == 0:
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
                    g.toconsole("Lord " + str(fiefnum) + " landunit at " + str(x) + ", " + str(y))
                    land = LandUnit(x, y, fief)
                    fief.containedLand.append(land)
                    fmap[x][y].append(x)
                    fmap[x][y].append(y)
                    fmap[x][y].append(land)
                    fmap[x][y].append(1)
                    g.cellchange(x, y, 1)
                    y += 1
                x += 1
            grain = Grain(fief)
            fief.stores = grain
            lord = Lord("Lord " + str(fiefnum), fief)
            lord.land.ruler = lord
            lordslist.append(lord)
            fiefnum += 1
            g.update()
        boardstate.append(fmap)
        boardstate.append(lordslist)
        boardstate.append(runs)
        boardstate.append(width)
        boardstate.append(height)
        g.toconsole("Board Creation done")
        return boardstate
