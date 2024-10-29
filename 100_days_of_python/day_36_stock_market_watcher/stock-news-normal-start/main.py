STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_apikey = 'M36GTKBC5QPHXLN0'

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_apikey = 'bc3754c3553b41e79b7d5e387b681f8d'

import requests 
import pandas
import json

from datetime import datetime

day = int(datetime.now().day)
yesterday = day-1
day_before = day-2
month = datetime.now().month
year = datetime.now().year
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


stock_parameters = {'function':'TIME_SERIES_DAILY','symbol':'TSLA','interval':'60min','apikey':stock_apikey}
stock_response = requests.get("https://www.alphavantage.co/query",params=stock_parameters)
stock_response.raise_for_status()
data = stock_response.json()
closing_yesterday = float(data["Time Series (Daily)"][f"{year}-{month}-{yesterday}"]['4. close'])
closing_before = float(data["Time Series (Daily)"][f"{year}-{month}-{day_before}"]['4. close'])
difference = abs(closing_yesterday-closing_before)
percent_difference = difference/closing_before*100

news_parameters = {'apikey':news_apikey,'q':"tesla",'from':f'{year}-{month}-{day_before}','sortby':"popularity"}
if percent_difference > 5:
    news_response = requests.get("https://newsapi.org/v2/everything",params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    for n in range (0,3):
        print(f'Title: {news_data['articles'][n]['title']}')
        print(f'Description: {news_data['articles'][n]['description']}\n')
    


#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

