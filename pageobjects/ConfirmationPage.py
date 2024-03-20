from selenium.webdriver.common.by import By


class ConfirmationPage:

    shiptocountry = (By.ID, "country")
    country_element = "//div[@class='suggestions']/ul/li/a[text()='India']"
    country_element1 = (By.XPATH,"//div[@class='suggestions']/ul/li/a[text()='India']")
    termsandconditions = (By.XPATH, "//*[contains(text(), 'I agree')]")
    purchasebtn = (By.XPATH, "//input[@value='Purchase']")
    confirmmessage = (By.XPATH, "//*[contains(text(), 'Success')]")

    def __init__(self, driver):
        self.driver = driver

    def searchForShippingLocation(self, locstring):
        self.driver.find_element(*ConfirmationPage.shiptocountry).send_keys(locstring)

    def selectShipToLocation(self):
        self.driver.find_element( *ConfirmationPage.country_element1).click()

    def confirmTnC(self, ):
        self.driver.find_element(*ConfirmationPage.termsandconditions).click()

    def ccnfirmPurchase(self,):
        self.driver.find_element(*ConfirmationPage.purchasebtn).click()
        assert self.driver.find_element(*ConfirmationPage.confirmmessage)

