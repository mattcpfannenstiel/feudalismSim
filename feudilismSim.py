from random import random

import golly as g
NULL = 999

def calcwealth(fiefs, jnum, grain):
    i = 0
    while i < len(fiefs[j]):
        if (fiefs[jnum][i][0] and fiefs[jnum][i][1]) != NULL:
            grain[jnum] += fiefs[jnum][i][2]
        i += 1
    return grain


def getvonnuemann(x, y):
    c = [4]
    c[0] = [x+1, y]
    c[1] = [x, y+1]
    c[2] = [x-1, y]
    c[3] = [x, y-1]
    return c


def combat(attacker, defender, ja, jb):



    return winner

def getborders(fiefs, jnum, size):
    b =[size]
    x = 0
    u = 0
    while x < (len(b) + 1):
        if (fiefs[jnum][x][0] and fiefs[jnum][x][1]) != NULL:
            c = getvonnuemann(fiefs[jnum][x][0], fiefs[jnum][x][1])
            y = 0
            while y < len(c + 1):
                if jnum != c[y][1]:
                    b[u] = c[y]
                    u += 1
                y +=1
        x += 1
    return b


def placeserfs(fiefs, landUnits, runs, size):
    #places serfs on random landUnits within each feif every 2 years
    f = len(fiefs)
    if runs%2 ==0:
        x = 0
        while x < (f+1):
            g = random(size)
            if (fiefs[x][g][0] and fiefs[x][g][1])!= NULL:
                landUnits[fiefs[x][g][0]][fiefs[x][g][1]][2] = 100
            x +=1
    return landUnits


def main(width, height, landunits, fiefs, grain):
    lords = [10]

    return 0


try:
    g.new("Feudalism Simulation")
    global NULL
    #User entered parameters for testing
    numRuns = int(g.getstring("Enter a number of iterations", "5000"))
    lords = 10
    width = lords * 10
    height = lords * 10
    #Lords [id of lord][array of land unit pairs in [0] is x [1] is y][wealth of lord]
    fiefs = [[NULL for x in range(lords)]for x in range(width * height)]
    grain = [0 for x in range(lords)]
    #Array for storing the states and owners of the landunits
    landUnits = [[0 for x in range(width)] for x in range(height)]
    x = 0
    runs = 0
    p = 0
    #Goes through each land unit to give it an initial state and owner
    #List of 3 at each x, y coordinate are
    #State in the first position
    #Variable j represents the Lord Number that owns a landUnit in the second
    #Grain per year in the third
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
                landUnits[x][y] = [1, j-1, 0]
                fiefs[j-1][p] = [x, y]
                p += 1
            else:
                if j < (fiefs+1):
                    j += 1
                    landUnits[x][y] = [1, j-1, 0]
                    fiefs[j-1][p] = [x, y]
                    p += 1
            g.show("Expected: " + str(j-1) + ", Actual for " + str(x) + ", " + str(y) + ": " + str(landUnits[x][y][1]))
            g.note("fiefs " + str(j-1) + " at " + str(p) + " should be [" + str(x) + ", " + str(y) + "]")
            g.setcell(x, y, 1)
            y += 1
        x += 1
    g.update()
    while runs < numRuns:
        g.show("In Main " + str(runs))
        main(width, height, landUnits, fiefs, grain, runs)
        runs += 1


finally:
    g.note("Goodbye")