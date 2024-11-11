from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://secure-retreat-92358.herokuapp.com")
first = driver.find_element(By.XPATH,value='/html/body/form/input[1]')
first.send_keys("Me")
last = driver.find_element(By.XPATH,value='/html/body/form/input[2]')
last.send_keys("I_am")
email = driver.find_element(By.XPATH,value='/html/body/form/input[3]')
email.send_keys("blah@blah.com")
sign_up = driver.find_element(By.XPATH,value = '/html/body/form/button')
sign_up.click()