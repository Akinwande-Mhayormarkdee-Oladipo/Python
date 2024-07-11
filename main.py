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


def money_check(amount, required_store):
    if amount < required_store['cost']:
        print('Sorry that is not enough money. Money refunded.')
    else:
        change = amount-required_store['cost']
        print(f"Here is ${0:.2f} in change.".format(change))
        return amount


def coffee_maker():
    machine_switch = True
    available_items = resources
    machine_amount = 0
    while machine_switch:

        coffee_type = drink_choice()
        while coffee_type != 'espresso' and coffee_type != 'latte' and coffee_type != 'cappuccino':
            print(f"You've chosen {coffee_type}")
            if coffee_type == 'off':
                print("Bye!")
                machine_switch = False
                break
            coffee_store = MENU["coffee_type"]
            if coffee_type == 'report':
                report(available_items, machine_amount)






