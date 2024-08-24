'''#learning about dictionaries 

programming_dictionary = {
    "bug": "an error in a program that prevents the program from running as expected.",
    "function": "a piece of code that you can easily call over and over again"
    }
print(programming_dictionary["function"])

#add to a dictionary
programming_dictionary["Loop"] = "the action of doing something over and over again"
print(programming_dictionary)

#create new dictionary
#empty_dictionary = {}

#wipe dictionary
#programming_dictionary = {}


#edit an item in a dictionary
programming_dictionary["bug"] = "a little creature that crawled on me last night"

#loop through a dictionary 

for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])'''

########################################

'''#nesting a list in a dictionary
travel_log = {
    "France": ['paris', 'lille', 'dijon'],
    "Germany": ["Berlin", "hamburg", 'stuttgart']
}

#nesting a dictionary in a dictionary

travel_log2 = {
    'France': {"cities_visitied": ["paris", 'lille', 'dijon'], "total visits": 12},
    "Germany": {'cities visited': ['Berlin', 'Hamburg', 'Stockholm'], 'total visits': 5},
}

#nesting a dictionary in a list

travel_log3 = [
    {
    'Country': 'France',
    "cities_visitied": ["paris", 'lille', 'dijon'],
    "total visits": 12
    },
    {
    'country': "Germany",
    'cities visited': ['Berlin', 'Hamburg', 'Stockholm'],
    'total visits': 5
    },
]'''

##################################
import os
def clear_terminal():
    _ = os.system('clear')
    
def auction():
    print("Welcome to the blind auction")
    bidders = int(input("How many bidders are there?\n"))
    bidders_and_bids = {}
    bidlist = []
    def run_auction(bidders):
        for index in range(0,bidders):
            name = input("What is your name?\n")
            bid = int(input("What is your bid?\n"))
            clear_terminal()
            bidders_and_bids[name] = bid
    run_auction(bidders)
    def check_for_ties(bidders_and_bids):
        values = list(bidders_and_bids.values())
        names = list(bidders_and_bids.keys())
        for i in range(0, len(values)):
            for j in range(i + 1, len(values)):
                if values[i] == values[j]:
                    print(f"There is a tie between {names[i]} and {names[j]}, please bid again.")
                    auction()
                else:
                    print(f'The bids stack up as such: \n {bidders_and_bids}')
                    max_bidder = max(bidders_and_bids, key=bidders_and_bids.get)
                    print(f'The winner is {max_bidder}!')
    check_for_ties(bidders_and_bids)
auction()
