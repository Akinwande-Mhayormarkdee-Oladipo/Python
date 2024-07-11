from coffee_resources import MENU, resources

# this is a coffee making software
# resources report


def drink_choice():
    print("Drinks available: Expresso, Latte, Cappuccino.")
    choice = input("Select a drink: ").lower()
    return choice


def compare_resource(store_qty, required_qty):
    should_continue = True
    for item in store_qty:
        if store_qty[item] < required_qty[item]:
            print(f"Sorry there is not enough {item}")
            should_continue = False
            return should_continue
    return should_continue


def report(store, amount):
    print(f"Water: {store['water']}ml")
    print(f"Milk: {store['milk']}ml")
    print(f"Coffee: {store['coffee']}g")
    print(f"Money: ${amount}")


def money_process():
    num_quarters = int(input("Enter number of quarters: "))
    num_dimes = int(input("Enter number of dimes: "))
    num_nickels = int(input("Enter number of nickels: "))
    num_pennies = int(input("Enter number of pennies: "))
    total_amount = num_quarters*0.25 + num_dimes*0.1 + num_nickels*0.05 + num_pennies*0.01
    return total_amount

def money_check(
        
)

report(resources, amount=50)
