## list of items
inventory_list = [
    {'Item No.': 1, 'item_name': 'Eggs', 'Stock': 25, 'Price': 20000},
    {'Item No.': 2, 'item_name': 'Milk', 'Stock': 10, 'Price': 15000},
    {'Item No.': 3, 'item_name': 'Bread', 'Stock': 30, 'Price': 7000},
    ]


## Function to display items (Read)
def display_list_items():
    print('\n \t BetaMart Inventory List \n')    
    print('No.:\t nama_item:\t Stock:\t Price:\n')
    for item in inventory_list:
        print(f"{item['Item No.']} \t {item['item_name']} \t\t {item['Stock']} \t {item['Price']}")
    print('')


## Function add items (Create)
def add_items():
    print()
    while True:
        num_of_items = input("How many items would you like to add? (type '0' to cancel) ")
        if not num_of_items.isdigit():
            print('\ninput invalid\n')
        else:
            break

    print()
    num_of_items = int(num_of_items)
    print()

    for i in range(1, num_of_items+1):
        checker = True
        while checker == True:
            input_item_no = input('Insert new item Number: ')
            if not input_item_no.isdigit():
                print('\nInput invalid, please try again.\n')
                input_item_no
                continue
            else:
                input_item_no = int(input_item_no)
                for j in range(len(inventory_list)):
                    if input_item_no == (inventory_list[j]['Item No.']):
                        print("Item number already in inventory list!")
                        break
                    elif j == len(inventory_list)-1: 
                        input_item_no = int(input_item_no)
                        checker = False
                    
        while True:
            input_item_name = input('Insert new item name: ').title()
            if input_item_name != '':
                break

        while True:
            input_stock = input('Insert new item stock: ')
            if not input_stock.isdigit():
                print('\nInput invalid, please try again.\n')
            else:
                break 

        while True:
            input_price = input('Insert new item price: ')
            if not input_price.isdigit():
                print('\nInput invalid, please try again.')
            else:
                break 

        print('')
        print('New item has been added:')
        print('No.:\t nama_item:\t Stock:\t Price:')
        print(f"{input_item_no} \t {input_item_name} \t\t {input_stock} \t {input_price}")
        print('')

        inventory_list.append({'Item No.': int(input_item_no), 'item_name': input_item_name, 'Stock': int(input_stock), 'Price': int(input_price)})


## Function del items (Delete)
def del_items():
    while True:
        input_item_no = input('\nInsert the Item Number to be deleted: ')
        if not input_item_no.isdigit():
            print('\ninput invalid\n')
            continue
        else:
            input_item_no = int(input_item_no)
            break

    while True:
        input_item_no = int(input_item_no)
        for i in range(len(inventory_list)):
            if input_item_no == (inventory_list[i]['Item No.']):
                while True:
                    confirmation = input(f"\nAre you sure you want to delete everything in item '{inventory_list[i]['item_name']}'(Y/N): ").lower()
                    if confirmation in ['y', 'n']:
                        break
                if confirmation == 'y':
                    del inventory_list[i]
                    print(f"Item has been removed.")
                elif confirmation == 'n':
                    del_items()
                    break
                else:
                    print('\nInput invalid, please try again.\n')
                break
            elif i == len(inventory_list)-1:
                print(f'\nItem does not exist with the Item Number "{input_item_no}"')
                continue
        break      


