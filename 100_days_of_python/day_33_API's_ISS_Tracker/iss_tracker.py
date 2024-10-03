# import requests
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# long_lat = (float((response.json()['iss_position']['longitude'])),float(response.json()['iss_position']["latitude"]))
# print(iss_longzzzz_lat)
from datetime import datetime
import requests
import smtplib
import time
LATITUDE = 39.103119
LONGITUDE = -84.512016

parameters = {'lat': LATITUDE,
              'lng': LONGITUDE,
              'formatted': 0}

#find out when the sunset and sunrise are and what time it currently is where I am
response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data['results']['sunrise'].split("T")[1].split(':')[0]) -4
sunset = int(data['results']['sunset'].split("T")[1].split(':')[0]) -4
time_now = datetime.now().hour
#find out where the ISS is
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
long = float((response.json()['iss_position']['longitude']))
lat = float(response.json()['iss_position']["latitude"])
#if the ISS is near me and it is dark then send me an email

while True:
    time.sleep(60)
    if long > -85 and long < -84 and lat > 38.6 and lat < 39.6:
        if time_now > sunset and time_now < sunrise:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                app_password = "[APP PASSWORD, SETUP IN EMAIL ACCOUNT SETTINGS]"
                #security setup 
                connection.starttls()
                #login and send mail
                connection.login(user = 'automobilemusic@gmail.com', password= app_password)
                connection.sendmail(
                        from_addr = 'automobilemusic@gmail.com',
                        to_addrs = 'automobilemusic@gmail.com',
                        msg = 'Subject: ISS Nearby \n\n The ISS is nearby!')


