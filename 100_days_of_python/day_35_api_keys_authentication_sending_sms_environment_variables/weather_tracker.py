import requests 
from twilio.rest import Client

twilio_phone_number = 1234567890
twilio_account_number = 123
twilio_api_key = 456

LATITUDE = 39.103119
LONGITUDE = -84.512016
#may need to get different api key or 'appid'
parameters = {'lat':LATITUDE,'lon':LONGITUDE,'appid':'69f04e4613056b159c2761a9d9e664d2','cnt':4}
weather_response = requests.get("api.openweathermap.org/data/2.5/weather",params=parameters)
weather_response.raise_for_status()
weather_data = weather_response.json()
will_rain = False
for n in range(0,4):
    #search through the json file (a dictionary) to find the condition code and make it an integer
    if int(weather_data['list'][n]['weather'][0]['id']) < 700:
        will_rain = True
if will_rain == True:
    client = Client(twilio_account_number,twilio_api_key)
    message = client.messages \ 
    .create(
        body = "Bring an umbrella, it's going to rain"
        from = (+1234567890)
        to = 4407874411
    )


#send myself a text using twilio

twilio_response = requests.get("")



