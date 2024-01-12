import time
from time import sleep
from typing import List, Any

import pytest
import webdriver_manager.utils
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select


@pytest.mark.usefixtures("setup")
class TestOne:

    def test_e2e(self):
        webdriv




