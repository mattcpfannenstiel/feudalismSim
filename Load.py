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
        # Displayed name of the simulation
        g.setsimname("Feudalism Simulation")

        # User entered parameters for testing
        runs = g.getuserinputint("Enter the number of iterations", "5000")
        lords = g.getuserinputint("Enter the number of lords that can be square rooted ", "2")
        landcount = g.getuserinputint("Enter the number of landunits per lord that can be square rooted", "1")
        height = lords * 10
        width = lords * 10

        # switches to a rule that has at least 5 states to use in Golly
        g.setrule("LifeHistory")

        # State 5 is fought over land and is red
        g.setstatecolors(5, 255, 0, 0)

        # State 4 is occupied and battle scarred land and is blue
        g.setstatecolors(4, 0, 0, 255)

        # State 3 is occupied and underproducing land and is yellow
        g.setstatecolors(3, 230, 216, 90)

        # State 2 is occupied and normal production land and is green
        g.setstatecolors(2, 0, 255, 0)

        # State 1 is farmable land and is white
        g.setstatecolors(1, 255, 255, 255)

        # Goes through each land unit to give it an initial state and initializes the board
        # Lords are also created with their given fiefs
        xmax = 1000
        ymax = 1000
        fmap = []
        fiefnum = 0
        lordslist = []
        # Boardstate set up as [fmap, lordslist, xmax, ymax]
        boardstate = []
        # Sets up landowner and state tracking map
        i = 0
        while i < xmax:
            j = 0
            fmap.append([])
            while j < ymax:
                fmap[i].append([])
                j += 1
            i +=1

        # Sets landunits into fiefs and fiefs into lords ownership
        y = 0
        while fiefnum < lords:
            x = 0
            fief = Fief(fiefnum)
            while x < landcount:
                land = LandUnit(x, y, fief)
                fief.containedLand.append(land)
                fmap[x][y].append(x)
                fmap[x][y].append(y)
                fmap[x][y].append(land)
                fmap[x][y].append(1)
                g.statechange(x, y, 1)
                x += 1
            grain = Grain(fief)
            fief.stores = grain
            lord = Lord("Lord " + str(fiefnum), fief)
            lord.land.ruler = lord
            lordslist.append(lord)
            fiefnum += 1
            y +=1
            g.update()
        boardstate.append(fmap)
        boardstate.append(lordslist)
        boardstate.append(runs)
        boardstate.append(xmax)
        boardstate.append(ymax)
        return boardstate