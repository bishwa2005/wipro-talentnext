# Travel Recommendation Program

distance = float(input("Enter the distance you want to travel (in miles): "))

if distance < 3:
    vehicle = "Bicycle"
elif distance < 300:
    vehicle = "Motor-Cycle"
else:
    vehicle = "Super-Car"

print(f"I suggest using a {vehicle} for your trip.")