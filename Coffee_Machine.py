coffees = [
    {"name": "Cappuccino",
     "cost": 3,
     "milk": 100,
     "water": 250,
     "coffee": 24
     },
    {"name": "Espresso",
     "cost": 1.5,
     "milk": 50,
     "water": 50,
     "coffee": 18
     },
    {"name": "Latte",
     "cost": 2.5,
     "milk": 150,
     "water": 20,
     "coffee": 24
     }
]




process = True

resources = {
    "milk": 60,
    "water": 50,
    "coffee": 100,
    "money": 0
}


def change_resources(milk, water, coffee, shift):
    global resources
    if shift == "use":
        resources["milk"] -= milk
        resources["water"] -= water
        resources["coffee"] -= coffee
    if shift == "top-up":
        resources["milk"] += milk
        resources["water"] += water
        resources["coffee"] += coffee


def compare_resources(milk_needed, water_needed, coffee_needed):
    if milk_needed > resources["milk"]:
        print("Sorry. There isn't enough milk to process your request at this time.")
        return False
    elif water_needed > resources["water"]:
        print("Sorry. There isn't enough water to process your request at this time.")
        return False
    elif coffee_needed > resources["coffee"]:
        print("Sorry. There isn't enough coffee to process your request at this time.")
        return False
    else:
        return True


logo = '''
       .
                        `:.
                          `:.
                  .:'     ,::
                 .:'      ;:'
                 ::      ;:'
                  :    .:'
                   `.  :.
          _________________________
         : _ _ _ _ _ _ _ _ _ _ _ _ :
     ,---:".".".".".".".".".".".".":
    : ,'"`::.:.:.:.:.:.:.:.:.:.:.::'
    `.`.  `:-===-===-===-===-===-:'
      `.`-._:                   :
        `-.__`.               ,' 
    ,--------`"`-------------'--------.
     `"--.__                   __.--"'
            `""-------------""'
'''


def buy_coffee(coffee_type, milk_added):
    if coffee_type == "espresso":
        selected = coffees[1]
    elif coffee_type == "cappuccino":
        selected = coffees[0]
    elif coffee_type == "latte":
        selected = coffees[2]
    else:
        print(f'Milk remaining: {resources["milk"]}mL')
        print(f'Water remaining: {resources["water"]}mL')
        print(f'Coffee remaining: {resources["coffee"]}mL')
        print(f'Money earned: ${resources["money"]}')

        increase_needed = input("Would you like to top-up the machine? [Y/N]: ").lower()

        if increase_needed == "y":
            milk = int(input("How much milk would you like to add?(in mL): "))
            water = int(input("How much water would you like to add?(in mL): "))
            coffee = int(input("How much coffee would you like to add?(in g): "))
            change_resources(milk, water, coffee, "top-up")
        return 100

    cost = selected["cost"]
    water_needed = selected["water"]
    coffee_needed = selected["coffee"]

    if milk_added == "y":
        milk_needed = selected["milk"]
    else:
        milk_needed = 0

    message = compare_resources(milk_needed, water_needed, coffee_needed)
    if message:
        sugar_needed = input("Would you like some sugar in the coffee? [Y/N]: ").lower()
        if sugar_needed == "y":
            cost += 0.5
        size = input("What size would you prefer? [S/M/L]: ").lower()
        if size == "l":
            cost += 1
        elif size == "m":
            cost += 0.5

        return cost

    else:
        return 0


def payment(cost, pennies, nickels, dimes, quarters):
    penny = 0.01
    nickel = 0.05
    dime = 0.1
    quarter = 0.25

    paid = (pennies * penny) + (nickels * nickel) + (dimes * dime) + (quarters * quarter)

    if paid < cost:
        print("Not enough money paid. Coffee Refunded. Please try again.")

    elif paid == cost:
        print("Thank you for the payment. Enjoy your coffee ☕! 😊")
        resources["money"] += cost

    else:
        change = paid - cost
        resources["money"] += cost
        print(f"Thank you for the payment. ${change} has been given back as change. Enjoy your coffee ☕! 😊")


while process:
    print("Welcome to this coffee machine!")
    print(logo)
    coffee_type = input("What kind of coffee would you like? [espresso/cappuccino/latte]: ").lower()
    milk_added = input("Would you like to add milk to your coffee?[Y/N]: ").lower()
    cost = buy_coffee(coffee_type, milk_added)
    if cost != 0 and cost != 100:
        print(f"Please pay ${cost}.")
        pennies = int(input("How many pennies? "))
        nickels = int(input("How many nickels? "))
        dimes = int(input("How many dimes? "))
        quarters = int(input("How many quarters? "))

        payment(cost, pennies, nickels, dimes, quarters)

        cont_process = input("Would you like to buy another coffee? [Y/N]: ").lower()
        if cont_process == "n":
            process = False

    elif cost == 100:
        print("Changes made.")
        print(f'Milk remaining: {resources["milk"]}mL')
        print(f'Water remaining: {resources["water"]}mL')
        print(f'Coffee remaining: {resources["coffee"]}mL')
        print(f'Money earned: ${resources["money"]}')
        cont_process = input("Would you like to buy a coffee? [Y/N]: ").lower()
        if cont_process == "n":
            process = False
    else:
        process = False

print("Thank you for using this coffee machine! :)")

