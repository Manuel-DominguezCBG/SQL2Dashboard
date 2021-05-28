"""
NAME:          test_db2dashboard.py
AUTHOR:        Manuel Dominguez
EMAIL:         manolo.biomero@gmail.com
DATE:          27/05/2021
INSTITUTION:   Salisbury Hospital
DESCRIPTION:   To test the dashboard Covid-19. A total of 17 test group in 4 funtions     
"""
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from time import sleep


URL = 'http://127.0.0.1:8001/'
@pytest.fixture
def browser():

  # Initialize ChromeDriver
  driver = Chrome("./chromedriver")

  # Wait implicitly for elements to be ready before attempting interactions
  driver.implicitly_wait(10)
  
  # Return the driver object at the end of setup
  yield driver
  
  # For cleanup, quit the driver
  driver.quit()


def test_text(browser):
  # Navigate to the Dashboard 
  browser.get(URL)
  # Find the search input element

  expected = "People tested positive"
  assert expected == browser.find_element_by_id("Title_card1").text

  expected = "Deaths within 28 days of positive test"
  assert expected == browser.find_element_by_id("Title_card2").text

  expected = 'Patients admitted'
  assert expected == browser.find_element_by_id("Title_card3").text
  
  expected = 'Virus test conducted'
  assert expected == browser.find_element_by_id("Title_card4").text

def test_buttons(browser):
  # Click in each button 
  browser.get(URL)
  browser.find_element_by_id("Author").click()
  sleep(2) # Sometimes the output of the buttoms takes a a bit

  browser.find_element_by_id("close").click()
  sleep(2)

  browser.find_element_by_id("data_show").click()
  sleep(2)

  browser.find_element_by_id("close2").click()
  sleep(2)

  browser.find_element_by_id("link-centered").click()
  sleep(2)


def test_dates(browser):
  browser.get(URL)

  expected = "01/27/2021"
  # This is using relative xpath
  assert expected == browser.find_element_by_xpath(".//input[contains(@class,'DateInput_input')]").get_attribute("value")
  # This is using absolute xpath
  expected = '01/28/2021'
  assert expected == browser.find_element_by_xpath('/html/body/div/div/div/div[3]/div[1]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div/div/input').get_attribute("value")

def test_card_values(browser):
  browser.get(URL)
  firs_card = "726797"
  second_card = "49806"
  Third_card = "2216"
  Fourth = "6099" 
  Fift_card = "1524741"

  assert firs_card == browser.find_element_by_xpath("/html/body/div/div/div/div[3]/div[1]/div/div/div[2]/div[1]/div/div[2]/h2").text 
  assert second_card == browser.find_element_by_xpath('/html/body/div/div/div/div[3]/div[1]/div/div/div[2]/div[2]/div/div[2]/h2').text 
  assert Third_card == browser.find_element_by_xpath('/html/body/div/div/div/div[3]/div[1]/div/div/div[2]/div[3]/div/div[2]/h2').text
  assert Fourth == browser.find_element_by_xpath('/html/body/div/div/div/div[3]/div[1]/div/div/div[2]/div[4]/div/div[2]/h2').text
  assert Fift_card == browser.find_element_by_xpath('/html/body/div/div/div/div[3]/div[1]/div/div/div[2]/div[5]/div/div[2]/h2').text


if __name__ == "__main__":
    simple_test()