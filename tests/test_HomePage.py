import pytest

from e2ePytestSeleniumFlow.pageobjects.HomePage import HomePage
from e2ePytestSeleniumFlow.testdata.TestData import TestData
from e2ePytestSeleniumFlow.utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_HomePage(self,getTestData):
        self.driver.refresh()
        self.log.info("Starting Test test_HomePage")

        homepage = HomePage(self.driver)
        self.log.info("Navigated to Home Page")

        homepage.enterName(getTestData["name"])
        self.log.info("Entered Name " +  getTestData["name"])

        homepage.enterEmail(getTestData["email"])
        self.log.info("Entered Email" +  getTestData["email"])

        homepage.enterPassword(getTestData["password"])
        self.log.info("Entered Password" + getTestData["password"] )

        homepage.selectLove4Icecreams()
        self.log.info("selected  Love4Icecreams ")

        homepage.selectGender(getTestData["gender"])
        self.log.info("Entered gender" +  getTestData["gender"])

        homepage.clickSubmit()
        homepage.verifySuccessfulCompletion("Success! The Form has been submitted successfully!.")
        self.log.info(" verifeidSuccessfulCompletion")


        assert 1


    def test_HomePage2(self):
        self.log.info(" test_HomePage2")

@pytest.fixture(params=TestData.homepage_testdata)
def getTestData(request):
    return request.param

