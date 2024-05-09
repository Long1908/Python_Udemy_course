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


def check_for_valid_input(my_input):
    if my_input not in list(MENU):
        return False
    else:
        return True


def check_recourse_sufficiency(the_user_order):
    sufficient = True
    for ingredient in MENU[the_user_order]["ingredients"]:
        if resources[ingredient] < MENU[the_user_order]["ingredients"][ingredient]:
            sufficient = False
    return sufficient


def money_count (u_quarters, u_dimes, u_nickles, u_pennies):
    return u_quarters * 0.25 + u_dimes * 0.10 + u_nickles * 0.05 + u_pennies * 0.01


def check_money(u_quarters, u_dimes, u_nickles, u_pennies, u_order):
    money_put = money_count(u_quarters, u_dimes, u_nickles, u_pennies)
    if money_put < MENU[u_order]["cost"]:
        return False
    else:
        return True


def working_coffee_machine(money_in_machine):
    # TODO 1: Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
    order = input("What would you like? (espresso/latte/cappuccino):").lower().strip()
    # TODO 2: Turn off the Coffee Machine by entering "off" to the prompt
    if order == "off":
        return money_in_machine
    # TODO 3: Print report.
    elif order == 'report':
        for resource in resources:
            print(f"{resource.title()}: {resources[resource]}ml")
        print(f"Money: ${money_in_machine}")
        working_coffee_machine(money_in_machine)
    else:
        while not check_for_valid_input(order):
            print("Sorry, we don't have that yet!")
            order = input("What would you like? (espresso/latte/cappuccino):").lower().strip()
        # TODO 4: Check resources sufficiency
        if not check_recourse_sufficiency(order):
            for resource in resources:
                if resources[resource] == 0:
                    print(f"Sorry there is no {resource}.")
            working_coffee_machine(money_in_machine)
        else:
            cost_of_order = MENU[order]["cost"]
            print(f"The order costs: ${cost_of_order}")
            # TODO 5: Process coins prompt
            quarters = int(input("How many quarters are you gonna put:"))
            dimes = int(input("How many dimes are you gonna put:"))
            nickles = int(input("How many nickles are you gonna put:"))
            pennies = int(input("How many pennies are you gonna put:"))
            # TODO 6: Check transaction successful?
            if not check_money(quarters, dimes, nickles, pennies, order):
                print("Sorry that's not enough money. Money refunded.")
                working_coffee_machine(money_in_machine)
            else:
                # TODO 7: Make Coffee.
                for ingredient in MENU[order]["ingredients"]:
                    resources[ingredient] -= MENU[order]["ingredients"][ingredient]
                print(f"Here is your {order}.")
                money_user_give = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
                money_change = money_user_give - MENU[order]["cost"]
                money_change = round(money_change, 2)
                print(f"You have putted: ${money_user_give}.")
                print(f"Here is your change: ${money_change}")
                money_in_machine += MENU[order]["cost"]
                return working_coffee_machine(money_in_machine)


beginning_money = 0
money = working_coffee_machine(beginning_money)
