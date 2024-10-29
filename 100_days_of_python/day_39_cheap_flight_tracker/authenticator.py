
################ AUTHENTICATE ACCESS //// KEY LASTS FOR 30 MINUTES ###################

# apikey = 'DlmY6KHWjf28MaM45Ms4JaTrkN5SGEiG'
# apisecret = '6XI4lrK0EteEVLxG'
# endpoint = 'https://test.api.amadeus.com/v1/security/oauth2/token'
# parameters = {'grant_type':'client_credentials','client_id':apikey,'client_secret':apisecret}
# headers = {'Content-Type': 'application/x-www-form-urlencoded'}
# response = requests.post(url=endpoint,headers=headers,data=parameters)
# result = response.json()
# access_token = result['access_token']
# print(access_token)
import os

if 'AMADEUS_FLIGHT_SEARCH_API_KEY' in os.environ:
    print("Variable exists!")
else:
    print('No')