import golly as g


def calcwealth(l, j, w):
    i = 0
    while i < len(l[j]):
        w[j] += l[j][i[3]]
        i += 1
    return w


def getvonnuemann(x, y):
    c = [4]
    c[0] = [x+1, y]
    c[1] = [x, y+1]
    c[2] = [x-1, y]
    c[3] = [x, y-1]
    return c


def combat(a, d):


def getborders(l, j):
    b =[len(l[j])]
    g.note(str(len(b)))
    x = 0
    while x < (len(b) + 1):
        
        x += 1

def placeserfs(l):


def main(wea, h, l, f, d, g):


try:
    g.new("Feudalism Simulation")
    #User entered parameters for testing
    numRuns = int(g.getstring("Enter a number of iterations", "5000"))
    lords = int(g.getstring("Enter a number of Lords", "10"))
    width = lords * 10
    height = lords * 10
    #Lords [id of lord][array of land unit pairs in [0] is x [1] is y][wealth of lord]
    fiefs = [[0 for x in range(lords)]for x in range(width * height)]
    grain = [0 for x in range(lords)]
    #Array for storing the states and owners of the landunits
    landUnits = [[0 for x in range(width)] for x in range(height)]
    x = 0
    i = 0
    p = 0
    #Goes through each land unit to give it an initial state and owner
    #State 1 is farmable land
    #State 2 is occupied and normal production land
    #State 3 is occupied and underproducing land
    #State 4 is occupied and battle scarred land
    #State 5 is fought over land
    while x < width:
        y = 0
        j = 1
        while y < height:
            if y < (j * 10):
                landUnits[x][y] = [1, j, 100]
                fiefs[j][p] = [x, y]
                p += 1
            else:
                if j < (fiefs+1):
                    j += 1
                    landUnits[x][y] = [1, j, 100]
                    fiefs[j][p] = [x, y]
                    p += 1
            g.show("Expected: " + str(j) + ", Actual for " + str(x) + ", " + str(y) + ": " + str(landUnits[x][y][2]))
            g.note("fiefs " + str(j) + " at " + str(p) + " should be [" + str(x) + ", " + str(y) + "]")
            g.setcell(x, y, 1)
            y += 1
        x += 1
    g.update()
    while i < numRuns:
        g.show("In Main " + str(i))
        main(width, height, landUnits, fiefs, lords, grain)
        i += 1


finally:
    g.note("Goodbye")