import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep


def test_lambdatest_todo_app():
    chrome_driver = webdriver.Chrome("./chromedriver")
    chrome_driver.get('http://127.0.0.1:8001/')

    expected = "COVID-19 in the UK"
    assert expected == chrome_driver.find_element_by_id("Title").text

    chrome_driver.close()
