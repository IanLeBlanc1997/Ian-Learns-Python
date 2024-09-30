import pandas
import datetime as dt
import smtplib
my_email = 'ian@gmail.com'

# check what today is and if today is someone's birthday
birthdays = pandas.read_csv("day_32_automated_birthday_wisher/birthdays.csv")


today = dt.datetime.now()
month = today.month
day = today.day
birthday = False
birthday_person = birthdays[(birthdays['month'] == month) & (birthdays['day'] == day)]
birthday_person_name = birthday_person.at[0,'name']
if not birthday_person.empty:
    #modify the letter
    with open("day_32_automated_birthday_wisher/letter_1.txt",'r') as starting_letter:
        letter = starting_letter.read()
        new_letter = letter.replace('[NAME]',birthday_person_name)
        with open(f"day_32_automated_birthday_wisher/letter_for_{birthday_person_name}",'w') as completed_letter:
            completed_letter.write(new_letter)

with smtplib.SMTP("smtp.gmail.com") as connection:
    app_password = "[APP PASSWORD, SETUP IN EMAIL ACCOUNT SETTINGS]"
    #security setup 
    connection.starttls()
    #login and send mail
    connection.login(user = my_email, password= app_password)
    with open(f"day_32_automated_birthday_wisher/letter_for_{birthday_person_name}",'r') as completed_letter:
        sendable_letter = completed_letter.read()
        connection.sendmail(
            from_addr = my_email,
            to_addrs = birthday_person.at[0,'email'],
            msg = f"Subject: Happy birthday: {birthday_person_name}\n\n{sendable_letter}")



    


    
