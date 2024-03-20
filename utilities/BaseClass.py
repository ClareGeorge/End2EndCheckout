import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def waitUntilElementIsDisplayed(self, pageelement):
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(By.XPATH, pageelement).is_displayed())

    # def getLogger(self):
    #
    #     loggerName = "Test Case: "+ inspect.stack()[1][3] + " LINE-NO: "+ str(inspect.stack()[1][2])
    #     self.logger = logging.getLogger(loggerName)
    #
    #     fileHandler = logging.FileHandler('logfile1.log')
    #     formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    #     fileHandler.setFormatter(formatter)
    #
    #     self.logger.addHandler(fileHandler)  # filehandler object
    #
    #     self.logger.setLevel(logging.DEBUG)
    #     return self.logger