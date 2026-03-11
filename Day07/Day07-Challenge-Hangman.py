import random

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
word = random.choice(words)
win = False
lives = 7
used_letters = []

placeholder = ["_"] * len(word)
print("\n----------------------------------------")
print("Welcome to hangman! Try to guess all the letters in the word without running out of guesses.")
print(" ".join(placeholder))

while True:
    print(f"Words guessed: {', '.join(used_letters)}")
    guess = input("Guess a letter: ").lower()
    print("\n----------------------------------------")
    # Error check if input is not a letter or is longer than 1 letter.
    if not guess.isalpha() or len(guess) != 1:
        print("Enter a letter!")
        continue
    # Disallow user to put same letter twice
    if guess in used_letters:
        print("You already guessed that letter!")
        continue
    # Prevent user from guessing an already correct letter
    if guess in placeholder:
        print("You already correctly guessed this letter!")

    # Replace _ with letter if guess was in word
    for i in range(len(placeholder)):
        if guess == word[i]:
            placeholder[i] = guess
    # Remove life and add letter to guessed words if letter not in word
    if guess not in word:
        used_letters.append(guess)
        used_letters.sort()
        lives -= 1
    # If no more blanks user wins
    if "_" not in placeholder:
        print("You won!")
        print(f"The word was {word}!")
        break
    # Print each picture corresponding to user's remaining lives.
    if lives == 6 and guess not in placeholder:
        print(f"Uh oh, {guess} is not in the word")            
        print('''
  +---+
  |   |
      |
      |
      |
      |
=========''')
    elif lives == 5 and guess not in placeholder:
        print(f"Uh oh, {guess} is not in the word")
        print('''
  +---+
  |   |
  O   |
      |
      |
      |
=========''')
    elif lives == 4 and guess not in placeholder:
        print(f"Uh oh, {guess} is not in the word")
        print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''')
    if lives == 3 and guess not in placeholder:
        print(f"Uh oh, {guess} is not in the word")
        print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')
    if lives == 2 and guess not in placeholder:
        print(f"Uh oh, {guess} is not in the word")
        print('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''')
    if lives == 1 and guess not in placeholder:
        print(f"Uh oh, {guess} is not in the word")
        print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''')
    if lives == 0 and guess not in placeholder: 
        print(f"Uh oh, {guess} is not in the word")
        print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''')
        print("Game over! You ran out of guesses :(")
        print(f"The word was {word}.")
        break
    print(" ".join(placeholder))