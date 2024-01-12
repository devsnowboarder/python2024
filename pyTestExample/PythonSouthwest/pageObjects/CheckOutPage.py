from selenium.webdriver.common.by import By

class CheckOutPage:
    def __init__(self,driver):
        self.driver = driver



    ProtoCommerceCheckOut = (By.XPATH,"//a[@class='nav-link btn btn-primary']")
    cardTitle = (By.CSS_SELECTOR,".card-title a")
    blackBerry = (By.XPATH,"(//button[@class='btn btn-info'])[4]")
    deliveryCheckout = (By.ID,"country")
    shoppingCheckout = (By.CSS_SELECTOR, ".btn-success")
    IAgreeCheckBox =(By.XPATH,"//label[@for='checkbox2']")
    purchaseCheckout =(By.CSS_SELECTOR,".btn-lg")

#  self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

    def ProtoCommerceCheckoutItem(self):
        return self.driver.find_element(*CheckOutPage.ProtoCommerceCheckOut)

    def getCardTitle(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def clickAdd(self):
        return self.driver.find_element(*CheckOutPage.blackBerry)

    def deliver(self):
        return self.driver.find_element(*CheckOutPage.deliveryCheckout)

    def shopping(self):
        return self.driver.find_element(*CheckOutPage.shoppingCheckout)

    def IAgree(self):
        return self.driver.find_element(*CheckOutPage.IAgreeCheckBox)

    def purchase(self):
        return self.driver.find_element(*CheckOutPage.purchaseCheckout)






