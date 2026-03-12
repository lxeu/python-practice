from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffee_machine_on = True
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while coffee_machine_on:
    coffee = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee == "report":
        coffee_maker.report()
        money_machine.report()
    elif coffee == "off":
        coffee_machine_on = False
    else: 
        drink = menu.find_drink(coffee)
        if drink and coffee_maker.is_resource_sufficient(drink):
            payment_successful = money_machine.make_payment(drink.cost)
            if payment_successful:
                coffee_maker.make_coffee(drink)
