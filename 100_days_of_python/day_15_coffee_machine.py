#coffee machine

import os
def clear_terminal():
    _ = os.system('clear')
espresso = {
    'water': 50,
     "coffee": 18,
      "milk": 0,
      "dollars": 1.5
      
        }
latte = {'water': 200,
     "coffee": 24,
      "milk": 150,
      "dollars": 2.5
        }
cappuccino = {'water': 250,
"coffee": 24,
"milk": 100,
"dollars": 3
}

coffee_machine = {'water': 300,
"coffee": 100,
"milk": 200,
"dollars": 0}

ingredients = 'yes'
clear_terminal()
#print report of resources if asked
#check if the resources are sufficient to make the drink
#process coins, if enough money, give correct change, if not enough money, give money back 
#make coffee, deduct resources from coffee machine and add money 
#make the machine able to turn off

def drink_type():
    # drink = 'latte'
    # drink_factor = latte
    # return drink, drink_factor
    drink = input("What would you like? Espresso/Latte/Cappucino?\n").lower()
    if drink == 'espresso':
        drink_factor = espresso
        return drink, drink_factor
    elif drink == "latte":
        drink_factor = latte
        return drink, drink_factor
    elif drink == 'cappuccino':
        drink_factor = cappuccino
        return drink, drink_factor
    elif drink == 'report':
        print(coffee_machine)
        drink_type()
    elif drink == 'off':
        exit()
    else:
        drink_type()

def take_money():
    money = 0
    quarters = (input("Insert coins: \n How many quarters?\n"))
    while quarters == 'report':
        print(coffee_machine)
        quarters = (input("How many quarters?\n"))
    if quarters == 'off':
        exit()
    quarters = int(quarters)
    dimes = (input("How many dimes?\n"))
    while dimes == 'report':
        print(coffee_machine)
        dimes = (input("How many dimes?\n"))
    if dimes == 'off':
        exit()
    dimes = int(dimes)
    nickels = (input("How many nickels?\n"))
    while nickels == 'report':
        print(coffee_machine)
        nickels = (input("How many nickels?\n"))
    if nickels == 'off':
        exit()
    nickels = int(nickels)
    pennies = (input("How many pennies?\n"))
    while pennies == 'report':
        print(coffee_machine)
        pennies = (input("How many pennies?\n"))
    if pennies == 'off':
        exit()
    pennies = int(pennies)
    clear_terminal()
    money = round((quarters * .25) + (dimes * .1) + (nickels * .05) + (pennies * .01), 2)
    print(quarters, dimes, nickels, pennies)
    print(f'${money} inserted')
    return money

def make_coffee(drink_factor, refund, money):
    for i in coffee_machine:
        #makes money additive to machine
        if i == "dollars":
            coffee_machine[i] += money
            coffee_machine[i] -= refund
            continue
        coffee_machine[i] -= drink_factor[i]
    return coffee_machine, drink_factor, refund, money

def unmake_coffee(drink_factor, refund, money):
    for i in coffee_machine:
        #makes money additive to machine rather than taking away
        if i == "dollars":
            coffee_machine[i] -= money
            coffee_machine[i] += refund
            continue
        coffee_machine[i] += drink_factor[i]
      
        
def check_money(money, cost):
    while money < cost:
        print("Not enough money. Please insert coins again")
        take_money()
    if money == cost:
        refund = 0
        return refund
    if money > cost:
        refund = round((money - cost), 2)
        print(f'Refund ${refund}')
        return refund
    
def check_ingredients(coffee_machine):
    for i in coffee_machine:
        if coffee_machine[i] < 0:
            ingredients = 'no'
            return ingredients
         
clear_terminal()
#program level loop
while True:
    #determine type of drink and make able to reference drink attributes in dictionary 
    drink, drink_factor = drink_type()
    #determine how much money tendered and how much the drink costs
    money = take_money()
    cost = drink_factor["dollars"]
    #compare money to drink cost
    refund = check_money(money, cost)
    #make coffee if money is sufficient and there are sufficient ingredients
    coffee_machine, drink_factor, refund, money = make_coffee(drink_factor, refund, money)
    #check the ingredients
    ingredients = check_ingredients(coffee_machine)
    if ingredients == 'no':
        print("Out of ingredients for that item. Please make another selection")
        unmake_coffee(drink_factor, refund, money)
        print(coffee_machine)
        continue
    print(f'Here is your {drink}')  
    print(f'coffee machine readout: {coffee_machine}')
    
