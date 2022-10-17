import logging
from logging.handlers import TimedRotatingFileHandler


# creating a logger using getLogger method
def logg(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    handler = TimedRotatingFileHandler('timed.log', when='S', interval=1, backupCount=5)
    logFormatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(logFormatter)
    logger.addHandler(handler)
    return logger
