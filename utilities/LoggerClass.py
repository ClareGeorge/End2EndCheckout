
import inspect
import logging


class LoggerClass:
    def getLogger(self):

        loggerName = "Test Case: "+ inspect.stack()[1][3] + " LINE-NO: "+ str(inspect.stack()[1][2])
        self.logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        self.logger.addHandler(fileHandler)  # filehandler object

        self.logger.setLevel(logging.DEBUG)

        return self.logger
#
