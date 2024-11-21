google_form = 'https://docs.google.com/forms/d/e/1FAIpQLSeJdac0y3aIbe-pnWekS1aJLtH1J6u9v-SAOcZaZJx6Cjml5Q/viewform?usp=sf_link'
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
sleep_time = .01
driver = webdriver.Chrome()
driver.get(google_form)
def fill_form(addresses,rents,urls):
    for n in range(len(addresses)):
        first_question = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        second_question = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        third_question = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        submit = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
        first_question.send_keys(addresses[n])
        second_question.send_keys(rents[n])
        third_question.send_keys(urls[n])
        submit.send_keys(Keys.RETURN)
        time.sleep(sleep_time)
        submit_another = driver.find_element(By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        submit_another.click()
        time.sleep(sleep_time)
        

