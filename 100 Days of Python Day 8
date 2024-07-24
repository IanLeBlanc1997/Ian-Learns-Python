#paint can calculator
"""import math
def paint_calc(height, width, coverage):
   # cans = math.ceil(height * width / coverage)
    #print(f"You'll need {cans} cans of paint.")
height = int(input("height?\n"))
width = int(input('width?\n'))
coverage = int(input("coverage?\n"))
paint_calc(height, width, coverage)"""


"""#prime number calculator
def prime_checker(number):
    is_prime = True
    for n in range (2,number -1):
        if number % n == 0:
            print("It's not a prime number")
    if is_prime:
        print("It's a prime number")
number = int(input("What number would you like to check?\n"))
prime_checker(number)"""

#caeser shift encryption

"""alphabet = list('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')


def run_caeser_shift():
    cypher_direction = input("Would you like to encode a message (E) or decode one (D)?\n")
    if cypher_direction.upper() == "E":
        encode()
    elif cypher_direction.upper() == "D":
        decode()
    else:
        print("Sorry, I didn't get that. Try again")

def encode():
    english_message = input("What is your message to encrypt?\n")
    english_message = list(english_message.lower())
    for n in range (0, len(english_message)):
        if n == ' ':
            return
        else:
            english_message[n] = alphabet.index(english_message[n])
    shift_english(english_message)

def decode():
    coded_message = input("What message should I decrypt?\n")
    coded_message = list(coded_message.lower())
    for n in range (0, len(coded_message)):
        if n == ' ':
            pass
        else:
            coded_message[n] = alphabet.index(coded_message[n])
    shift_coded(coded_message)

def shift_english(english_message):
    secret_message = ''
    shift_number = int(input("What is the shift number?\n"))
    for n in range (0, len(english_message)):
        english_message[n] = int(english_message[n]) + shift_number
        secret_message += alphabet[english_message[n]]
    print(f'Your secret message is: {secret_message}')   

def shift_coded(coded_message):
    decoded_message = ''
    shift_number = int(input("What is the shift number?\n"))
    for n in range (0, len(coded_message)):
        coded_message[n] = int(coded_message[n]) - shift_number
        decoded_message += alphabet[coded_message[n]]
    print(f'Your decoded message reads: {decoded_message}')
run_caeser_shift()"""

#caesar shift challenge, one function called "caesar" that will encrypt and decrypt
run_again = True
while run_again == True:

    alphabet = ('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')
    print("Welcome to Caesar Shift Cipher")
    cipher_direction = input("Would you like to encode or decode?\n")
    shift_amount = int(input("What is the shift number?\n"))
    start_text = list(input("What is your message?\n").lower())
    if shift_amount >= 26:
        shift_amount = shift_amount % 26
    def caesar(start_text, shift_amount, cipher_direction):
        end_text = ""
        if cipher_direction == 'decode':
            shift_amount *= -1       
        for letter in start_text:
            if letter not in alphabet:
                end_text += letter
            else:
                position = alphabet.index(letter)
                new_position = position + shift_amount
                end_text += alphabet[new_position]
        print(f"Here's the {cipher_direction}d result: {end_text}")
    caesar(start_text, shift_amount, cipher_direction)
    repeat = input(f'Would you like to encode or decode again? Y or N\n').upper()
    if repeat == "N":
        run_again = False
        print("Goodbye")