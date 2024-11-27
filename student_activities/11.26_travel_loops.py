def vacay_tool():
    # Declare lists
    cities = ["Rome", "Nairobi", "Phnom Penh", "Santiago", "Toronto", "Rotorua"]
    cities_daily_cost = [150, 70, 60, 80, 110, 125]

    # Loop 3 times through the cities list
    x = 1 
    while x <=3:
        print(cities)
        x += 1           

    # Ask the user for a city and convert it to title case
    new_city = input("Enter a city: ")
    # Append the city to the cities list
    cities.append(new_city.title()) 
    print(cities)
    # Use a while loop to append to the cities_daily_cost list as long as that list
    # is shorter than the cities list
    # Use the length of cities_daily_cost for the index of cities to print its
    # value when asking the cost to append to the cities_daily_cost list
    while len(cities_daily_cost) < len(cities):
        cities_daily_cost.append(int(input("Enter a daily cost: ")))
        print(cities_daily_cost.index(cities_daily_cost[-1]))

    # Loop through the cities_daily_cost list and add 10 to each item
    print(cities_daily_cost)
    cities_daily_cost = [x+10 for x in cities_daily_cost]
    print(cities_daily_cost)
    # Use a for loop to loop through both of the lists at the same time, since
    # they're the same length, and print out the city and daily cost on the same
    # line
    for city, cost in zip(cities, cities_daily_cost):
        print(f"{city}: ${cost}")
vacay_tool()