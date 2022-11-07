from xml.dom.minidom import Element
from selenium import webdriver
driver =  webdriver.Chrome(executable_path='/home/dr74/Downloads/chromedriver_linux64/chromedriver')
driver.get('http://quotes.toscrape.com/js/')

elements  = driver.find_elements_by_class_name("author")
for ele in elements:
    print(ele.text)
driver.quit()