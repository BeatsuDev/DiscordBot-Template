from config import log_file
from config import file_logging_level
from config import stream_logging_level
from config import logging_stdout
from config import logging_file
from config import logging_format

import logging

logger = logging.getLogger()
print("\n\n\n\n-------------------------")
print(f"Type: {type(logger)}")
print(f"Logger: {logger}")
print("-------------------------\n\n\n\n")

class Logger(logger):
    def __init__(self, name: str=__name__, flevel=file_logging_level, slevel=stream_logging_level, stdout: bool=logging_stdout, fout: bool=logging_file, format: str=logging_format):
        '''
        An easier Logger object.
        Parameters:
        name: str, flevel: str or logging object, stdout: bool and format: str
        '''
        # Set the name of the logger
        if name: __super__().__init__(name)
        if not name: __super__().__init__("")

        self.fhandler = logging.FileHandler(log_file)
        self.shandler = logging.StreamHandler()

        # Set the logger level
        if level: setLevel(logger, level)

        # Set the logging format and the file output handlers
        formatter = logging.Formatter(logging_format)

        self.shandler.setFormatter(formatter)
        self.fhandler.setFormatter(formatter)
        self.setStreamLevel(logger, slevel)
        self.setFileLevel(logger, flevel)

        # Add the handlers to the logger
        if stdout: self.addHandler(shandler)
        if fout: self.addHandler(fhandler)


    def setFileLevel(self, level: str = "INFO"):
        '''
        Sets the level of a logger from a string value of
        the wanted level.
        '''
        level = level.lower()
        if level == "debug": self.fhandler.setLevel(logging.DEBUG)
        if level == "info": self.fhandler.setLevel(logging.INFO)
        if level == "warning": self.fhandler.setLevel(logging.WARNING)
        if level == "error": self.fhandler.setLevel(logging.ERROR)
        if level == "critical": self.fhandler.setLevel(logging.CRITICAL)

    def setStreamLevel(self, level: str = "INFO"):
        '''
        Sets the level of a logger from a string value of
        the wanted level.
        '''
        level = level.lower()
        if level == "debug": self.shandler.setLevel(logging.DEBUG)
        if level == "info": self.shandler.setLevel(logging.INFO)
        if level == "warning": self.shandler.setLevel(logging.WARNING)
        if level == "error": self.shandler.setLevel(logging.ERROR)
        if level == "critical": self.shandler.setLevel(logging.CRITICAL)
