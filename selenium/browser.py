
import time
from time import sleep
from typing import List, Any

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select


def launchBrowser() -> object:
    chrome_driver_path = "/Users/chrome/chromedriver"
    driver_service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=driver_service)
    options = webdriver.ChromeOptions()
    options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    chrome_driver_binary = "/Users/chrome/chromedriver"
    driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

    return driver
