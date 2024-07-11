from coffee_resources import MENU, resources

# this is a coffee making software
# resources report


def drink_choice():
    print()


def report(store, amount):
    print(f"Water: {store['water']}ml")
    print(f"Milk: {store['milk']}ml")
    print(f"Coffee: {store['coffee']}g")
    print(f"Money: ${amount}")


report(resources, amount=50)
