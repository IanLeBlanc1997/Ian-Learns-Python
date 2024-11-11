from selenium import webdriver
from selenium.webdriver.common.by import By


# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get(url="https://www.udemy.com/course/100-days-of-code/learn/lecture/21785306#overview")

# price_dollar = driver.find_element(By.CLASS_NAME, value='a-price-whole').text
# price_cents = driver.find_element(By.CLASS_NAME, value='a-price-fraction').text
# print(f'price is ${price_dollar}.{price_cents}')
# driver.find_element(By.ID,value=)
# driver.find_element(By.NAME,value=)
# driver.find_element(By.CLASS_NAME,value=)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value = ".documentation-widget a")
# print(documentation_link.text)

print(driver.find_element(By.XPATH, value='//*[@id="tabs--1-content-2"]/div/div'))


driver.quit()