#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from flight_search import FlightSearch
from data_manager import DataManager
from datetime import datetime
from dateutil.relativedelta import relativedelta
import time
from flight_data import FlightData

today = datetime.now() # Finding the current date

flight_data = FlightData()
flight_searcher = FlightSearch()
data_manager = DataManager() #establishing classes

# main query parameters boilerplate
parameters = {'originLocationCode':'CVG','destinationLocationCode':'','adults':'1','departureDate':'','maxPrice':'','currencyCode':'USD'}

city_codes_list, price_points = data_manager.get_data()  #getting the cities and pricepoints from the google sheet
for city in range(len(city_codes_list)): #setting an iterable for each city on the excel sheet
    for date in range(1,30): #iterable for how many days to look into the future
        today += relativedelta(days=1)
        formatted_today = today.date()
        time.sleep(.1)
        #adjust the parameters to fill the city code and the pricepoint for that city
        parameters['destinationLocationCode'] = city_codes_list[city]
        parameters['maxPrice'] = price_points[city]
        parameters['departureDate'] = formatted_today
        data = flight_searcher.search_flight(parameters) #querying the api
        if data['meta']['count'] > 0: #if there is a flight on that date that fits the pricepoint
            flight_data.parse_data(data)
            # for n in range(0,len(data['data'])): 
            #     departure_date = (f'{data['data'][n]['itineraries'][0]['segments'][0]['departure']['at']}')
            #     date_and_time = departure_date.split('T')
            #     destination = data['data'][n]['itineraries'][0]['segments'][-1]['arrival']['iataCode']
            #     stopovers = len(data['data'][n]['itineraries'][0]['segments'])-1
            #     grand_total = data['data'][n]['price']['grandTotal']
            #     if stopovers > 0:
            #         print(f"There is a flight leaving from CVG to {destination} on {date_and_time[0]} at {date_and_time[1]} with {stopovers} stopovers\n The total price is {grand_total} dollars")
            #     else:
            #         print(f"There is a flight leaving from CVG to {destination} on {date_and_time[0]} at {date_and_time[1]} with 0 stopovers\nThe total price is {grand_total} dollars")
                    


