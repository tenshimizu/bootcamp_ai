def vac_calc():
    pi = float(3.14159265358979323846)
    # Ask the user what their vacation budget is and convert it to a float
    budget = float(input("Hello! Thank you for using Vacay Calc! \nI have a few quick questions about your vacation!\nWhat is your total vacation budget? "))
    # Ask the user how much of their budget should be spent on flights and 
    # accommodation and convert it to a float
    flights_accommodation = float(input("What is your budget for the flights and accommodation? "))
    # Ask the user how many days they will go on vacation and convert it to an
    # integer
    vacation_days = int(input(f"Fantastic! That means that you will have ${budget-flights_accommodation} leftover to spend.\nHow many days will you go on vacation? "))
    # Ask the user how much they would like to spend per day and convert it to a float
    daily_budget = float(input(f"Awesome! Based on my calculations you should spend no more than ${round((budget-flights_accommodation)/vacation_days,2)} per day to stay within your budget.\nWhat is your preferred daily budget? "))
    # Ask the user the currency exchange rate for the country they're visiting and
    # convert it to a float
    exchange_rate = float(input("What is the currency exchange rate? "))
    # Ask the user for the radius distance they're willing to walk from their
    # hotel and convert it to a float
    distance = float(input("What is the radius distance you're willing to walk from your hotel (in meters)? "))
    amount_spent = (daily_budget*vacation_days)
    # Calculate the budget remaining after flights and accommodation
    budget_remaining = (budget-flights_accommodation)
    # Calculate the remaining budget in local currency amount
    remaining_budget_local = (budget_remaining*exchange_rate)
    # Calculate the budget per day in the local currency
    daily_budget_local = (daily_budget*exchange_rate)
    # Calculate the budget per day in the local currency, ignoring cents
    rounded_daily_budget_local = (round(daily_budget*exchange_rate))
    # Calculate the total area around the hotel the user can walk within
    # Area of a circle = pi * radius ** 2
    walking_area = round(pi*distance**2,2)
    # Calculate the amount left from the budget if the user sticks with their
    # daily budget.
    budget_left = (budget_remaining-amount_spent)

    print(f"Thank you! Here is a breakdown of your vacation:\n    -Total Budget:${budget}\n    -Budget After Flights and Accommodations:${budget_remaining}\n    -Remaining budget: {remaining_budget_local} (local currency)\n    -Daily Budget: {daily_budget_local} (local currency)\n    -Daily Budget Simplified: {rounded_daily_budget_local}\n    -Walking Area: {walking_area} square meters\n    -Budget Remaining: ${budget_left} USD")

vac_calc()



