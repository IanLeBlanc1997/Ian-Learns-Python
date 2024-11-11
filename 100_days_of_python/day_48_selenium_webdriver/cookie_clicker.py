from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
service = Service(ChromeDriverManager().install())

# Create a new Chrome webdriver instance with the service
driver = webdriver.Chrome(service=service)
driver.get("http://orteil.dashnet.org/experiments/cookie/") # Navigate to a webpage

def buy_item():
    menu = driver.find_elements(By.CSS_SELECTOR,value= "#store div b")
    menu = [price.text.split("-") for price in menu]
    menu.remove([''])
    prices = [int(price[1].replace(",",'')) for price in menu]
    ids = [price[0].strip() for price in menu]
    for i in range(len(prices)-1,0,-1): 
        bank = int(driver.find_element(By.XPATH, value= '//*[@id="money"]').text.replace(",",'')) #update the elements as close to their interaction as possible
        if bank >= prices[i]:
            driver.find_element(By.ID,value= "buy"+ids[i]).click()
            break

five_seconds = time.time() +5 
five_minutes = time.time() + 60*5
cookie = driver.find_element(By.XPATH,value='//*[@id="cookie"]')

while True:
    cookie.click()
    if time.time() > five_seconds:
        buy_item()
        five_seconds = time.time() +5
    if time.time() > five_minutes:
        print(f'after five minutes: {driver.find_element(By.XPATH, value='//*[@id="cps"]').text}')
        exit()