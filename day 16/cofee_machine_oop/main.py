from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_machine_on = True

coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while is_machine_on:
    user_input = input(f"What would you like? ({menu.get_items()}): ")
    if user_input == "off":
        is_machine_on = False
    elif user_input == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_input)
        if drink is not None:
            if coffe_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffe_maker.make_coffee(drink)
                    coffe_maker.report()
                    money_machine.report()
                else:
                    print("Payment insufficient. Transaction canceled.")
            else:
                print(f"Sorry, not enough resources to make {drink.name}.")
        else:
            print("Item not found")