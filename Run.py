from Load import Load
from Gollyhandler import Gollyhandler

g = Gollyhandler()


class Run:
    def __init__(self):
        self.new = Load("feud")
        g.toconsole("Now Loading")
        self.board = self.new.initialize()
        g.toconsole("Loading done")
        i = 0
        while i < self.board[2]:
            cont = self.cycle()
            if cont == 1:
                break

    def cycle(self):
        # Goes through the yearly cycle for each lord
        g.topopup("Cycle")
        i = 0
        while i < self.board[2]:
            lordturn = 0
            while lordturn < len(self.board[1]):
                self.board[1][lordturn].land.calculatewealth()
                self.board[1][lordturn].land.placeserf()
                self.board[1][lordturn].land.findborders(self.board[0])
                self.board[1][lordturn].decision()

                lordturn += 1
            i += 1
        return 0
