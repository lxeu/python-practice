import random

print("Welcome to guess the number!")
print("I'm thinking of a number from 1 to 100.")
difficulty = input("Choose a difficulty (Easy or Hard): ").lower()

# Give user 5 guesses for hard and 10 for easy.
num = random.randint(1,100)
if difficulty == "easy":
    guesses = 10
else:
    guesses = 5

game_over = False

print(f"You have {guesses} to guess the number. Good luck!")

# Check if user guesses number of not and if not give higher or lower hint
def check_guess(guess):
    global game_over
    if guess == num:
        print(f"You guess it! The number was {num}.")
        game_over = True
    elif guess > num:
        print("Too high! Guess again.")
    else:
        print("Too low! Guess again.")

while not game_over:
    guess = int(input("Make a guess: "))
    guesses -= 1
    if guesses == 0:
        print("You ran out of guesses!")
        game_over = True
    else:
        check_guess(guess)