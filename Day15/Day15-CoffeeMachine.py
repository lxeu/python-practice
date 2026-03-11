from CoffeeData import menu, resources
coffee_machine_on = True
# Total money made
profit = 0
# Total coin value
total = 0

# print remaining resources
def report(resources):
    global profit
    print(f'Water: {resources["water"]}')
    print(f'Milk: {resources["milk"]}')
    print(f'Coffee: {resources["coffee"]}')
    print(f'Money: ${profit}')

# Logic to detect if enough resources remain
def check_resources(resources, menu, coffee):
    for ingredient, amount in menu[coffee]["ingredients"].items():
        if resources[ingredient] < amount:
            print(f"Not enough {ingredient} to make {coffee}")
            return False
    return True

# Prompts user to insert coins and check if there is enough
def check_money():
    print("Please insert coins")
    global total
    # catch value error if non-integer entered
    try:
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickels = int(input("How many nickels? "))
        pennies = int(input("How many pennies? "))
        total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
        return total
    except:
        print("Enter a number!")
        return False
    
# subtract used resources
def remove_resources(resources, menu, coffee):
    for ingredient, amount in menu[coffee]["ingredients"].items():
        resources[ingredient] -= amount

def refill_machine(resources):
    refill = input("What would you like to refill? (water, milk, or coffee): ")
    try:
        amount = int(input("How much amount would you like to add? "))
        resources[refill] += amount
    except:
        print("Enter a number")

while coffee_machine_on:
    coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if coffee == "report":
        report(resources)

    if coffee == "espresso" or coffee == "latte" or coffee == "cappuccino":
        cost = menu[coffee]["cost"]
        if check_resources(resources, menu, coffee):
            check_money()
            if total >= cost:
                print(f"Here is your {coffee}. Enjoy!")
                print(f"You receieved {round(total - cost, 2)} in change!")
                remove_resources(resources, menu, coffee)
                profit += cost
            else:
                print(f"Not enough money! You are ${round(total - cost, 2)} short!")
        else:
            continue

    if coffee == "refill":
        refill_machine(resources)

    if coffee == "off":
        coffee_machine_on = False
