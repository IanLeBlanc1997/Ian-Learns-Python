#Followers Game 2 With Functions 

#Who has more followers game
import pdb
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

################################

def convert_data(data):
    contender = random.choice(data)
    name = contender['name']
    description = contender['description']
    followers = contender['follower_count']
    country = contender['country']
    return name, description, followers, country

def compare(guess, followers1, followers2):
    if guess == 'A':
        if followers1 > followers2:
            return True
    if guess == 'B':
        if followers2 > followers1:
            return False 
    else:
        return "Game Over"
    
    
    #establish contender 1 outside of function
contender1 = convert_data(data)
game_going = True
def run_game(contender1):
    wins = 0
    contender2 = convert_data(data)
    print(f"{contender1[0]} vs\n")
    while contender1 == contender2:
        contender2 = convert_data(data)
    followers1 = int(contender1[2])
    followers2 = int(contender2[2])
    print(contender2[0])
    #run compare function
    guess = input("Who has more followers? 'A' or 'B'?").upper()
    if compare(guess, followers1, followers2) == True:
        wins += 1
        print("You're right!")
        return contender1
    elif compare(guess, followers1, followers2) == False:
        wins +=1
        print("You're right!")
        contender1 = contender2
        return contender1
    elif compare(guess, followers1, followers2) == 'Game Over':
        print(f"Game over. Wins: {wins}")
        exit()
clear_terminal()  

while True:
    contender1 = run_game(contender1)
    
