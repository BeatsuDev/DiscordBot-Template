from config import log_file
from config import file_logging_level
from config import stream_logging_level
from config import logging_stdout
from config import logging_file
from config import logging_format

import logging

class Logger(logging.Logger):
    def __init__(self, name: str=__name__, flevel=file_logging_level, slevel=stream_logging_level, stdout: bool=logging_stdout, fout: bool=logging_file, format: str=logging_format):
        '''
        An easier Logger object.
        Parameters:
        name: str, flevel: str or logging object, stdout: bool and format: str
        '''
        # Set the name of the logger
        if name: super().__init__(name)
        if not name: super().__init__("")

        self.fhandler = logging.FileHandler(log_file)
        self.shandler = logging.StreamHandler()

        # Set the logging format and the file output handlers
        self.formatter = logging.Formatter(logging_format)

        self.shandler.setFormatter(self.formatter)
        self.fhandler.setFormatter(self.formatter)
        self.setStreamLevel(slevel)
        self.setFileLevel(flevel)

        # Add the handlers to the logger
        if stdout: self.addHandler(self.shandler)
        if fout: self.addHandler(self.fhandler)


    def setFileLevel(self, level: str = "INFO"):
        '''
        Sets the level of a logger from a string value of
        the wanted level.
        '''
        bypass = False
        if isinstance(level, str): level = level.lower()
        if isinstance(level, int): bypass = True
        if level == "debug" or bypass == True: self.fhandler.setLevel(logging.DEBUG)
        if level == "info" or bypass == True: self.fhandler.setLevel(logging.INFO)
        if level == "warning" or bypass == True: self.fhandler.setLevel(logging.WARNING)
        if level == "error" or bypass == True: self.fhandler.setLevel(logging.ERROR)
        if level == "critical" or bypass == True: self.fhandler.setLevel(logging.CRITICAL)

    def setStreamLevel(self, level: str = "INFO"):
        '''
        Sets the level of a logger from a string value of
        the wanted level.
        '''
        bypass = False
        if isinstance(level, str): level = level.lower()
        if isinstance(level, int): bypass = True
        if level == "debug" or bypass == True: self.shandler.setLevel(logging.DEBUG)
        if level == "info" or bypass == True: self.shandler.setLevel(logging.INFO)
        if level == "warning" or bypass == True: self.shandler.setLevel(logging.WARNING)
        if level == "error" or bypass == True: self.shandler.setLevel(logging.ERROR)
        if level == "critical" or bypass == True: self.shandler.setLevel(logging.CRITICAL)
