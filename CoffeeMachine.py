MENU = {
    "espresso" : {
        "ingredients":{
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {"ingredients":{
            "water": 200,
            "coffee": 24,
            "milk":150,
        },
        "cost": 2.5,},
    "cappuccino" : {
        "ingredients":{
            "water": 250,
            "coffee": 24,
            "milk":100,
        },
        "cost": 3.5,
    }  
}

resource = {
    "water" : 300,
    "milk":200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    """ Returns true if order can be made otherwise false."""
    for item in order_ingredients:
       if order_ingredients[item] >= resource[item]:
           print(f"Sorry there is not enough {item}.")     
           return False
    return True

def process_coins():
    """ Returns the total calculated from coins inserted """
    print("Please insert coins.")
    total = int(input("How many quaters?: "))* 0.25
    total += int(input("How many dimes?: "))* 0.1
    total += int(input("How many nickels?: "))* 0.05
    total += int(input("How many pennies?: "))* 0.01
    return total
    
def is_transaction_successful(money_received,drink_cost):
    """ Returns True when the payment is accepted, or False if money is insufficient. """
    if money_received >= drink_cost :
        change = money_received - drink_cost
        print(f"Here is ${round(change,2)} in change.")
        global profit 
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money will be refunded.")
        return False


def make_coffee(drink_name,order_ingredients):
    """ Deduct the required ingredients from the resources. """
    for item in order_ingredients:
        resource[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕.")

is_on = True
profit = 0
while is_on:
    choice = input("What would you like?(espresso/latte/cappuccino)")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water : {resource['water']}")
        print(f"Milk  : {resource['milk']}")
        print(f"Coffee: {resource['coffee']}")
        print(f"Money: {profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])
            
    