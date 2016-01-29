import golly as g
from Fief import Fief
from Grain import Grain
from LandUnit import LandUnit
from Lord import Lord


def main():
    # Displayed name of the simulation
    g.new("Feudalism Simulation")

    # User entered parameters for testing
    runs = int(g.getstring("Enter the number of iterations", "5000"))
    lords = int(g.getstring("Enter the number of lords", "100"))
    height = lords * 10
    width = lords * 10

    # switches to a rule that has at least 5 states to use in Golly
    g.setrule("LifeHistory")

    # State 5 is fought over land and is red
    g.setcolors([5, 255, 0, 0])

    # State 4 is occupied and battle scarred land and is blue
    g.setcolors([4, 0, 0, 255])

    # State 3 is occupied and underproducing land and is yellow
    g.setcolors([3, 230, 216, 90])

    # State 2 is occupied and normal production land and is green
    g.setcolors([2, 0, 255, 0])

    # State 1 is farmable land and is white
    g.setcolors([1, 255, 255, 255])

    # Goes through each land unit to give it an initial state and initializes the board
    # Lords are also created with their given fiefs
    tailx = 0
    taily = 0
    fiefnum = 0
    lordslist = []
    while fiefnum <= lords:
        l = 0
        fief = Fief(fiefnum)
        x = 0 + (tailx * 10)
        while tailx * 10 <= x < fiefnum * 10:
            y = 0 + (taily *10)
            while taily * 10 <= y < fiefnum * 10:
                land = LandUnit(x, y, fief)
                #land.map[x][y] = land
                fief.containedLand.append(land)
                g.setcell(x, y, 1)
                y += 1
            x += 1
        g.show("Lord " + str(fiefnum) + " is done")
        if fiefnum <= lords:
            fiefnum += 1
        tailx += 1
        if fiefnum%10 == 0:
            g.note("10 fiefs are done")
            taily += 1
            tailx = 0
        grain = Grain(fief)
        fief.stores = grain
        lord = Lord("Lord " + str(fiefnum), fief)
        lord.land.ruler = lord
        lordslist.append(lord)
        g.update()
    g.note("Setup done")

    # Goes through the yearly cycle for each lord
    i = 0
    while i < runs:
        lordturn = 1
        while lordturn <= lords:

            lordturn += 1
        i += 1

try:
    main()

finally:
    g.note("Goodbye")
