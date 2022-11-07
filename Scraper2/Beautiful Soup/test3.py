from selenium import webdriver
driver = webdriver.Chrome(executable_path='/home/dr74/Downloads/chromedriver_linux64/chromedriver')
driver.get("https://avi.im/stuff/js-or-no-js.html")
p_element = driver.find_element_by_id(id_='intro-text')
print(p_element.text)
driver.quit()