
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
}

# todo 3: calculating the exchange


def exchange(total_coins, coffee_selected):
    price = coffee_selected["cost"]

    if total_coins >= price:
        change = round(total_coins - price, 2)
        print(f"You gave ${total_coins}, Here is you change ${change}")
        return change


# todo 4: manage the resources
def qte_resources(q_resources,  ingredient):

    for item in ingredient:
        q_resources[item] = q_resources[item] - ingredient[item]
#    print(f"resources left {q_resources}")
    return q_resources


def check_resources(resources_remaining, ingredient):
    not_enough = False
    for item in ingredient:
        if resources_remaining[item] < ingredient[item]:
            print(f"Sorry there is not enough {item}.")
            not_enough = True
        return not_enough

# todo 2: inserting coins.


def insert_coin():
    print("Please insert coins.")
    quarter = 0.25*int(input("how many quarters?:"))
    dimes = 0.1*int(input("how many dimes?:"))
    nickles = 0.05*int(input("how many nickles?:"))
    pennies = 0.01*int(input("how many pennies?:"))
    t_coins = round(quarter + dimes + nickles + pennies, 2)
    return t_coins

# todo 1: select the coffee in the menu list


resources_left = resources
enough = False
again = True
coins = 0
machine_coins = 0
resources_left["Money"] = machine_coins

while not enough:

    while again:
        #   print("total money in the coffee machine:$", machine_coins)
        choose_coffee = input("What would you like? (espresso/latte/cappuccino):").lower()
        if choose_coffee == "report":
           print(f"Water:{resources_left['water']}ml\nMilk: {resources_left['milk']}ml\nCoffee: {resources_left['coffee']}g\nMoney: ${resources_left['Money']}")
           choose_coffee = input("What would you like? (espresso/latte/cappuccino):").lower()
        coffee = MENU[choose_coffee]
        ingredients = coffee["ingredients"]
        coffee_price = coffee["cost"]
        enough = check_resources(resources_left, ingredients)
        if not enough:
            coins = insert_coin()
            exchange(coins, coffee)

        if coins >= coffee_price:

            if not enough:

                resources_left = qte_resources(resources, ingredients)
                print(f"Here is your {choose_coffee}☕. Enjoy!")
                coins = 0
                resources_left['Money'] += coffee_price

        elif coins <= coffee_price and not enough:
            print(f"The {choose_coffee } costs: ${coffee_price}, you gave ${coins}, Money refund.")
            coins = 0
