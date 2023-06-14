# импортируем модули и отдельные классы

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

URL = "http://ichamjkegm.temp.swtest.ru/"
def test_group(browser):
  
    expected_menu = [None] 


    browser.get(URL)
    elements = browser.find_elements(by=By.CSS_SELECTOR, value= "[class='block-entries']")
    

    result = [el.get_attribute('text') for el in elements]

    assert result == expected_menu, 'Top menu does not matching to expected'