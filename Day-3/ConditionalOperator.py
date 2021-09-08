print("Welcome to rollercoaster")

height = int(input("Enter your height"))


if height >= 120:
    print("Welcome to the ride")
    age = int(input("What is your age:"))
    if age > 18:
        print(" 12$ Ticket ")
    elif 18 >= age >= 12:
        print(" 7$ Ticket")
    else:
        print(" 5$ Ticket")
else:
    print("Grow up kid")