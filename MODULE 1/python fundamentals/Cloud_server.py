# Cloud Server Cost Calculator

hourly_rate = 0.51

# Cost calculations
daily_cost = hourly_rate * 24
weekly_cost = daily_cost * 7
monthly_cost = daily_cost * 30

# Budget given
budget = 918

# Number of days the server can run
days_possible = budget / daily_cost

# Display results
print("Cloud Server Cost Analysis")
print("-" * 30)

print(f"Cost per day   : ${daily_cost:.2f}")
print(f"Cost per week  : ${weekly_cost:.2f}")
print(f"Cost per month : ${monthly_cost:.2f}")
print(f"Days server can run with ${budget}: {days_possible:.2f} days")