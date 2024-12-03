# Dictionary full of info
aboutme = {
    "name": "Erin",
    "age": 33,
    "hobbies": ["video games", "cooking", "reading"],
    "wake-up": {"day": ["Monday", "Tuesday", "Saturday","Sunday"], "time":["8:00", "8:30", "10:00","9:30"]}
}

# Print out results stored in the dictionary
print(f"My name is {aboutme['name']} and I am {aboutme['age']} years old.")
print(f"My first hobby is {aboutme['hobbies'][0]}.")
print(f"I typically wake up on {aboutme['wake-up']['day'][3]} at {aboutme['wake-up']['time'][3]}")


# Use a loop to print out the key-value pairs in the dictionary
for key, value in aboutme.items():
    print(f"{key}: {value}")

# Use a loop to print out the keys of the wake-up dictionary
for key in aboutme['wake-up'].keys():
    print(key)

# Use a loop to print out the values of the wake-up dictionary
for value in aboutme['wake-up'].values():
    print(value)