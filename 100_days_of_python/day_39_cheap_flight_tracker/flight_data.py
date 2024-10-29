class FlightData:
    def __init__(self) -> None:
        pass
    def parse_data(self,data):
        for n in range(0,len(data['data'])): 
            departure_date = (f'{data['data'][n]['itineraries'][0]['segments'][0]['departure']['at']}')
            date_and_time = departure_date.split('T')
            destination = data['data'][n]['itineraries'][0]['segments'][-1]['arrival']['iataCode']
            stopovers = len(data['data'][n]['itineraries'][0]['segments'])-1
            grand_total = data['data'][n]['price']['grandTotal']
            if stopovers > 0:
                print(f"There is a flight leaving from CVG to {destination} on {date_and_time[0]} at {date_and_time[1]} with {stopovers} stopovers\n The total price is {grand_total} dollars")
            else:
                print(f"There is a flight leaving from CVG to {destination} on {date_and_time[0]} at {date_and_time[1]} with 0 stopovers\nThe total price is {grand_total} dollars")

