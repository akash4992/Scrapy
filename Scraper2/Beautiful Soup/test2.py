from lib2to3.pgen2 import driver
from selenium import webdriver
import unittest
import time
class GoogelSearch(unittest.TestCase):
    def setup(self):
            global driver
            driver = webdriver.Chrome(executable_path='/home/dr74/Downloads/chromedriver_linux64/chromedriver')
            driver.get('https://www.google.com/')
            driver.maximize_window()

    def test(self):
        driver.find_elements_by_class_name('gLFyf gsfi').send_keys('Kubernates')
        time.sleep(5)
        driver.find_elements_by_class_name('btnK').click()
        time.sleep(5)
    # def tearDown(self):
    #     driver.quit()
        



unittest.main()
