#Who has more followers game

import random
import os
def clear_terminal():
    _ = os.system('clear')
data = [
    {'name': 'Instagram',
     'follower_count': 346,
     'description': 'Social Media platform',
     'country': 'United States'
     },
     {
     'name': 'Cristiano Ronaldo',
     'follower_count': 215,
     'description': 'Footballer',
     'country': 'Portugal'
     },
     {
     'name': 'Ariana Grande',
     'follower_count': 183,
     'description': 'Musician and actress',
     'country': 'United States'}
         
]

winning = True
wins = 0
clear_terminal()
#set first contender one time to start game
contender1 = random.choice(data)
while winning == True:

    #establish data for contender 1 each time
    name1 = contender1['name']
    followers1 = contender1['follower_count']
    description1 = contender1['description']
    country1 = contender1['country']

    #randomly select contender  2
    contender2 = random.choice(data)
    name2 = contender2['name']
    followers2 = contender2['follower_count']
    description2 = contender2['description']
    country2 = contender2['country']

    #make sure conteder 2 not the same as contender 1
    while contender1 == contender2:
        contender2 = data[random.randint(0,2)]
        name2 = contender2['name']
        followers2 = contender2['follower_count']
        description2 = contender2['description']
        country2 = contender2['country']

        #make sure there is a valid answer
    guess = ""
    while guess != "A" and guess != 'B':    
        guess = input(f"Who has more followers?\n'A'\n{name1}\n{description1}\n{country1}\n...or...\n'B'\n{name2}\n{description2}\n{country2}\n" ).upper()
        clear_terminal()
        if guess != "A" and guess != 'B':  
            print("Type 'A' or 'B'")

    def compare(guess, followers1, followers2):
        if guess == 'A':
            if followers1 > followers2:
                return 'a'
            else:
                return "c"
        if guess == 'B':
            if followers2 > followers1:
                return 'b'
            else:
                return "c"
       
    if compare(guess, followers1, followers2) == 'a':
        wins +=1
    elif compare(guess, followers1, followers2) == 'b':
        wins+=1
        contender1 = contender2 
    elif compare(guess, followers1, followers2) == 'c':
        print(f"Game over. Wins: {wins}")
        exit()
    
