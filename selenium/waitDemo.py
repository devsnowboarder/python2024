import time
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
driver.get("https://www.rahulshettyacademy.com/seleniumPractice")
driver.find_element(By.CSS_SELECTOR,"input.search-keywork").send_keys("ber")
driver.implicitly_wait(4)

# from the parent, get the list of all the buttons
buttons = driver.find_elements(By.XPATH,"//div[@class='product-action']/button")

for button in buttons:
    button.click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CLASS_NAME,"promoBtn").send_keys("rahushettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
print(driver.find_element(By.CSS_SELECTOR,"span.promoInfo").text)
