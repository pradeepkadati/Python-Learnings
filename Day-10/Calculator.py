# Calculator

# Add Function
def add(n1, n2):
    return n1+n2


# Subtraction
def subtract(n1, n2):
    return n1-n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Division
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
for key in operations:
    print(key)
operation = input("Which operations do you want to perform:")

function = operations[operation]
op_value = function(num1, num2)
print(f"{num1} {operation} {num2} is {op_value}")