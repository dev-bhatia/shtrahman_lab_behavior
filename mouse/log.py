import os
import sys
import logging
from datetime import datetime


class Logger:
    def __init__(self):
        """
        Create logging file for program.
        Reference: https://stackoverflow.com/a/28330410

        USE:
            Logger.log.info("Hello World")
            Logger.log.debug("Hello World")
            Logger.log.warning("Hello World")
            Logger.log.critical("Hello World")
            Logger.log.error("Hello World")

        :param name: (str) Name of logger, can be anything.
        """
        # Format Log File Name and Logging Style
        filename = datetime.now().strftime("%Y-%m-%d_%H:%M")
        formatter = logging.Formatter(fmt="%(asctime)s %(levelname)-8s - %(message)s",
                                      datefmt="%m-%d-%Y %I:%M:%S %p")
        # Idenitfy where Logs should be saved
        handler = logging.FileHandler("logs/{}.log".format(filename), mode='w')
        handler.setFormatter(formatter)
        screen_handler = logging.StreamHandler(stream=sys.stdout)
        screen_handler.setFormatter(formatter)
        logger = logging.getLogger("logfile")
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)
        logger.addHandler(screen_handler)
        self.log = logger