## Function purchase (Update) --> will update stock after purchase confirmation
virtual_cart = []
def purchase_items():
    while True:
        input_item_no = input('\nInsert the Item Number to be added to cart: ')
        if not input_item_no.isdigit():
            print('\ninput invalid\n')
            continue
        else:
            input_item_no = int(input_item_no)
            break
    while True:
        input_item_no = int(input_item_no)
        for i in range(len(inventory_list)):
            if input_item_no == (inventory_list[i]['Item No.']):
                while True:
                    confirmation = input(f"\nAre you sure you want to add this Item '{inventory_list[i]['item_name']}' to cart? (Y/N):    ").lower()
                    if confirmation in ['y', 'n']:
                        break
                if inventory_list[i]['Stock'] == 0:
                        print('\n\nSorry, the item is out of stock.\n')
                        purchase_items()
                elif confirmation == 'y':
                    virtual_cart.append({
                        'Item No.': inventory_list[i]['Item No.'], 
                        'item_name': inventory_list[i]['item_name'],
                        'Price': inventory_list[i]['Price']})
                    print(f"\nItem has been added to cart\n")

                    while True:
                        item_amount = input('Insert the amount of items to be purchased: \n')
                        if not item_amount.isdigit():
                            print('\ninput invalid\n')
                            continue
                        else:
                            item_amount = int(item_amount)
                            if item_amount > inventory_list[i]['Stock']:
                                print('Amount too large, stock is not enough for the amount requested.\n\n')
                                continue
                            elif item_amount < inventory_list[i]['Stock'] or item_amount == inventory_list[i]['Stock']:
                                (virtual_cart[0])['Amount'] = item_amount
                                break

                elif confirmation == 'n':
                    purchase_items
                else:
                    print('\nInput invalid, please try again.\n')
                break
            elif i == len(inventory_list)-1:
                print(f'\nItem does not exist with the Item Number "{input_item_no}"')
                continue       
        break

    print()
    print('---------------CART-----------------')
    print('No.:\t nama_item:\tAmount:\t Price:')
    for v in virtual_cart:
        print(f"{v['Item No.']} \t {v['item_name']} \t\t {v['Amount']} \t {v['Price']}")
        break

    for v in virtual_cart:
        total_price = v['Amount'] * v['Price']
        break
    print(f'Total Price to be paid: {total_price}')
    total_price

    while True:
        money = int(input('Insert money amount: '))

        if money > total_price:
            money_left = money - total_price
            print(f'\nThank you. Here is your change of {money_left}')
            inventory_list[i]['Stock'] = (inventory_list[i]['Stock']) - item_amount
            virtual_cart.clear()
            break

        elif money < total_price:
            money_needed = total_price - money
            print(f'\nInsufficient funds. You need {money_needed} more to buy. Please enter the amount of money that is sufficient.')
            continue

        elif money == total_price:
            money_left = money - total_price
            print(f'\nThank you. The amount of paid is exact.')
            inventory_list[i]['Stock'] = (inventory_list[i]['Stock']) - item_amount
            virtual_cart.clear()
            break

## Sub menu 3 
def sub_menu_2():
    while True:
        user_input = input('''
        Would you like to Add new items or Remove items from the inventory?

        1. display current items
        2. add items
        3. remove items
        4. cancel and return to main menu
        
        Insert number:  ''')

        if user_input == '1':
            display_list_items()
        elif user_input == '2':
            add_items()
        elif user_input == '3':
            del_items()
        elif user_input == '4':
            break
        else:
            print('\nInvalid input.')


## Sub menu 
def sub_menu_3():
    while True:
        user_input = input('''
        Purchasing Items from BetaMart Simulator

        1. view BetaMart
        2. Purchase items
        3. cancel and return to main menu
        
        Insert number:  ''')

        if user_input == '1':
            display_list_items()
        elif user_input == '2':
            purchase_items()
        elif user_input == '3':
            break
        else:
            print('\nInvalid input.')


def main_menu():
    while True:
        menu = input('''
        Welcome to BetaMart:

        1. View Current Inventory
        2. Add or Remove items from inventory
        3. Purchase Items Simulation
        4. Exit

        Please insert menu number:  ''')
        if menu == '1':
            display_list_items()
        elif menu == '2':
            sub_menu_2()
        elif menu == '3':
            sub_menu_3()
        elif menu == '4':
            break
        else:
            print('\nInvalid input.')


main_menu()