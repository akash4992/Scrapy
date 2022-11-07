from bs4 import BeautifulSoup
import requests
from selenium import webdriver
driver =  webdriver.Chrome(executable_path='/home/dr74/Downloads/chromedriver_linux64/chromedriver')
driver.get('http://quotes.toscrape.com/js/')
# response = requests.get(url)
# htmlcontent = response.text
soup = BeautifulSoup(driver.page_source,"lxml")
author_element = soup.find("small",class_="author")
print(author_element.text)
driver.quit()
