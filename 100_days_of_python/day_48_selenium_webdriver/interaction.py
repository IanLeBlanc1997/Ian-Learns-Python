from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# articles = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]').text #find elements by XPATH
# articles = driver.find_element(By.CSS_SELECTOR, value = "#articlecount a") #find elements by css selectors


# all_portals = driver.find_element(By.LINK_TEXT, value = "Content portals") #find elements by hyperlink text
# all_portals.click()
# print(articles)

#Find the Search <input> by Name
search = driver.find_element(By.NAME, value= 'search')
search.send_keys("Python",Keys.ENTER)

time.sleep(10)
driver.quit()