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

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME,"name").send_keys("Michael")
driver.find_element(By.ID,"exampleCheck1").click()
print(driver.find_element(By.CLASS_NAME,"tab-space").text)
print(driver.find_element(By.XPATH,"(//div[@class='form-group']/label)[1]").text)


driver.quit()