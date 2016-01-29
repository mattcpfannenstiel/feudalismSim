import logging


class Logger:
    logging.basicConfig(filename='debug.log', level=logging.DEBUG)
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

    def __init__(self, name):
        self.Name = name
        self.text = " "

    def track(self, text, number, numq):
        # For tracking messages or messages with numbers
        if numq == False:
            logging.debug(self.Name + ": " + text)
        else:
            logging.debug(self.Name + ": " + text + " " + number)

    def errorcatch(self, var1name, num1, var2name, num2):
        # For errors in expected values
        if num1 != num2:
            logging.critical(self.Name + ": " + var1name + ": " + num1 + " doesn't equal " + var2name + ": " + num2)
