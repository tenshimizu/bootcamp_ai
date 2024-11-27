def print_pres():
    # Declare pi
    pi = 3.14159265358979323846
    # Print a string that uses the new line character
    # Ask the user for a name and store it as a variable
    name = input(f"Hello!\nWhat is your name? ")
    # Use an f-string to print the name in title case, along with something they 
    # said that uses both single and double quotation marks
    print(f'{name.title()} said: "I am happy"')
    # Ask the user for the number of dashes that should be displayed in the 
    # presentation and convert it to an integer
    dashes = int(input("How many dashes? "))

    # Ask the user for the radius of a circle and convert it to a float
    radius = float(input("What is the radius of a circle? "))
    # Print out the dashes
    print("-"*dashes)
    # Use a multiline f-string to print out the radius, surface area, and volume
    # of a sphere to 4 decimal places using the radius from the user input.
    print(f"Radius: {radius}\nSurface Area: {round(4*pi*radius**2,4)}\nVolume: {round((4/3)*pi*radius**3,4)}")
        
print_pres()