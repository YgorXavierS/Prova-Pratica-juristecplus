from selenium.webdriver import Firefox
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

url = "https://portal.inmet.gov.br/"
from selenium import webdriver
# Code 2
browser.get("https://app.finxter.com/")
browser = webdriver.Firefox(executable_path="") 
driver =webdriver.Firefox()
driver.get(url)

driver.find_element_by_nome("search").send_keys(Keys.ENTER)
driver.get("https://portal.inmet.gov.br/")
soup = BeautifulSoup(driver.page_source,'html_parse')
