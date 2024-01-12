import time
from time import sleep
from typing import List, Any

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select


import browser

# chrome_driver_path = "/Users/chrome/chromedriver"
# driver_service = Service(executable_path=chrome_driver_path)
# driver = webdriver.Chrome(service=driver_service)
# options = webdriver.ChromeOptions()
# options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
# chrome_driver_binary = "/Users/chrome/chromedriver"
# driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

@pytest.fixture
def fixture1():
    return "porsche"


def test_firstProgram():
    print("hello World")
    driver =browser.launchBrowser()

    driver.get("https://www.rahulshettyacademy.com/AutomationPractice")

    radioButtons = driver.find_elements(By.NAME, "radioButton")
    radioButtons[2].click()
    assert radioButtons[2].is_selected()
    driver.quit()


def test_secondProgram():
    print("Second Program")
    driver = browser.launchBrowser()
    driver.get("https://www.rahulshettyacademy.com/dropdownsPractise/")
    driver.find_element(By.ID, "autosuggest").send_keys("ind")

    time.sleep(2)
    countries = driver.find_elements(By.CLASS_NAME, "ui-menu-item")

    for country in countries:
        if country.text.strip("\n") == "India":
            print(" found ", country.text)
            time.sleep(2)
            country.click()
            time.sleep(3)
            print(driver.find_element(By.ID, "autosuggest").text)

    driver.quit()


def test_thirdProgram(fixture1):
    print("Third Program")
    driver = browser.launchBrowser()

    driver.get("https://www.rahulshettyacademy.com/AutomationPractice")

    checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    print(len(checkboxes))
    for checkbox in checkboxes:
        if checkbox.get_attribute("name") == "checkBoxOption2":
            checkbox.click()
            assert checkbox.is_selected()

    driver.quit()



def test_fourthProgram():
    print('fourth Program')
