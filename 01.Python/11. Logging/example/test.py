from logger import logging

def add(a, b):
    logging.debug(f"Adding {a} and {b}")
    return a + b

result = add(1, 2)
logging.info("Starting the program and the result is %s", result)
