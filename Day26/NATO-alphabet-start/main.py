import pandas

# store csv contents in a variable called data
data =  pandas.read_csv("NATO-alphabet-start/nato_phonetic_alphabet.csv")

# format dictionary
phonetic_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}

# ask user for a word to assign codes to
word = input("Enter a word: ").upper()

# output words with associated code
output_list = [phonetic_dictionary[letter] for letter in word]
print(output_list)