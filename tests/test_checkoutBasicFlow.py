from e2ePytestSeleniumFlow.pageobjects.HomePage import HomePage
from e2ePytestSeleniumFlow.utilities.BaseClass import BaseClass


class TestE2ECheckout(BaseClass):

    def test_e2e(self):
        self.log.info("Starting Test test_e2e")

        homepage = HomePage(self.driver)

        checkoutpage = homepage.shopitems()
        self.log.info("Navigated to Search Page")

        products = checkoutpage.getProductsDetails()
        for product in products:
            if product.text == "Blackberry":
                checkoutpage.product = product
                checkoutpage.getProductAddToCart().click()

        # //h4[@class='card-title']/a/../../following-sibling::div/button
        print("item added to cart")
        self.log.info("Added " + product.text + " to cart")

        checkoutpage.checkoutItems()
        self.log.info("Navigated to Cart/Checkout Page")

        confirmationpage = checkoutpage.proceedToCheckout()
        self.log.info("Navigated to Shipping/Confirmation Page")

        confirmationpage.searchForShippingLocation("ind")
        self.waitUntilElementIsDisplayed(confirmationpage.country_element)
        # WebDriverWait(self.driver, 10).until(lambda x: x.find_element(By.XPATH, country_element).is_displayed())
        confirmationpage.selectShipToLocation()
        self.log.info("Shipping/Confirmation Page: Selected Shipping location")

        confirmationpage.confirmTnC()
        self.log.info(" Shipping/Confirmation Page: confirmed TnC")

        confirmationpage.ccnfirmPurchase()
        self.log.info("Shipping/Confirmation Page: Confirmed purchase")


        print("Success")


