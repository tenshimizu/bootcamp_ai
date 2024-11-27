def loopy():
    # Declare lists
    rides = []
    prices = []

    # Continuous loop
        # Keep adding rides until exiting loop
        # Continuous loop
            # Prompt user for the cost of the ride
            # Check if the input is a number
                # Check if the input is less than or equal to 15
                    # Convert the input to a float and append it to the prices list
                    # Exit the loop

    while True:
        ride = input("Enter a ride name: ")
        rides.append(ride)
        price = float(input("Enter the cost of the ride: "))
        if price <= 15:
            prices.append(price)
        if price > 15:
            print("Error: Price must be less than or equal to $15.")

    # Ask the user if they wish to quit, and break the loop if they type 'q'
        quit_check = input("Do you wish to continue? Press enter to continue or 'q' to quit: ")
        if quit_check.lower() == "q":
            break
        else:
            continue

    print(rides,prices)
    # Loop through the rides and prices lists by finding the length of rides
        # Set the discount variable to False
        # Check if the price is greater than $5
            # Update the price to include a 10% discount
            # Set the discount variable to true
        # Print the ride name and price, with the price formatted to 2 decimal places
        # If a discount was applied, print a message that says this
    for i in range(len(rides)):
        discount = False
        if prices[i] > 5:
            prices[i] = prices[i] * 0.9
            discount = True
        print(f"{rides[i]}: ${prices[i]:.2f}")
        if discount:
            print("This ride is discounted!")

        # Print a dash 40 times
    print('-' * 40)
loopy()