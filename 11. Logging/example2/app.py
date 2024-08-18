import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArithmiticApp")

def add(x, y):
    logger.info(f"Adding {x} and {y} to get {x + y}")
    return x + y

def subtract(x, y):
    logger.info(f"Subtracting {y} from {x} to get {x - y}")
    return x - y

def multiply(x, y):
    logger.info(f"Multiplying {x} and {y} to get {x * y}")
    return x * y

def divide(x, y):
    logger.info(f"Dividing {x} by {y} to get {x / y}")
    return x / y


# call the functions
logger.info("Program started")
add(1, 2)
subtract(2, 1)
multiply(2, 3)
divide(6, 3)