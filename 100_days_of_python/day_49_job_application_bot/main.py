from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get('https://www.linkedin.com/jobs/search/?currentJobId=4057290270&distance=100&f_AL=true&f_WT=2&geoId=106310628&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&sortBy=R')
time.sleep(2)
try:
    sign_in = driver.find_element(By.XPATH, value = '//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
except:
    pass
    sign_in = driver.find_element(By.CLASS_NAME, value="")
#THIS LINK LOADS THREE DIFFERENT PAGES WITH DIFFERENT HTML STUFF, AND SOMETIMES DOESN'T LOAD AT ALL. I COULD MAKE A TRY BLOCK BUT I THINK I AM JUST GONNA MOVE ON BECAUSE THIS IS STUPID

# sign_in = driver.find_element(By.XPATH, value = '//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
# sign_in.click()
# email_entry = driver.find_element(By.CSS_SELECTOR,value='#email')
# password_entry = driver.find_element(By.CSS_SELECTOR,value='#password')
# email_entry.send_keys("iancodespython@gmail.com")
# password_entry.send_keys("LeBl8675")



time.sleep(100)