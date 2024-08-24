"""#Scope

enemies = 1 

def increase_enemies():
    print(f'Enemies inside function: {enemies}')
    return enemies + 1
enemies = increase_enemies()
print(f'Enemies outside function : {enemies}')

# local scope"""

""""# global scope
player_health = 10 

def drink_potion():
    potion_strength = 2
    print(potion_strength)
    print(player_health)
drink_potion()
"""


#number guessing game 
import random
number = random.randint(1,100)
difficulty = input("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100\nChoose a difficulty. Type 'Easy' or 'Hard'\n").lower()
if difficulty == 'easy':
    tries = 9
if difficulty == 'hard':
    tries = 4
def guess_and_check():
    guess = int(input("Make a guess\n"))
    if guess == number:
        return True
    if guess > number:
        print("Too high.\nGuess again")
        return tries - 1
    if guess < number:
        print("Too low.\n Guess again")
        return tries -1


while tries > 0:
    if guess_and_check() == True:
        print("You win!")
        break
    else:
        tries = guess_and_check()
        print(f"You have {tries} tries left")
    