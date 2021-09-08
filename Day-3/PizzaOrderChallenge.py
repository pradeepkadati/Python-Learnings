print("Order Your Pizza")

pizza_size = input("What size of pizza do you want? S,M or L:")

billAmt = 0

if pizza_size == "S":
    bill = 15
elif pizza_size == "M":
    bill = 20
elif pizza_size == "L":
    bill = 25

add_pep = input("Would you like to add pepperoni")
if add_pep == "Y" and pizza_size == "S":
    bill += 2
elif add_pep == "Y" and (pizza_size == "L" or pizza_size == "M"):
    bill += 3


extra_Cheese = input("Would you like to have extra Cheese")
if extra_Cheese == "Y":
    bill += 1

print(f"Your Bill Would be ${bill}")
