import requests
sheetyUN = 'automobilemusic@gmail.com'
sheetyUN = 'automobilemusic@gmail.com'
sheet_endpoint = 'https://api.sheety.co/7130b0d4939d4c449510184247cbd134/cheapFlightTracker/sheet1'
class DataManager:
    def __init__(self):
        pass
    def get_data(self):
        response = requests.get(sheet_endpoint)
        results=response.json()
        data = results['sheet1']
        city_codes_list = [cities['iataCode'] for cities in data]
        price_points = [cities['lowestPrice'] for cities in data]
        return city_codes_list, price_points