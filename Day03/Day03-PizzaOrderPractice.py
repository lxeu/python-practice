print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

cost = 0

# size selection
if size == "S": 
    cost += 15
elif size == "M": 
    cost += 20
elif size == "L":
    cost += 25
else:
    print("Please enter a valid size.")

# pepperoni selection $2 on small $3 on medium or large
if pepperoni == "Y":
    if size == "S":
        cost += 2
    if size == "M" or size == "L":
        cost += 3

# extra cheese selection
if extra_cheese == "Y":
    cost += 1

print(f"Your final bill is ${cost}")