def take_order():
    # Take input of an item the user wants to purchase
    item = input("Hello! What would you like to order? ")
    # Ask how much the item costs and cast it as a number.
    # What type of number should it be cast as?
    cost = float(input(f"How much does {item} cost? "))
    # Ask what quantity of the item should be purchased and cast it as a number.
    # What type of number should it be cast as?
    quantity = int(input(f"How many {item} would you like? "))
    # Print the item cost along with its data type
    # Print the item quantity along with its data type
    print(f"Fantastic! Each {item} costs {cost}.\nYour total will be ${round(cost * quantity,2)}.\nThe data types for cost and quantity are cost:{type(cost)} and quantity:{type(quantity)}")

# Print results
take_order()