from selenium.webdriver.common.by import By


class HomePage():
    def __init__(self, driver):
        self.driver = driver

    depart = (By.ID, "LandingAirBookingSearchForm_originationAirportCode")
    arrive = (By.XPATH, "(//input[@class='input--text'])[2]")
    promo = (By.XPATH, "(//input[@type='text'])[6]")
    search = (By.ID, "LandingAirBookingSearchForm_submit-button")
    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def getDepart(self):
        return self.driver.find_element(*HomePage.depart)

    def getArrive(self):
        return self.driver.find_element(*HomePage.arrive)

    def getPromo(self):
        return self.driver.find_element(*HomePage.promo)

    def getSearch(self):
        return self.driver.find_element(*HomePage.search)

    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)
