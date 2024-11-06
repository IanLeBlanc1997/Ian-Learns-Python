import requests
from bs4 import BeautifulSoup
import smtplib
import os
email = os.getenv("EMAIL")
print(email)

response = requests.get('https://appbrewery.github.io/instant_pot/')
data= response.text
soup = BeautifulSoup(data,"html.parser")
whole_number= int(soup.find(class_="a-price-whole").getText().strip("."))
decimal = int(soup.find(class_='a-price-fraction').getText())
full_price = float(whole_number + decimal/100)


if full_price <= 100:
    with smtplib.SMTP("smtp.yahoo.com") as connection:
        app_password = "[APP PASSWORD, SETUP IN EMAIL ACCOUNT SETTINGS]"
        #security setup 
        connection.starttls()
        #login and send mail
        connection.login(user = email, password= app_password)
        connection.sendmail(
            from_addr = my_email,
            to_addrs = "ianleblanc7667@yahoo.com",
            msg = f"Subject: Monday Quote\n\n{quote}")
