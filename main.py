from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo, fin

power = True
menu = Menu()
coffee_maker = CoffeeMaker()
money = MoneyMachine()

print(logo)

while power:
    print("="*110)
    print("Note: type 'report' to generate report of the current coffee machine resources, 'off' to turn off the program")
    print("-"*110)

    user_input = input(f"What would you like? {menu.get_items()}: ").lower()

    if user_input == "off": 
        coffee_maker.report()
        power = False
        print(fin)
    elif user_input == "report":
        coffee_maker.report()
        power = True
    else:
        drink = menu.find_drink(user_input)
        sufficient = coffee_maker.is_resource_sufficient(drink)
        # print(coffee_maker.is_resource_sufficient(drink))

        if sufficient == True:
            print(f"{drink.name}: ${drink.cost}")
            money.make_payment(drink.cost)

            coffee_maker.make_coffee(drink)

            print(money.report())
    #after fetching user input return the menu item

