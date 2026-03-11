import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
dealer_cards = []

# Dealer draw function
def dealer_draw(dealer_cards, dealer_total):
    while dealer_total <= 16:   # keep drawing until 17+
        dealer_cards.append(random.choice(cards))
        dealer_total = sum(dealer_cards)
    # Ace conversion logic
    while dealer_total > 21 and 11 in dealer_cards:
        dealer_cards[dealer_cards.index(11)] = 1
        dealer_total = sum(dealer_cards)
    return dealer_cards, dealer_total

# User draw function
def user_draw(user_cards, user_total):
    user_cards.append(random.choice(cards))
    user_total = sum(user_cards)
    # Ace conversion logic
    while user_total > 21 and 11 in user_cards:
        user_cards[user_cards.index(11)] = 1
        user_total = sum(user_cards)
    return user_cards, user_total
# Check winner
def check_winner(user_total, computer_total):
    if user_total > 21:
        return "Bust! Dealer wins!"
    elif computer_total > 21:
        return "Dealer busts! You win!"
    elif user_total > computer_total:
        return "You win!"
    elif computer_total > user_total:
        return "Dealer wins!"
    else:
        return "Tie"

# Loop for replayability
while True:
    choice = input("Would you like to play a game of blackjack? (yes or no) ").lower()
    if choice == "yes":
        user_cards = []
        dealer_cards = []

        for i in range(2):
            user_cards.append(random.choice(cards))
            dealer_cards.append(random.choice(cards))
        print(f"Your cards: {user_cards}")
        print(f"Dealer's first card: [{dealer_cards[0]}, ?]")
        user_total = sum(user_cards)
        dealer_total = sum(dealer_cards)
        hit_or_stand = input("Would you like to hit or stand? ")
        # Allow user to hit until bust or sum reaches 21
        while hit_or_stand == "hit":
            user_cards, user_total = user_draw(user_cards, user_total)
            print(f"Your cards: {user_cards} total = {user_total}")
            if user_total == 21:
                break
            if user_total > 21:
                break
            hit_or_stand = input("Would you like to hit or stand? ")
        # Call dealer draw function every turn.
        if user_total <= 21:
            dealer_cards, dealer_total = dealer_draw(dealer_cards, dealer_total)
        print(f"Dealer cards: {dealer_cards} total = {dealer_total}")

        print(check_winner(user_total, dealer_total))
    else:
        break