from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



coffee_maker_obj = CoffeeMaker()
menu_obj = Menu()
money_obj = MoneyMachine()

is_on = True
profit = 0
while is_on:
    choice = input(f"What would you like? {menu_obj.get_items()}")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker_obj.report()
        money_obj.report()
    else:
        drink = menu_obj.find_drink(choice)
        """check 
        if coffee_maker_obj.is_resource_sufficient(drink):
            payment = money_obj.process_coins()
            if money_obj.make_payment(payment,):
                coffee_maker_obj.make_coffee(choice)"""
            
    