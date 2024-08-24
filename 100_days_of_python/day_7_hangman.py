#hangman 
import random

def get_secret_hangman_word() -> list:
    word_list = ["aardvark", 'baboon', 'camel', 'dog', 'ravine', 'cherry', 'toupee', 'mister', 'guitar', 'mixer', 'twister', 'glitter', 'monkey', 'quiz', 'ghost', 'piano', 'speaker', 'mountain', 'computer', 'rodeo']
    return list(random.choice(word_list))

def get_empty_answer(secret_hangman_word: list) -> list:
    answer = ""
    for x in range (0, len(secret_hangman_word)):
        answer += "_"
    return list(answer)

def run_hangman():
    secret_hangman_word = get_secret_hangman_word()
    answer = get_empty_answer(secret_hangman_word)

    print("Let's begin hangman!")
    guesses_remaining = int(input("How many guesses do you want?\n"))

    print("Okay! Let's begin.")
    while True:
        print(f'Answer so far: {answer}')
        guess = input('Guess a letter\n')

        # if guess in secret_hangman word, add letter to answer where relevant
        if guess in secret_hangman_word:
            for index in range(0,len(secret_hangman_word)):
                if guess == secret_hangman_word[index]:
                    answer[index] = guess
        else: 
            guesses_remaining -= 1
            print("The word does not contain '" + guess + "'")
            print(f'You have {guesses_remaining} guesses left')

        if guesses_remaining == 0:
            print('You lose! Hangman!')
            break
        elif answer == secret_hangman_word:
            print("You win! The word is " + str(secret_hangman_word))
            break

run_hangman()
