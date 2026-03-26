import pandas

# store csv contents in a variable called data
data =  pandas.read_csv("NATO-alphabet-with error handling/nato_phonetic_alphabet.csv")

phonetic_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}

# format dictionary
def generate_phonetic():
    word = input("Enter a word: ").upper()
    # ask user for a word to assign codes to
    if word == "EXIT":
        pass
    else:
        try:
            output_list = [phonetic_dictionary[letter] for letter in word]
        except:
            print("Please enter a word!")
            generate_phonetic()
        else:
            # output words with associated code
            print(output_list)
            generate_phonetic()

generate_phonetic()