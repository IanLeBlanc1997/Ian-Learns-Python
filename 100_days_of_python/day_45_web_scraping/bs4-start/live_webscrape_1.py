from bs4 import BeautifulSoup
import requests
response = requests.get('https://news.ycombinator.com')
data = response.text
soup = BeautifulSoup(data,'html.parser')
all_scores = soup.select(".score") # get all of the scores
highest_score = 0 #set baseline score to compare to in the "for" loop
counter = 0
for score in all_scores:
    counter +=1
    datapoint = score.getText()
    split_datapoint = datapoint.split(" ")
    number = int(split_datapoint[0]) #parse the score data into an integer that lets us compare values
    if number > highest_score: 
        highest_score = number 
        article_number = counter #log where the score counter found it's highest mark for indexing all articles list

titles = soup.findAll(name='span',class_='titleline')
print(f"The highest scored article on hackernews is '{titles[article_number].getText()}' with a score of {highest_score} points\nLink:{titles[article_number].get("href")}")      


# first_title = soup.find(name='span',class_='titleline')
# # first_title=first_title.get("href")
# print(first_title.a.getText())




 
