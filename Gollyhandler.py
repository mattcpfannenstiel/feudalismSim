import golly as g


class Gollyhandler:
    """
    Handles all the Golly calls so that it wont have to be imported into the files that need it
    """

    def __init__(self):
        self.name = "FeudalSim"

    def topopup(self, text):
        g.note(text)

    def toconsole(self, text):
        g.show(text)

    def cellchange(self, x, y, state):
        g.setcell(x, y, state)

    def setstatecolors(self, state, r, gr, b):
        g.setcolors([state, r, gr, b])

    def setrule(self, text):
        g.setrule(text)

    def getuserinputint(self, text, default):
        temp = int(g.getstring(text, default))
        return temp

    def setsimname(self, text):
        g.new(text)

    def update(self):
        g.update()