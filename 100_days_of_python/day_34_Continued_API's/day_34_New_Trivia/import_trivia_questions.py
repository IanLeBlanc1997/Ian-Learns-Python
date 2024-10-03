import requests


#get 10 true or false questions from the api and save them in a file 
parameters = {"amount":10,
              "type":'boolean'}
response = requests.get(url="https://opentdb.con/api",params=parameters)
response.raise_for_status()
trivia_questions = response.json()['results']


#these questions are not formatted properly with some symbols being replaced with html character entitites
# import the html module and "unescape" the text 

import html 
trivia_questions = html.unescape(trivia_questions)

with open("day_34_Continued_API's/trivia_questions.txt",'w') as question_data:
    question_data.write(trivia_questions)

