print("Welcome to the tip calculator!")
total = int(input("What was the total bill? $"))
tip = int(input("How much % tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
cost = 0

# Add tip to total cost
tip = tip/100 + 1
total *= tip

# Cost split evenly rounded to two decimal places.
cost = (round(total/people, 2))

print(f"Each person should pay: ${cost}")