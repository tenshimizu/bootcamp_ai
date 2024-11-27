# Create a tuple containing the names of menu sections:
# snacks, meals, drinks, and dessert.
menu_tuple = ('snacks', 'meals', 'drinks', 'dessert')

# Print the tuple.
print(menu_tuple)

# Create a list of items for one of the menu sections.
snacks_list = ['chips', 'nuts', 'popcorn', 'candy']

# Create a list of prices for each of the menu items in the previous list.
snacks_prices = [1.50, 2.00, 2.50, 3.00]

# Ask a user to input a new item and append it to the relevant list.
snacks_list.append(input('Enter a new snack item: '))

# Ask a user to input the price of the new item, referenced using list indexing
# and append it to the relevant list.
snacks_prices.append(float(input('Enter the price of the new snack item: ')))

# Print the menu and prices.
print(snacks_list,snacks_prices)

# Ask the user which item to remove from the menu.
item_to_remove = input('Enter the item to remove from the menu: ')

# Find the index of the item and save it as a variable.
item_index = snacks_list.index(item_to_remove)

# Remove the item from the menu list using remove().
snacks_list.remove(item_to_remove)

# Remove the item from the prices list using pop().
snacks_prices.pop(item_index)

# Print the menu and prices again to confirm removal.
print(snacks_list, snacks_prices)

# Find the most expensive price on the menu.
print(max(snacks_prices))

# Find the cheapest price on the menu.
print(min(snacks_prices))

# Find the cost if someone bought every item on the menu.
print(sum(snacks_prices))   

# Confirm that the menu and prices lists are the same length.
if len(snacks_list) == len(snacks_prices):
    print('The menu and prices lists are the same length.')