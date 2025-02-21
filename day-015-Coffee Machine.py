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
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
is_on=True
def is_resource_sufficient(order_ingredients):
    is_enough= True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough= False
    return True
def process_coins():
    """returns the total calculated and coins inserted."""
    print("Insert some coins.")
    total=int(input("How many quarters?: ")) * 0.25
    total+=int(input("How many dime?: ")) * 0.10
    total+=int(input("How many nickels?: ")) * 0.05
    total+=int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_success(money_received,drink_cost):
    """Return True when payment is accepted, or False if money is insufficient. """
    if money_received>=drink_cost:
        change=round(money_received-drink_cost,2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name,order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {drink_name} ☕")

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice =="off":
        is_on = False
    elif choice=="report":
       print(f"water:{resources['water']}ml")
       print(f"milk: {resources['milk']}ml")
       print(f"coffee: {resources['coffee']}g")
       print(f"Money : ${profit}")
    else:
        drink=MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment=process_coins()
            if is_transaction_success(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])



