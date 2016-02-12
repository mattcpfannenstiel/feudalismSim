import logging
from Gollyhandler import Gollyhandler


class Logger:
    """
    Tracks messages for the console, popup windows and the log
    """
    logging.basicConfig(filename='debug.log', level=logging.DEBUG)
    g = Gollyhandler()
    POPUP = False
    LOG = False
    CONSOLE = True

    def __init__(self, name, level):
        """
        Makes a new Logger
        :param name: name of the class being logged
        :param level: level of log to be output to
        """
        self.Name = name
        self.level = "low"


    def tracknum(self, text, number):
        """
        Logs text with a number for output
        :param text: text to be put in the message
        :param number: number to be put in the message
        """
        # For log tracking, popping up, or printing out messages with numbers
        if self.CONSOLE:
            self.g.toconsole(text + " " + str(number))
        if self.POPUP:
            self.g.topopup(text + " " + str(number))
        if self.LOG:
            logging.debug(self.Name + ": " + text + " " + str(number))

    def tracktext(self, text):
        """
        Logs text only for output
        :param text: text to be output
        """
        # For log tracking, popping up, or printing out messages
        if self.CONSOLE:
            self.g.toconsole(text)
        if self.POPUP:
            self.g.topopup(text)
        if self.LOG:
            logging.debug(text)

    def trackconsoleonly(self, text, num):
        """
        For printing to the console in Golly only
        :param text: text to be output
        :param num: number to be output
        """
        self.g.toconsole(text + " " + str(num))
