# replace [name] from starting letter
placeholder = "[name]"
    
# store names in a list
with open("Mail Merge Project Start/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    
# store letter template in a variable called letter
with open("Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()

for name in names:
    # remove \n from end of each name
    stripped_name = name.strip()
    # replace [name] with actual name
    finished_letter = letter.replace(placeholder, stripped_name)
    # write letter with actual names in new files.
    with open(f"Mail Merge Project Start/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as ready_to_send:
        ready_to_send.write(finished_letter)
