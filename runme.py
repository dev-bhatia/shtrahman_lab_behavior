import os
import sys

# Custom Python
from mouse.log import Logger

x = Logger()
x.logfile.info("Hello World")
x.logfile.debug("Hello World")
x.logfile.warning("Hello World")
x.logfile.critical("Hello World")
x.logfile.error("Hello World")