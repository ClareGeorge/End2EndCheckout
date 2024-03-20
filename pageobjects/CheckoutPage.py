from selenium.webdriver.common.by import By

from e2ePytestSeleniumFlow.pageobjects.ConfirmationPage import ConfirmationPage


class CheckoutPage:
    productdetail = (By.XPATH, "//h4[@class='card-title']/a")
    addtocart = (By.XPATH, "../../following-sibling::div/button")
    checkout = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    proceedcheckout = (By.XPATH, "//button[@class ='btn btn-success']")

    def __init__(self, driver):
        self.driver = driver
    def getProductsDetails(self):
        return self.driver.find_elements(*CheckoutPage.productdetail)

    def getProductAddToCart(self):
        return self.product.find_element(*CheckoutPage.addtocart)


    def checkoutItems(self):
        self.driver.find_element(*CheckoutPage.checkout).click()
        print("clicked checkout")

    def proceedToCheckout(self):
        self.driver.find_element(*CheckoutPage.proceedcheckout).click()
        print("clicked  proceed to checkout")
        return ConfirmationPage(self.driver)



