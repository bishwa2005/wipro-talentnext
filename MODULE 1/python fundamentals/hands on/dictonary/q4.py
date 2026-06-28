student = {
    "Name": "Rahul",
    "Age": 20,
    "City": "Delhi"
}

print("Keys:")
for key in student:
    print(key)

print("\nValues:")
for value in student.values():
    print(value)

print("\nKeys and Values:")
for key, value in student.items():
    print(key, ":", value)