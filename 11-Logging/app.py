import logging

##logging settings:
logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H-%M-%S',
    handlers=[
        logging.FileHandler('app2.log'),
        logging.StreamHandler()
    ]
)

logger=logging.getLogger("ArithmeticApp")

def add(a,b):
    result=a+b
    logger.debug(f"Adding {a} and {b} = {result}")
    return result

def sub(a,b):
    result=a-b
    logger.debug(f"Subtracting {a} and {b} = {result}")
    return result

def mult(a,b):
    result=a*b
    logger.debug(f"Multiplying {a} and {b} = {result}")
    return result

def div(a,b):
    try:
        result=a/b
        logger.debug(f"Dividing {a} by {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error.")
        return None
    
add(2,3)
sub(56,7)
mult(3,8)
div(81,9)