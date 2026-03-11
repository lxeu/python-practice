import random
from GameData import data
from art import logo, vs

def get_account():
    return random.choice(data)

def format_account(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}."

def check_answer(guess, account_a, account_b):
    followers_a = account_a["follower_count"]
    followers_b = account_b["follower_count"]
    if followers_a < followers_b:
        return guess == "b"
    else:
        return guess == "a"

def play_game():
    score = 0
    game_not_over = True
    print(logo)
    account_a = get_account()
    account_b = get_account()
    while account_a == account_b:
        account_b = get_account()
    
    while game_not_over:
        print(f"Compare A: {format_account(account_a)}")
        print(vs)
        print(f"Against B: {format_account(account_b)}")
        
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        is_correct = check_answer(guess, account_a, account_b)
        if is_correct:
            account_a = account_b
            score += 1
            print(f"Correct! Your score is {score}")
            account_b = get_account()
            while account_a == account_b:
                account_b = get_account()
        else:
            print(f"Wrong! Your score was {score}")
            game_not_over = False

play_game()