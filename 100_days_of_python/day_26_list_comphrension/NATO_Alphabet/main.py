import pandas
nato = pandas.read_csv('day_26_list_comphrension/NATO_Alphabet/NATO_Alphabet.csv')
word = input("What word would you like to translate?\n").upper()
nato_dict = {row.letter:row.code for (index,row) in nato.iterrows()}
alphabet = list(nato_dict.keys())

# OR nato_dict = dict(zip(nato.letter,nato.code))
while True:
    try:
        translated = [nato_dict[letter] for letter in word]
        print(translated)
        break
    except:
        print("Please enter a word using only the English alphabet")
        word = input("What word would you like to translate?\n").upper()



    