MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def resources_sufficient(d):
    for i in d:
        if d[i] <= resources[i]:
            continue
        else:
            print(f"Sorry there is not enough {i}")
            return False
    return True


def process_coins():
    money = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    if money == MENU[choice]["cost"]:
        resources["money"] = money
        print(money)
        return True
    elif money > MENU[choice]["cost"]:
        resources['money'] = MENU[choice]["cost"]
        print(money)
        print(f"Here is your balance.{round(money - MENU[choice]["cost"], 2)}")
        return True
    else:

        return False


def make_coffee(d):
    for i in d:
        resources[i] -= d[i]


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "report":
        print(
            f"Water: {resources["water"]}\nMilk: {resources["milk"]}\n Coffee: {resources["coffee"]}\nMoney: {resources["money"]}")
    elif choice in ["espresso", "latte", "cappuccino"]:
        d = MENU[choice]["ingredients"]
        if resources_sufficient(d):
            print("Please insert coins")
            quarters = int(input("How many quarters?"))
            dimes = int(input("How many dimes?"))
            nickels = int(input("How many nickles?"))
            pennies = int(input("How many pennies?"))
            if process_coins():
                make_coffee(d)
                print(f"Here is your {choice}. Enjoy! ☕")
            else:
                print("Sorry, that's not enough money. Money refunded")
    elif choice == "off":
        is_on = False
    else:
        print("invalid response")
