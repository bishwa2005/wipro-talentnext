numbers = [10, -5, 8, -2, 15, -7, 20, -9, 12, -1]

try:
    index = int(input("Enter index: "))

    value = numbers[index]

    if value >= 0:
        print("Positive Number")
    else:
        print("Negative Number")

except IndexError:
    print("Error: Invalid index.")

except ValueError:
    print("Error: Please enter a valid index.")

except Exception:
    print("Something went wrong.")