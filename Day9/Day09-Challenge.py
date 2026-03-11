import gravelart

print(gravelart.art)
print("Welcome to the secret auction program.")

bidders = {}

while True:
    name = input("What is your name? ")
    bid = input("What's your bid? $")
    more_bid = input("Are there any extra bidders? ").lower()
    # Error check if amount is an integer
    if not bid.isdigit():
        print("Enter a number")
        continue
    else:
        bid = int(bid)

    bidders[name] = bid

    if more_bid == "yes":
        print("\n" * 100)
        continue
    elif more_bid == "no":
        break
    else:
        print("Enter yes or no.")


largest_bid = 0
winner = ""
# Find highest bidder
for i in bidders:
        if bidders[i] > largest_bid:
            largest_bid = bidders[i]
            winner = i
print(f"The winner is {winner} with the highest bid of {largest_bid}!")