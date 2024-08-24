#BlackJack
import os
def clear_terminal():
    _ = os.system('clear')
import random




#ask the player what they would like to wager
def bet(bank):
    print(f"Welcome to blackjack\nYour bank is ${bank}")
    wager = int(input(f"What would you like to wager?\n$"))
    while wager > bank:
        wager = int(input(f"You have bet more money than you have\nEnter another wager less than {bank}\n"))
    return wager

#deal players cards and dealer's cards and display them
def deal(wager):
    clear_terminal()
    print("I'll deal now")
    print(f"Your wager is: ${wager}")
    your_cards = [random.randint(1,11), random.randint(1,11)]
    dealer_cards = [random.randint(1,11), random.randint(1,11)]
    your_score = sum(your_cards)
    dealer_score = sum(dealer_cards)
#account for two 11's dealt
    if your_score == 22:
        your_cards[0] = 1
        your_score = sum(your_cards)
    if dealer_score == 22:
        dealer_cards[0] = 1
        dealer_score = sum(dealer_cards)
    print(f"Your cards: {your_cards}, current score: {your_score}\nDealer's first card: {dealer_cards[0]}")
    return your_cards, dealer_cards, your_score, dealer_score

#asking player if they want to hit or stand 
def hit_or_stand(your_cards, your_score):
    while True:
        hit = input("Would you like to hit or stand?\n").lower()
        if hit == "hit":
            your_cards.append(random.randint(1,11))
            #check for ace to be 11 or 1, make sure player doesn't enter other number
            if your_cards[-1] == 11 or your_cards[-1] == 1:
                while True:
                    ace = int(input("You drew an ace, would you like it to be an 11 or a 1?\n"))
                    your_cards[-1] = ace
                    if ace == 1 or ace == 11:
                        break        
            your_score = sum(your_cards)
            print(f"Your cards: {your_cards}, current score: {your_score}")
            if your_score > 21:
                break
        elif hit == "stand":
            break
        else:
            print("Sorry, I didn't get that. Please type 'Hit' or 'Stand'")
        
    return your_cards, your_score
        
#dealer plays after player
def dealer_play(dealer_cards, dealer_score):
    dealer_hit_counter = 1
    while dealer_score < 17:
        dealer_hit_counter += 1
        dealer_cards.append(random.randint(1,11))
        dealer_score = sum(dealer_cards)
         #make it so the dealer doesn't bust with ace
        if dealer_cards[-1] == 11 and dealer_score > 21:
            dealer_cards[-1] = 1
            dealer_score = sum(dealer_cards)
        print(f"Dealer hits, dealer's cards: {dealer_cards[0:dealer_hit_counter]} _")
    if dealer_score >= 17 and dealer_score <= 21:
        print(f"Dealer stands")
    else:
        print(f"Dealer busts")
    return dealer_cards, dealer_score

#determine winner and adjust bank
def compare(your_score, dealer_score, bank, wager):
    if your_score > 21:
        print(f"You lose.\nYour score: {your_score}\nDealer score: {dealer_score}")
        bank = bank - wager
        print(f"Your bankroll is: ${bank}")
        return your_score, dealer_score, bank, wager
    if dealer_score > 21:
        print(f"You win! Dealer busts\nYour score: {your_score}\nDealer score: {dealer_score}")
        bank = bank + wager
        print(f"Your bankroll is: ${bank}")
        return your_score, dealer_score, bank, wager
    if your_score > dealer_score and your_score <= 21:
        print("You win")
        bank = bank + wager
        print(f"Your bankroll is: ${bank}")
        return your_score, dealer_score, bank, wager
    elif your_score < dealer_score and dealer_score <= 21:
        print(f"You lose.\nYour score: {your_score}\nDealer score: {dealer_score}")
        bank = bank - wager
        print(f"Your bankroll is: ${bank}")
        return your_score, dealer_score, bank, wager
    elif your_score == dealer_score:
        print("Standoff. It's a tie")
        print(f"Your bankroll is: ${bank}")
        return your_score, dealer_score, bank, wager
    
#main blackjack function
def blackjack():
    clear_terminal()
    bank = 100
    mafia_loans = 0
    while True:
        wager = bet(bank)
        your_cards, dealer_cards, your_score, dealer_score = deal(wager)
        your_cards, your_score = hit_or_stand(your_cards, your_score)
        if your_score <= 21:
            dealer_cards, dealer_score = dealer_play(dealer_cards, dealer_score)
        your_score, dealer_score, bank, wager = compare(your_score, dealer_score, bank, wager)

        #keep playing functionality
        keep_playing = input("Would you like to keep playing?\n").lower()
        if keep_playing != "yes":
            sure = input("Are you sure?\n").lower()
            if sure == "yes":
                break
             #mafia functionality
        if bank == 0:
            mafia = input("You're broke!\nTake a loan from the mafia?\n")
            if mafia == "yes":
                bank += 100
                mafia_loans +=1
                if mafia_loans > 2:
                     print("The mob goon comes in the room and breaks your legs. Game over")
                     break
            else:
                break
blackjack()        
