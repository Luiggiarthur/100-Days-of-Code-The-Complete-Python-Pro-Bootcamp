from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

while True:
    options = menu.get_items()
    choice = input(f"What would you like? ({options})").lower()
    drink = menu.find_drink(choice)
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == drink.name:
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
