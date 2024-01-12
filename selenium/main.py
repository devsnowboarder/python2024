from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


chrome_driver_path = "/Users/chrome/chromedriver"
driver_service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=driver_service)




options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
chrome_driver_binary = "/Users/chrome/chromedriver"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

driver.get("https://secure-retreat-92358.herokuapp.com/")


first_name = driver.find_element(By.NAME,"fName")
first_name.send_keys("Michael")
last_name = driver.find_element(By.NAME,"lName")
last_name.send_keys("Wong")



sleep(1000)

driver.quit()