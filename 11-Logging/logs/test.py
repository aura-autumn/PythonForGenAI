import logging
import logger

def add(a,b):
    logging.debug("Addition is happening.")
    return a+b

logging.debug("The addition function is called.")
add(56785,746)