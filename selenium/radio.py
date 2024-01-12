import time
from time import sleep
from typing import List, Any

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select


chrome_driver_path = "/Users/chrome/chromedriver"
driver_service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=driver_service)




options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
chrome_driver_binary = "/Users/chrome/chromedriver"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice")

radioButtons = driver.find_elements(By.NAME,"radioButton")
radioButtons[2].click()
assert  radioButtons[2].is_selected()


driver.quit()

