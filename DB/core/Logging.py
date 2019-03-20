from config import log_file
from config import file_logging_level
from config import stream_logging_level
from config import logging_stdout
from config import logging_file
from config import logging_format

import logging

def get_logger(name: str=__name__, flevel=file_logging_level, slevel=stream_logging_level, stdout: bool=logging_stdout, fout: bool=logging_file, format: str=logging_format):
    '''
    An easier Logger object.
    Parameters:
    name: str, flevel: str or logging object, stdout: bool and format: str
    '''
    # Set the name of the logger
    logger = logging.getLogger(name)

    fhandler = logging.FileHandler(log_file)
    shandler = logging.StreamHandler()

    # Set the logging format and the file output handlers
    formatter = logging.Formatter(logging_format)

    shandler.setFormatter(formatter)
    fhandler.setFormatter(formatter)
    shandler.setLevel(slevel)
    fhandler.setLevel(flevel)

    # Add the handlers to the logger
    if stdout: logger.addHandler(shandler)
    if fout: logger.addHandler(fhandler)

    return logger

def set_level(logger, level: str = "INFO"):
    '''
    Sets the level of a logger from a string value of
    the wanted level.
    '''
    bypass = False
    if isinstance(level, str): level = level.lower()
    if isinstance(level, int): bypass = True
    if level == "debug" or bypass == True: logger.setLevel(logging.DEBUG)
    if level == "info" or bypass == True: logger.setLevel(logging.INFO)
    if level == "warning" or bypass == True: logger.setLevel(logging.WARNING)
    if level == "error" or bypass == True: logger.setLevel(logging.ERROR)
    if level == "critical" or bypass == True: logger.setLevel(logging.CRITICAL)
    return logger
