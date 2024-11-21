from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
tinder = driver.get("https://tinder.com")
time.sleep(2)
login = driver.find_element(By.XPATH, value= '//*[@id="s546717130"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]/div')
login.click()
time.sleep(1)
withphone = driver.find_element(By.XPATH, value='//*[@id="s-1181663946"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[3]/button/div[2]/div[2]/div[2]/div/div')
withphone.click()
time.sleep(2)
phone_entry = driver.find_element(By.CSS_SELECTOR, value='#phone_number')
phone_entry.send_keys('4407874411')
time.sleep(2)
next = driver.find_element(By.XPATH, value='//*[@id="s-1181663946"]/div/div[1]/div[1]/div/div[3]/button/div[2]/div[2]/div')
next.click()


time.sleep(100)