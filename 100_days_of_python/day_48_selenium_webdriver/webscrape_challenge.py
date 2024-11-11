from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
driver.get(url = 'https://www.python.org')
#find first upcoming event
times = []
events = []
for n in range (1,6):
    times.append(driver.find_element(By.XPATH, value = f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{n}]/time'))
    events.append(driver.find_element(By.XPATH, value= f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{n}]/a'))
times_and_events = {}
times = [n.text for n in times] 
events = [n.text for n in events]

for n in range(len(times)):
    times_and_events[n] = {"Time": times[n],"Event":events[n]}
print(times_and_events)
print("XXXXXXXXXXXXX")

########### CHALLENGE ############### MAKE THE ONE LINER ############
times_and_events = {i:{"time":time,"event":event} for i, (time,event) in enumerate(zip(times,events))}
print(times_and_events)


