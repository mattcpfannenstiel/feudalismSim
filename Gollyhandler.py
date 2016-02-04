import golly as g


class Gollyhandler:

    def __init__(self):
        self.name = "FeudalSim"

    def topopup(self, text):
        g.note(text)

    def toconsole(self, text):
        g.show(text)

    def statechange(self, x, y, state):
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