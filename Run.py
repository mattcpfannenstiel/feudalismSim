from Load import Load
from Gollyhandler import Gollyhandler

g = Gollyhandler()


class Run:
    def __init__(self):
        self.new = Load("feud")
        g.topopup("Now Loading")
        self.board = self.new.initialize()
        g.topopup("Loading done")
        i = 0
        while i < self.board[2]:
            cont = self.cycle()
            if cont == 1:
                break

    def cycle(self):
        # Goes through the yearly cycle for each lord
        i = 0
        while i < self.board[2]:
            lordturn = 0
            while lordturn < len(self.board[1]):
                if lordturn == 1:
                    self.board[1][lordturn].land.containedLand[0].addserf()
                    g.statechange(self.board[1][lordturn].land.containedLand[0].gridloc.xloc,
                                  self.board[1][lordturn].land.containedLand[0].gridloc.yloc, 2)
                    g.topopup(
                        "Serf placed in " + str(self.board[1][lordturn].land.containedLand[0].gridloc.xloc) + ", " +
                        str(self.board[1][lordturn].land.containedLand[0].gridloc.yloc) + " by " + self.board[1][
                            lordturn].name)
                    outcome = self.board[1][lordturn].simpleattack1on1(self.board[1][0])
                else:
                    self.board[1][lordturn].land.containedLand[0].addserf()
                    g.statechange(self.board[1][lordturn].land.containedLand[0].gridloc.xloc,
                                  self.board[1][lordturn].land.containedLand[0].gridloc.yloc, 2)
                    g.topopup(
                        "Serf placed in " + str(self.board[1][lordturn].land.containedLand[0].gridloc.xloc) + ", " +
                        str(self.board[1][lordturn].land.containedLand[0].gridloc.yloc) + " by " + self.board[1][
                            lordturn].name)
                    outcome = self.board[1][lordturn].simpleattack1on1(self.board[1][1])
                if outcome == 1:
                    g.topopup("Lord " + str(lordturn) + " wins")
                    return 1
                lordturn += 1
            i += 1
        return 0
