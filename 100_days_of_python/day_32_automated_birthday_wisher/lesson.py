# #how to send email using python 

# import smtplib 
# my_email = "automobilemusic@gmail.com"
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     app_password = "[APP PASSWORD, SETUP IN EMAIL ACCOUNT SETTINGS]"
#     #security setup 
#     connection.starttls()
#     #login and send mail
#     connection.login(user = my_email, password= app_password)
#     connection.sendmail(from_addr = my_email, to_addrs = "ianleblanc7667@yahoo.com", msg = "Subject: Greeting\n\nHello")


#make a datetime object that stores a particular time using kwargs

# birthday = dt.datetime(year=1997,month=2,day=2)
# print(birthday)



import datetime as dt
import random
import pandas
import smtplib


#open up the file with all the inspirational quotes and format it as a list
with open("day_32_automated_birthday_wisher/quotes.txt") as data:
    quotes_list = data.readlines()
    quote = random.choice(quotes_list)
   

#find out what day of the week it is
now = dt.datetime.now()
monday = 0
weekday = now.weekday()
#if it is monday, then send an email with a random quote
if weekday == monday:
    my_email = "automobilemusic@gmail.com"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        app_password = "[APP PASSWORD, SETUP IN EMAIL ACCOUNT SETTINGS]"
        #security setup 
        connection.starttls()
        #login and send mail
        connection.login(user = my_email, password= app_password)
        connection.sendmail(
            from_addr = my_email,
            to_addrs = "ianleblanc7667@yahoo.com",
            msg = f"Subject: Monday Quote\n\n{quote}")

