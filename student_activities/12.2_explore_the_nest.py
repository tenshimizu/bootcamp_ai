# List of lists of birds
birds_list = [
    ["Magpie", "Cockatoo", "Hummingbird", "Ostrich", "Bald Eagle", 
     "Emperor Penguin", "Lyrebird", "Peacock", "Toucan", "Helmeted Hornbill"],
    [60, 70, 10, 270, 100, 129, 90, 105, 60, 120],
    [210, 900, 5, 136000, 26000, 112000, 5200, 28600, 4180, 2900],
    [3.5, 45, 5, 40, 30, 20, 30, 15, 20, 30]
]

# List of bird dictionaries
birds_dictionaries = [
    {
        "name": "Magpie",
        "size (cm)": 60,
        "weight (g)": 210,
        "lifespan": 3.5
    },
    {
        "name": "Cockatoo",
        "size (cm)": 70,
        "weight (g)": 900,
        "lifespan": 45
    },
    {
        "name": "Hummingbird",
        "size (cm)": 10,
        "weight (g)": 5,
        "lifespan": 5
    },
    {
        "name": "Ostrich",
        "size (cm)": 270,
        "weight (g)": 136000,
        "lifespan": 40
    },
    {
        "name": "Bald Eagle",
        "size (cm)": 100,
        "weight (g)": 26000,
        "lifespan": 30
    },
    {
        "name": "Emperor Penguin",
        "size (cm)": 129,
        "weight (g)": 112000,
        "lifespan": 20
    },
    {
        "name": "Lyrebird",
        "size (cm)": 90,
        "weight (g)": 5200,
        "lifespan": 30
    },
    {
        "name": "Peacock",
        "size (cm)": 105,
        "weight (g)": 28600,
        "lifespan": 15
    },
    {
        "name": "Toucan",
        "size (cm)": 60,
        "weight (g)": 4180,
        "lifespan": 20
    },
    {
        "name": "Helmeted Hornbill",
        "size (cm)": 120,
        "weight (g)": 2900,
        "lifespan": 30
    }
]

# Print out the data about the 4th bird in birds_list
for bird in birds_list:
    print(bird[3])

# Calculate the total weight (kg) of all the birds in the birds list
total_weight_kg = sum(birds_list[2])/1000
print(round(total_weight_kg,3))

# Loop through the birds_dictionaries list
     # Print the names of the birds and their lifespans from the birds_dictionary
     # Calculate and print out the size to weight ratio
for birds in birds_dictionaries:
    print(f"{birds['name']} has a lifespan of {birds['lifespan']} years.It's size to weight ratio is {birds['size (cm)']/birds['weight (g)']}")  

# Which bird in the bird_dictionary has the highest size to weight ratio (lightest weight for its size)?: 
for bird in birds_dictionaries:
    if bird['size (cm)']/bird['weight (g)'] == max(bird['size (cm)']/bird['weight (g)'] for bird in birds_dictionaries):
        print(f"{bird['name']} has the highest size to weight ratio.")
    if bird['size (cm)']/bird['weight (g)'] == min(bird['size (cm)']/bird['weight (g)'] for bird in birds_dictionaries):
        print(f"{bird['name']} has the lowest size to weight ratio.")

