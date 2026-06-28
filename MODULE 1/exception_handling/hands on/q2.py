try:
    num = int(input("Enter a number: "))

    if num <= 1:
        print("Not a Prime Number")
    else:
        prime = True

        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

        if prime:
            print("Prime Number")
        else:
            print("Not a Prime Number")

except ValueError:
    print("Error: Please enter a valid number.")