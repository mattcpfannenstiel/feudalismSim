from Load import Load
from Logger import Logger


class Run:
    """
    Handles the running of the simulation through its yearly cycles
    """
    log = Logger("Run", "Low")

    def __init__(self):
        self.new = Load("Feudalism Simulation")
        self.log.tracktext("Now Loading")
        self.board = self.new.initialize()
        self.log.tracktext("Loading done")
        cont = 1
        while cont == 1:
            cont = self.cycle()
        self.log.tracktext("Simulation complete")


    def cycle(self):
        """
        Goes through the turn for each lord for every year
        :return: a zero when the number of runs is complete
        """

        i = 0
        while i < self.board[2]:
            self.log.trackconsoleonly("Yearly cycle", i)
            lordturn = 0
            while lordturn < len(self.board[1]):
                fate = self.board[1][lordturn].checkifdead()
                if fate:
                    self.log.tracktext(str(self.board[1][lordturn].name) + " is defeated")
                    self.board[1][lordturn].pop()
                self.board[1][lordturn].land.calculatewealth()
                self.board[1][lordturn].land.placeserf()
                self.board[1][lordturn].land.findborders(self.board[0])
                self.board[1][lordturn].decision()
                lordturn += 1
            i += 1
        return 0
