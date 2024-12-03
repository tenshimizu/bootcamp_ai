# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

menu_dashes = "-" * 42

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to view different sections of the menu, so let's create a 
# continuous loop
    # Ask the customer which menu category they want to view
print("Which menu would you like to view? ")
    # Create a variable for the menu item number
i = 1
    # Create a dictionary to store the menu for later retrieval 
menu_items = {}
    # Print the options to choose from menu headings (all the first level 
    # dictionary items in menu).
        # Store the menu category associated with its menu item number
        # Add 1 to the menu item number
for menu_category_name, menu_category in menu.items():
    print(f"{i}. {menu_category_name}")
    menu_items[i] = menu_category_name
    i += 1


while True:
    # Get the customer's input
    menu_category = input("Type menu number to view or q to quit: ")

    # Exit the loop if user typed 'q'
    if menu_category == 'q':
        break
    # Check if the customer's input is a number
    elif menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            selected_menu_category = menu_items[int(menu_category)]
            print(f"You selected {selected_menu_category}")

            print(menu_dashes)
            print(f"This is the {selected_menu_category} menu.")
            print(menu_dashes)
            # Specified all the formatting so all dashes line up when printed
            print("{:<6} | {:<25} | {:<10}".format("Item #", "Item name", "Price"))
            print("-" * 42)

            # Initialize a menu item counter
            item_counter = 1
            # Print out the menu options from the menu_category_name
            for menu_item, menu_item_value in menu[selected_menu_category].items():
                # Iterate through the dictionary items
                if isinstance(menu_item_value, dict):
                    # Iterate through the dictionary items
                    for sub_item, sub_price in menu_item_value.items():
                        # Print the menu item
                        print("{:<6} | {:<25} | ${:<8.2f}".format(
                            item_counter, 
                            f"{menu_item} - {sub_item}", 
                            sub_price
                        ))
                        # Add 1 to the item_counter
                        item_counter += 1
                # Else the menu item is not a dictionary
                else:
                    # Print the menu item
                    print("{:<6} | {:<25} | ${:<8.2f}".format(
                        item_counter, 
                        menu_item, 
                        menu_item_value
                    ))
                    # Add 1 to the item_counter
                    item_counter += 1

            print(menu_dashes)
            input("Press enter to return to the main menu.")

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")
