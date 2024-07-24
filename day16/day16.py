from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


while True:
    prompt = input("What would you like? (espresso/latte/cappuccino/):")

    if prompt == "off":
        break
    elif prompt == "report":
        coffee_maker.report()
    elif prompt in menu.get_items():
        drink_info=menu.find_drink(prompt)
        print(drink_info)
        if coffee_maker.is_resource_sufficient(drink_info):
            if money_machine.make_payment(drink_info.cost):
                coffee_maker.make_coffee(drink_info)


