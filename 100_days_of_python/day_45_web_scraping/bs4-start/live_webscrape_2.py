import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com')
data = response.text
soup = BeautifulSoup(data,'html.parser')
articles = soup.findAll(name='span',class_='titleline')

upvote_list = [int(score.getText().split(" ")[0]) for score in soup.findAll(name='span',class_='score')] # list comprehension turns a list into another list

highest_votes = max(upvote_list) #uses max function to find max of list

highest_index = upvote_list.index(highest_votes) #uses index function to find index of max value
title = articles[highest_index].find(name='a').getText() #cross-index with index value into other list 
print(title) 


  ######### THIS CODE DOES NOT RUN PROPERLY ALTHOUGH IT IS CODED PROPERLY BECAUSE OF LISTING ERROR ON SOURCE WEBSITE ############

########### SOME ENTRIES DO NOT HAVE AN UPVOTE VALUE OR ABILITY TO BE UPVOTED PRESENTLY SO THEY CREATE AN INDEX MISMATCH ##########






