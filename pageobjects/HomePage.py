from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from e2ePytestSeleniumFlow.pageobjects.CheckoutPage import CheckoutPage





class HomePage:
    shop = (By.XPATH, "//a[@class='nav-link' and @href='/angularpractice/shop']")
    text_name   =   (By.XPATH , "// input[ @ name = 'name']")
    text_email  =   (By.XPATH,"//input[@name='email']")
    text_password =  (By.XPATH, "//input[@type='password']")
    chkbox_icecreams = (By.XPATH, "//input[@type='checkbox']")
    dropdwn_gender = (By.CSS_SELECTOR, "select[id='exampleFormControlSelect1']")
    btn_submit = (By.XPATH, "//input[@value='Submit']")
    msg_success = (By.CSS_SELECTOR, ".alert-success")

    def __init__(self, driver):
        self.driver = driver
    def shopitems(self):
        self.driver.find_element(*HomePage.shop).click()
        return CheckoutPage(self.driver)
    def enterName(self, str_name):
        self.driver.find_element(*HomePage.text_name).send_keys(str_name)

    def enterEmail(self, str_email):
        self.driver.find_element(*HomePage.text_email).send_keys(str_email)

    def enterPassword(self, str_password):
        self.driver.find_element(*HomePage.text_password).send_keys(str_password)

    def selectLove4Icecreams(self):
        self.driver.find_element(*HomePage.chkbox_icecreams).click()

    def selectGender(self, str_Gender):
        Select(self.driver.find_element(*HomePage.dropdwn_gender)).select_by_visible_text (str_Gender)
        # dropdown = Select(chrome_driver.find_element(By.ID, "exampleFormControlSelect1")).select_by_visible_text(
        #     "Female")

    def clickSubmit(self):
        self.driver.find_element(*HomePage.btn_submit).click()
    def verifySuccessfulCompletion(self, str_success):
        str1 = self.driver.find_element(*HomePage.msg_success).text
        assert str1.find(str_success)




