from coffee_resources import MENU, resources
# this is a coffee making software
# resources report


def drink_choice():
    print("Drinks available: Espresso, Latte, Cappuccino.")
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
    print("\nAvailable Resources: ")
    print(f"Water: {store['water']}ml")
    print(f"Milk: {store['milk']}ml")
    print(f"Coffee: {store['coffee']}g")
    print(f"Money: ${amount} \n")


def money_process():
    num_quarters = int(input("Enter number of quarters: "))
    num_dimes = int(input("Enter number of dimes: "))
    num_nickels = int(input("Enter number of nickels: "))
    num_pennies = int(input("Enter number of pennies: "))
    total_amount = num_quarters*0.25 + num_dimes*0.1 + num_nickels*0.05 + num_pennies*0.01
    return total_amount


def money_check(amount, required_coffee):
    switch = True
    while amount < required_coffee['cost']:
        switch = True
        print('Sorry that is not enough money. Money refunded.')
        choice = input("Enter \"yes\" to insert other amount or \"no\" to cancel your order: ")
        if choice.lower() == 'no':
            print("Bye!")
            switch = False
            return [amount, switch]
        else:
            amount = money_process()

    change = amount-required_coffee['cost']
    print(f"You need to pay ${required_coffee['cost']}")
    print(f"You paid ${amount}")
    print(f"Here is ${change:.2f} in change.")
    return [amount, switch]


def make_coffee(resources_available, coffee_resources):
    for items in resources_available:
        resources_available[items] -= coffee_resources[items]


def coffee_maker():
    machine_switch = True
    available_items = resources
    machine_amount = 0
    coffee_type_bank = MENU
    while machine_switch:
        coffee_type = drink_choice()
        process_switch = True
        while process_switch:
            # check coffee type prompt.
            while coffee_type != 'espresso' and coffee_type != 'latte' and coffee_type != 'cappuccino':
                if coffee_type == 'off':
                    print("Bye!")
                    machine_switch = False
                    return
                # coffee_store = MENU[coffee_type]
                elif coffee_type == 'report':
                    report(available_items, machine_amount)
                    coffee_type = drink_choice()
                else:
                    print("Unknown coffee type. Try again")
                    coffee_type = drink_choice()
            print(f"You've chosen {coffee_type}")
            selected_coffee = coffee_type_bank[coffee_type]
            print(selected_coffee)
            print(f"You've chosen {coffee_type}")
            enough_resources = compare_resource(available_items, selected_coffee["ingredients"])
            if not enough_resources:
                # check if available resources are able to make at least one coffee type
                for coffee_type in coffee_type_bank:
                    resource_per_coffee = coffee_type["ingredients"]
                    enough_resources = compare_resource(available_items, resource_per_coffee)
                if not enough_resources:
                    print("Sorry, we are out of stock for all coffee types.")
                    return
                else:
                    print("We are out of stock for some coffee types.")
                    print("Please choose different coffee types.")
                    continue

            print("Please insert coins: ")
            machine_amount = money_process()
            print(f"Money amount: {machine_amount}")
            check_result = money_check(machine_amount, selected_coffee)
            machine_amount = check_result[0]
            process_switch = check_result[1]
            if not process_switch:
                break

            make_coffee(available_items, selected_coffee["ingredients"])
            print(f"Here is your {coffee_type}. Enjoy! \n\n")
            process_switch = False


# start the coffee machine program.
coffee_maker()
