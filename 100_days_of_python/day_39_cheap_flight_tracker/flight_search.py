import requests
import os
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

class FlightSearch:
    def __init__(self):
        #authentication
        apikey = os.getenv('AMADEUS_FLIGHT_SEARCH_API_KEY')
        apisecret = os.getenv("AMADEUS_FLIGHT_SEARCH_API_SECRET")
        endpoint = 'https://test.api.amadeus.com/v1/security/oauth2/token'
        parameters = {'grant_type':'client_credentials','client_id':apikey,'client_secret':apisecret}
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(url=endpoint,headers=headers,data=parameters)
        result = response.json()
        access_token = result['access_token']
        self.auth = {'authorization':f'Bearer {access_token}'} 

    def search_flight(self,parameters):
        """Queries the api"""
        endpoint = 'https://test.api.amadeus.com/v2/shopping/flight-offers'
        response = requests.get(endpoint,headers=self.auth,params=parameters)
        # print(f'this is the real response message:{response.text}') 
        response.raise_for_status()
        results = response.json()
        return results