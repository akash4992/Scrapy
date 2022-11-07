from lib2to3.pgen2 import driver
from selenium import webdriver
driver = webdriver.Chrome(executable_path='/home/dr74/Downloads/chromedriver_linux64/chromedriver')
driver.get('https://www.facebook.com/')
driver.maximize_window()
print('title',driver.title)
print('current url page',driver.current_url)