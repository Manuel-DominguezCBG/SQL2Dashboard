import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

chrome_driver = webdriver.Chrome("./chromedriver")
chrome_driver.get('http://127.0.0.1:8001/')
sleep(10)

def test_title():
    
    chrome_driver.find_element_by_id("Title").text
    expected = "COVID-19 in the UK"
    assert expected == chrome_driver.find_element_by_id("Title").text
    

    
def test_buttons():
    
    chrome_driver.find_element_by_id("Author").click()
    sleep(2)
    chrome_driver.find_element_by_id("close").click()
    sleep(2)
    chrome_driver.find_element_by_id("data_show").click()
    sleep(2)
    chrome_driver.find_element_by_id("close2").click()
    sleep(2)
    chrome_driver.find_element_by_id("link-centered").click()
    
    chrome_driver.close()

