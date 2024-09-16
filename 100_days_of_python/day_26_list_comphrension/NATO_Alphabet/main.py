import pandas
nato = pandas.read_csv('day_26_list_comphrension/NATO_Alphabet/NATO_Alphabet.csv')
word = input("What word would you like to translate?\n").upper()
nato_dict = {row.letter:row.code for (index,row) in nato.iterrows()}
# OR nato_dict = dict(zip(nato.letter,nato.code))
translated = [nato_dict[letter] for letter in word]
print(translated)



    