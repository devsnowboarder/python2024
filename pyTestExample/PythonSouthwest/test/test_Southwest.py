from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

from PythonSouthwest.pageObjects.HomePage import HomePage
from PythonSelfFramework.pageObjects.CheckOutPage import CheckOutPage
from selenium import webdriver
from utilities.BaseClass import BaseClass
from selenium.webdriver.support import expected_conditions as EC
# @pytest.mark.usefixtures("setup")

class TestSouthWest(BaseClass):

    def test_SouthWest(self,launchBrowser):
        homePage = HomePage(self.driver)
        time.sleep(3)
        homePage.getArrive().send_keys("LAS")
        homePage.getArrive().send_keys(Keys.ENTER)
        time.sleep(6)
        homePage.getDepart().click()
        homePage.getDepart().send_keys(Keys.CONTROL + "a")
        homePage.getDepart().send_keys(Keys.DELETE)
        time.sleep(3)
        homePage.getDepart().send_keys("SFO")
        homePage.getDepart().send_keys(Keys.ENTER)

        homePage.getPromo().click()
        time.sleep(2)
        homePage.getSearch().click()
        time.sleep(4)

        # homePage.getName().send_keys("Michael")

        # homePage.getEmail().send_keys("test@aol.com")
        # checkOutPage = CheckOutPage(self.driver)
        #
        # homePage.shopItems().click()
        # time.sleep(2)
        #
        # #  cards = self.driver.find_elements(By.CSS_SELECTOR,".card-title")
        # cards = checkOutPage.getCardTitle()
        # time.sleep(2)
        # i = 0
        # for card in cards:
        #     i = i + 1
        #     cardText = card.text
        #     print("\n", cardText)
        #     if cardText == "Blackberry":
        #         checkOutPage.clickAdd().click()
        #     # self.driver.find_element(By.XPATH,"(//button[@class='btn btn-info'])[4]").click()
        # time.sleep(3)
        #
        # # checkout
        # checkOutPage.ProtoCommerceCheckoutItem().click()
        # checkOutPage.shopping().click()
        # checkOutPage.deliver().send_keys("San Franicsco")
        # checkOutPage.IAgree().click()
        # checkOutPage.purchase().click()

