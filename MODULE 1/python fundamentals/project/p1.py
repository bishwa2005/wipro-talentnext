people = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}

print("Original List:")

for person in people:
    print(person + ":", people[person])

people["Jeff"] = "Is afraid of heights."

people["Jill"] = "Can hula dance."

print("\nUpdated List:")

for person in people:
    print(person + ":", people[person])