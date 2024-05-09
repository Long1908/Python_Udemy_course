from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
#The whole project is using allready given modules. In needs a good reading and understanding of what kind of arguments and methods have the modules and we just finish the main.py


def make_coffee(machine, money):
    item = Menu()
    order = input(f"What would you like {item.get_items()}:")
    if order == "report":
        machine.report()
        money.report()
    elif order == "off":
        return
    else:
        coffee = item.find_drink(order)
        while coffee is None:
            order = input(f"What would you like {item.get_items()}:")
            coffee = item.find_drink(order)
        if machine.is_resource_sufficient(coffee):
            print(f"The price of the {coffee.name} is ${coffee.cost}")
            if money.make_payment(coffee.cost):
                machine.make_coffee(coffee)#as we can see our function is named like the method from one of our moduls. This is not a good practice, but it works cause the method has only one argument while our function has two. Which means that the interpeter reads it as two different callings
    return make_coffee(machine, money)#we are parsing the objects, otherwise the money and the resources of the machine will not change


machine_ingredients = CoffeeMaker()
machine_money = MoneyMachine()
make_coffee(machine_ingredients, machine_money) #we are parsing the objects, otherwise the money and the resources of the machine will not change
#if we used while then the resources and money will be changed by it self.
#But if we use function as we remember, then the functions are like their own blocks and they do not change global variables.
#So that is why parsing it for the sake of this exercises it's crucial to use functions to make it work