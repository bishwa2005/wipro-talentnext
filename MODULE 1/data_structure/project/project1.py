# Dictionary storing people and their interesting facts

people_facts = {
    "Jeff": "is afraid of dogs",
    "David": "plays the piano",
    "Jason": "can fly an airplane"
}

print("Original Data:")
for person, fact in people_facts.items():
    print(f"{person}: {fact}.")

# Updating a fact
people_facts["Jeff"] = "is afraid of heights"

# Adding a new person
people_facts["Jill"] = "can hula dance"

print("\nUpdated Data:")
for person, fact in people_facts.items():
    print(f"{person}: {fact}.")