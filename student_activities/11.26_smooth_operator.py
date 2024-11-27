def vacay_plan():# Declare variables
    budget = 2000
    cities = ["Rome", "Nairobi", "Phnom Penh", "Santiago", "Toronto", "Rotorua"]
    cities_daily_cost = [150, 70, 60, 80, 110, 125]
    days = input("How many days can you travel? ")
    # Check if days is a number, and convert it to an integer if it is
    if days.isnumeric():
        days = int(days)
    # Else print an error
    else:
        print("Error: Days must be a number")
        
    # Check if budget and days are integers, and if so, calculate the daily budget
    if isinstance(budget, int) and isinstance(days, int):
        daily_budget = budget / days
        print(f"Your daily budget is ${daily_budget}")
    # Else print an error
    else:
        print("Error: Budget and days must be numbers")

    city_to_visit = input("What city would you like to visit? ")
    # Check if the city_to_visit is in the cities list, and if so,
    # get the daily cost for the city
    if city_to_visit in cities:
        city_daily_cost = cities_daily_cost[cities.index(city_to_visit)]
        print(f"It will cost ${city_daily_cost} per day to travel to {city_to_visit}")
    # Else set the city_daily_cost to 0 to be used for error checking
    else:
        city_daily_cost = 0
        print("Error: City not found")  

    # Check if the city_daily_cost is greater than 0 and equal to or less than the
    # daily budget, and if so, tell the traveler they can afford the vacation
    if city_daily_cost > 0 and city_daily_cost <= daily_budget:
        print(f"You can afford to travel to {city_to_visit}!")
    # Else if the city_daily_cost is greater than 0 and greater than the daily budget,
    # calculate and print out how much more per day the traveler needs
    elif city_daily_cost > 0 and city_daily_cost > daily_budget:
        print(f"You cannot afford to travel to {city_to_visit}.")
        print(f"You need ${city_daily_cost - daily_budget} more per day to travel to {city_to_visit}.")
    # Else print an error
    else:
        print("Error")
vacay_plan()